#  -*- coding: utf-8 -*-
# @Author  : zhouchao
# @File    : 超参.py
# @Time    : 2023/10/11 13:47
# @Software: PyCharm
#  -*- coding: utf-8 -*-
# @Author  : zhouchao
# @File    : 画8张折线图.py
# @Time    : 2023/5/31 22:10
# @Software: PyCharm

import numpy as np
import matplotlib.pylab as plt
import matplotlib.lines as lines
import pandas as pd
import matplotlib

label_size = 50 * 3 * 2 * 1.5
import matplotlib

font = {'family': 'Times New Roman', }
matplotlib.rc("font", **font)


def read_data_from_excel(sheet_name):
    data = pd.read_excel("./超参.xlsx", sheet_name=sheet_name)
    return data


# sheet_names = ['RECALL', 'NDCG']
# x = [0.00,0.25,0.5,0.75,1]
# y1 = [0.142, 0.143, 0.144, 0.145, 0.146, 0.147]
# y2 = [0.111 , 0.1115, 0.112 , 0.1125, 0.113 , 0.1135]
# print(y2)
# f, axs = plt.subplots(1, 2, dpi=200, figsize=(6, 3))
# for i, name in enumerate(sheet_names):
#     data = read_data_from_excel(name)
#     alpha=0.8
#     tick_size = 50
#     linewidth = 10*2
#     markersize = 20*2
#     labelsize = 60*1.3
#     legendsize = 80
#     axs[i].plot(data['BT'], data['Beauty'], c='#7e78b6')
#     axs[i].set_xticks(x1, x, fontsize=14)
#     axs[i].set_ylim(min(y1), max(y1))
#     axs[i].set_yticks(y1, y1, fontsize=14)
#     axs[i].set_xlabel('BT', fontsize=14)
#     axs[i].set_ylabel(f'{name}(Beauty)', fontsize=14)
#     axs[i].grid(True, alpha=0.6)
#
#     ax2 = axs[i].twinx()
#     ax2.set_ylabel(f'{name}(Yelp)', fontsize=14)
#     axs[i].set_ylim(min(y2), max(y2))
#     ax2.set_yticks(y2, y2, fontsize=14)
#     ax2.plot(data['BT'], data['Yelp'],c='#3a8d45')
#     break
# plt.subplots_adjust(left=0.1, right=0.97, top=0.94, bottom=0.1, wspace=0.38)
# plt.show()


#  -*- coding: utf-8 -*-
# @Author  : zhouchao
# @File    : 超参.py
# @Time    : 2023/10/11 13:47
# @Software: PyCharm
#  -*- coding: utf-8 -*-
# @Author  : zhouchao
# @File    : 画8张折线图.py
# @Time    : 2023/5/31 22:10
# @Software: PyCharm

import numpy as np
import matplotlib.pylab as plt
import matplotlib.lines as lines
import pandas as pd
import matplotlib

label_size = 50 * 3 * 2 * 1.5
import matplotlib

font = {'family': 'Times New Roman', }
matplotlib.rc("font", **font)


def read_data_from_excel(sheet_name):
    data = pd.read_excel("./超参.xlsx", sheet_name=sheet_name)
    return data


#### batch size
sheet_names = ['batch_size_Beauty', 'batch_size_Aminer']
# sheet_names = ['embedding_size_Beauty', 'embedding_size_Aminer'
colors = [(31 / 225, 127 / 225, 184 / 225), (95 / 225, 158 / 225, 110 / 225), (181 / 225, 93 / 225, 96 / 225),
          (57 / 225, 173 / 225, 195 / 225), (114 / 225, 200 / 225, 189 / 225)]
