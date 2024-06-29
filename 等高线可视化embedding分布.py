#  -*- coding: utf-8 -*-
# @Author  : zhouchao
# @File    : 
# @Time    : 2023/10/9 13:48
# @Software: PyCharm
import seaborn as sns
import matplotlib.pylab as plt
import numpy as np
import os
import matplotlib

font = {'family': 'Times New Roman', }
#         # 'weight': 'bold',
#         'size': f'{label_size}'}
#
matplotlib.rc("font", **font)
dirnames = ['1561', '1756', '1953', '454', '470', '515', '52', '695', '855', '884']

f, axs = plt.subplots(2, 2, figsize=(6, 6), dpi=200)
row = 0
col = 0
model_names = [['User of LightGCN on Yelp', 'User of DirectAU on Beauty'], ['Item of LightGCN on Yelp', 'Item of DirectAU on Beauty']]
filenames = \
    ['LightGCN_Yelp_user-LGCN_norm2.npy', 'DirectAU_Beauty_user-LGCN_norm2.npy',
     'LightGCN_Yelp_item-LGCN_norm2.npy', 'DirectAU_Beauty_item-LGCN_norm2.npy',
     ]

for dirname in filenames:
    if '.npy' in dirname:
        embs = np.load(f'./embd2/{dirname}')
        if col == 2:
            col = 0
            row += 1
        sns.kdeplot(x=embs[:, 0], y=embs[:, 1], cmap='GnBu', fill=True, legend=True, ax=axs[row][col])
        name = model_names[row][col]

        axs[row][col].set_title(name, fontsize=15)
        if col == 0:
            axs[row][col].set_xticks([-0.01, 0, 0.01],[-0.01, 0, 0.01], fontsize=14)
            axs[row][col].set_yticks([-0.01, 0, 0.01],[-0.01, 0, 0.01], fontsize=14)
        else:
            if row !=0:
                axs[row][col].set_xticks([-0.02, 0, 0.02], [-0.02, 0, 0.02], fontsize=14)
                axs[row][col].set_yticks([-0.02, 0, 0.02], [-0.02, 0, 0.02], fontsize=14)
            else:
                axs[row][col].set_xticks([-0.02, 0, 0.02], [-0.02, 0, 0.02], fontsize=14)
                axs[row][col].set_yticks([-0.01, 0, 0.01], [-0.01, 0, 0.01], fontsize=14)
        axs[row][col].set_ymargin(0.2)
        col += 1
axs[1][0].set_ylabel(' ' * 60 + 'Features', fontsize=14)
axs[1][0].set_xlabel(' ' * 60 + 'Features', fontsize=14)
plt.subplots_adjust(left=0.131, right=0.97, top=0.96, bottom=0.08, wspace=0.3, hspace=0.3)
# plt.show()
plt.savefig(f"images/等高线可视化embedding分布.pdf", dpi=200)
plt.close()
