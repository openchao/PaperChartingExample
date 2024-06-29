#  -*- coding: utf-8 -*-
# @Author  : zhouchao
# @File    : DCL
# @Time    : 2023/10/10 18:23
# @Software: PyCharm
import numpy as np
import matplotlib.pylab as plt
import matplotlib
from matplotlib.patches import Circle

label_size = 50 * 3 * 2 * 1.5
font = {'family': 'Times New Roman', }
#         # 'weight': 'bold',
#         'size': f'{label_size}'}
#
matplotlib.rc("font", **font)
size = 1.5
data = [0.008682483	,		0.004158104		,		0.002475269			,	0.003653386	,			0.001695533
]
data =[0.006052308, 0.002496604, 0.00218448, 0.001866566, 0.001279369
        ]

bar_width = 2
x = [i for i in range(0, 5 * 6, 6)]
x2 = [i+2 for i in range(0, 5 * 6, 6)]

print(x)
model_names = ['BPR', 'BUIR', 'LightGCN', 'DirectAU', 'DCF']
colors = [(31 / 225, 127 / 225, 184 / 225), (95 / 225, 158 / 225, 110 / 225), (181 / 225, 93 / 225, 96 / 225),
          (57 / 225, 173 / 225, 195 / 225), (114 / 225, 200 / 225, 189 / 225)]

f, axs = plt.subplots(1, 2, figsize=(6 * 2 *1.1, 3 * 2*1.1), dpi=200)
for i in range(5):
    axs[1].bar(x[i], data[i], color=colors[i], width=bar_width,hatch='/' )
axs[1].grid(True, alpha=0.6)
axs[1].set_xticks([1, 7, 13, 19, 25], model_names, fontsize=12 * size)

axs[1].set_ylabel('Ave.', fontsize=7 * 2 * size)
axs[1].set_xlabel('Model', fontsize=7 * 2 * size)


# yelp
data = [0.003189886, 0.002177351, 0.001980116, 0.001263561, 0.000607332]


axs[1].bar(x[0], 0, color='w', width=bar_width, label='Beauty', hatch='/')
axs[1].bar(x2[0], 0, color='w', width=bar_width, label='Yelp', hatch='O')

for i in range(5):
    axs[1].bar(x2[i], data[i], color=colors[i], width=bar_width, hatch='O')
axs[1].grid(True, alpha=0.6)
# axs[1].set_xticks([])
axs[1].set_yticks([0.00, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006], [0.00, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006], fontsize=12 * size)
axs[1].set_title('Margin Metric', fontsize=14 * size)
# axs[1].scatter([0],[0.014],c='w')
axs[1].legend(fontsize=12 * size)



# 画圆
embs = np.load('embd2/454/DirectAU_Beauty_user-LGCN_norm2.npy')


tick_size = 50*2*1.2
linewidth = 10 * 2*2
markersize = 20 * 2
labelsize = 60 * 1.3*2*1.2
legendsize = 80
hard_linewidth = 20 * 1.5 * 10*2*2*1.5*1.5

center = np.mean(embs, axis=0)
distances = np.linalg.norm(embs - center, axis=1)
radius = np.max(distances)
radius_id = np.where(distances>=radius)
print(radius_id[0][-1])

# 圆心和半径
circle_center = tuple(center)
circle_radius = radius
circle_radius_ = str(np.around(circle_radius, 2))
ticks = 135 * 1.3
axs[0].plot([circle_center[0], embs[radius_id[0][-1]][0]],
         [circle_center[1], embs[radius_id[0][-1]][1]],
         linewidth=8, alpha=0.95, label=f'R={circle_radius_}', color=colors[2],linestyle='--')
circ = Circle(circle_center, circle_radius+0.002, color='k', linestyle='--', linewidth=4,
                          fill=False)  # 圆心，半径，颜色，α
axs[0].add_patch(circ)
axs[0].scatter(embs[:, 0], embs[:, 1], c=colors[0], alpha=0.8, s=80)

axs[0].set_yticks([-0.075, -0.05, -0.025, 0, 0.025, 0.05, 0.075], [-0.075, -0.05, -0.025, 0, 0.025, 0.05, 0.075], fontsize=12 * size)
axs[0].set_xticks([-0.075, -0.05, -0.025, 0, 0.025, 0.05, 0.075], [-0.075, -0.05, -0.025, 0, 0.025, 0.05, 0.075], fontsize=12 * size)
axs[0].set_ylabel('Feature', fontsize=7 * 2 * size)
axs[0].set_xlabel('Feature', fontsize=7 * 2 * size)
axs[0].set_title('Distribution', fontsize=14 * size)

plt.subplots_adjust(left=0.085, right=0.996, top=0.935, bottom=0.12, wspace=0.2)
plt.savefig('images/Margin_Metric.pdf', dpi=200)