x = [256, 512, 1024, 2048]
y1 = [0.142, 0.143, 0.144, 0.145, 0.146, 0.147]
# y2 = [0.11, 0.11, 0.116, 0.1135, 0.114, 0.114]
y2 = np.linspace(14.62, 14.15, 6)
y1 = [round(14.1+_*0.12, 2) for _ in range(6)]
print(y2)
# plt.figure(dpi=200, figsize=(3, 2.8))
f, axs = plt.subplots(1, 2, dpi=200, figsize=(6, 2.8))
name = sheet_names[0]
data = read_data_from_excel(name)
# name = 'Recall'
axs[1].plot(data['batch_size'], data['Recall'], c=colors[0], label='Recall', marker='s')
axs[1].set_xticks(data['batch_size'], x, fontsize=10)
axs[1].set_ylim(min(y1), max(y1))
axs[1].set_yticks(y1, y1, fontsize=10)
axs[1].set_xlabel(r'$B$', fontsize=10)
axs[1].set_ylabel(f'Recall', fontsize=10)
axs[1].set_title(f'Beauty', fontsize=12)
axs[1].grid(True, alpha=0.6)
axs[1].legend(loc='upper left', fontsize=8)

ax2 = axs[1].twinx()
ax2.set_ylabel(f'NDCG', fontsize=10)
y1 = [round(6.8+_*0.05, 2) for _ in range(6)]
ax2.set_ylim(min(y1), max(y1))
ax2.set_yticks(y1, y1, fontsize=10)
ax2.plot(data['batch_size'], data['NDCG'], c=colors[1], label='NDCG', marker='^')
# plt.subplots_adjust(left=0.2, bottom=0.15, right=0.78, top=0.98)
ax2.legend(loc='upper right', fontsize=8)

name = sheet_names[1]
data = read_data_from_excel(name)
# name = 'Recall'
axs[0].plot(data['batch_size'], data['Recall'], c=colors[0], label='Recall', marker='s')
axs[0].set_xticks(data['batch_size'], x, fontsize=10)
y1 = [round(46+_*1, 2) for _ in range(6)]
axs[0].set_ylim(min(y1), max(y1))
axs[0].set_yticks(y1, y1, fontsize=10)
axs[0].set_xlabel(r'$B$', fontsize=10)
axs[0].set_ylabel(f'Recall', fontsize=10)
axs[0].set_title(f'AMiner', fontsize=12)
axs[0].grid(True, alpha=0.6)
axs[0].legend(loc='upper left', fontsize=8)

ax2 = axs[0].twinx()
ax2.set_ylabel(f'NDCG', fontsize=10)
y1 = [round(30.8+_*0.4, 2) for _ in range(6)]
ax2.set_ylim(min(y1), max(y1))
ax2.set_yticks(y1, y1, fontsize=10)
ax2.plot(data['batch_size'], data['NDCG'], c=colors[1], label='NDCG', marker='^')
# plt.subplots_adjust(left=0.2, bottom=0.15, right=0.78, top=0.98)
ax2.legend(loc='upper right', fontsize=8)

plt.subplots_adjust(left=0.075, bottom=0.15, right=0.915, top=0.92, wspace=0.57)
# plt.show()
plt.savefig(f'images/batch_size.pdf')


# # sheet_names = ['batch_size_Beauty', 'batch_size_Aminer']
sheet_names = ['embedding_size_Beauty', 'embedding_size_Aminer']
colors = [(31 / 225, 127 / 225, 184 / 225), (95 / 225, 158 / 225, 110 / 225), (181 / 225, 93 / 225, 96 / 225),
          (57 / 225, 173 / 225, 195 / 225), (114 / 225, 200 / 225, 189 / 225)]
x1 = [1, 2, 3, 4]
x = [16, 32, 64, 128]
y1 = [0.142, 0.143, 0.144, 0.145, 0.146, 0.147]
# y2 = [0.11, 0.11, 0.116, 0.1135, 0.114, 0.114]
y2 = np.linspace(14.62, 14.15, 6)
print(y2)
# plt.figure(dpi=200, figsize=(3, 2.8))
f, axs = plt.subplots(1, 2, dpi=200, figsize=(6, 2.8))
name = sheet_names[0]
data = read_data_from_excel(name)
# name = 'Recall'
axs[1].plot(data['embedding_size'], data['Recall'], c=colors[0], label='Recall', marker='s')
axs[1].set_xticks(x1, x, fontsize=10)
y1 = [round(11 + _ * 1, 2) for _ in range(6)]
axs[1].set_ylim(min(y1), max(y1))
axs[1].set_yticks(y1, y1, fontsize=10)
axs[1].set_xlabel(r'$F$', fontsize=10)
axs[1].set_ylabel(f'Recall', fontsize=10)
axs[1].set_title(f'Beauty', fontsize=12)
axs[1].grid(True, alpha=0.6)
axs[1].legend(loc='lower left', fontsize=8)

ax2 = axs[1].twinx()
ax2.set_ylabel(f'NDCG', fontsize=10)
y1 = [round(5 + _ * 0.5, 2) for _ in range(6)]
ax2.set_ylim(min(y1), max(y1))
ax2.set_yticks(y1, y1, fontsize=10)
ax2.plot(data['embedding_size'], data['NDCG'], c=colors[1], label='NDCG', marker='^')
# plt.subplots_adjust(left=0.2, bottom=0.15, right=0.78, top=0.98)
ax2.legend(loc='lower right', fontsize=8)

name = sheet_names[1]
data = read_data_from_excel(name)
# name = 'Recall'
axs[0].plot(data['embedding_size'], data['Recall'], c=colors[0], label='Recall', marker='s')
axs[0].set_xticks(x1, x, fontsize=10)
y1 = [round(29 + _ * 5, 2) for _ in range(6)]
axs[0].set_ylim(min(y1), max(y1))
axs[0].set_yticks(y1, y1, fontsize=10)
axs[0].set_xlabel(r'$F$', fontsize=10)
axs[0].set_ylabel(f'Recall', fontsize=10)
axs[0].set_title(f'AMiner', fontsize=12)
axs[0].grid(True, alpha=0.6)
axs[0].legend(loc='lower left', fontsize=8)

ax2 = axs[0].twinx()
ax2.set_ylabel(f'NDCG', fontsize=10)
y1 = [round(15 + _ * 5, 2) for _ in range(6)]
ax2.set_ylim(min(y1), max(y1))
ax2.set_yticks(y1, y1, fontsize=10)
ax2.plot(data['embedding_size'], data['NDCG'], c=colors[1], label='NDCG', marker='^')
# plt.subplots_adjust(left=0.2, bottom=0.15, right=0.78, top=0.98)
ax2.legend(loc='lower right', fontsize=8)

plt.subplots_adjust(left=0.075, bottom=0.15, right=0.926, top=0.92, wspace=0.42)
plt.savefig(f'images/embedding_size.pdf')
# plt.show()


# name = sheet_names[1]
# data = read_data_from_excel(name)
# axs[1].plot(data['BT'], data['Beauty'], c=colors[0], label='Beauty', marker='s')
# axs[1].set_xticks(x1, x, fontsize=10)
# axs[1].set_ylim(min(y1), max(y1))
# axs[1].set_yticks(y1, y1, fontsize=10)
# axs[1].set_xlabel(r'$\lambda$', fontsize=10)
# axs[1].set_ylabel(f'{name} (Beauty)', fontsize=10,labelpad=0.2)
# axs[1].grid(True, alpha=0.6)
# axs[1].legend(loc='lower left', fontsize=8)
#
# ax2 = axs[1].twinx()
# ax2.set_ylabel(f'{name} (Yelp)', fontsize=10)
# ax2.set_ylim(min(y2), max(y2))
# ax2.set_yticks(y2, y2, fontsize=10)
# ax2.plot(data['BT'], data['Yelp'],c=colors[1], label='Yelp', marker='^')
# ax2.legend(loc='lower right',  fontsize=8)
# plt.subplots_adjust(left=0.1, bottom=0.15, right=0.89, top=0.983, wspace=0.755)

# plt.show()
# plt.savefig(f'images/lambda.pdf')
