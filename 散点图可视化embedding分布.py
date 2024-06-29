#  -*- coding: utf-8 -*-
# @Author  : zhouchao
# @File    : Dimension Independent Mixup for Hard Negative Sample in Collaborative Filtering
# @Time    : 2023/6/1 16:06
# @Software: PyCharm

import numpy as np
import matplotlib.pylab as plt
import matplotlib.lines as lines
import matplotlib
label = 135*1.3*2
font = {'family': 'Arial'} # 设置字体，论文一般用新罗马。字号介绍：https://blog.csdn.net/weishengxin_/article/details/126016819

matplotlib.rc("font", **font)

"""
论文中图，字号，线宽等组件大小调整技巧：
首先确定画布大小，然后再调整每个组件的大小，最后精调的时候可以按照一定的比例去调整。
例如 linewidth（线宽）这个参数我调整了4版：5*1.2*4*2
好看的配图可以去小红书上搜索，整篇论文的配色要统一，不然看起来很乱，也不要用太深太抢眼的颜色，这样会影响审稿人阅读。
"""
tick_size = 50*2*1.5*1.5
linewidth = 5*1.2*4*2
line_linewidth = 5*1.2*3*2
pos_linewidth = 10*2*3*25*2
hard_linewidth = 10*2*3*20*2
markersize = 20*2*2
labelsize = 60*1.3*2*2
legendsize = 80*2
titlesize = 1.2*80*2*1.6

s=2*1.6*1.2
f, (ax1, ax2, ax3) = plt.subplots(1, 3, dpi=200, figsize=(8*3*2*s, 8*2*s))

data1 = np.load(f'./27562_{"OUR"}.npy')
data2 = np.load(f'./27562_{"MIX"}.npy')
data3 = np.load(f'./27562_{"RNS"}.npy')

ax3.set_title('DINS sampling',fontsize=titlesize)
d1 = np.sum((data1[1:, ] - data1[0,]) ** 2, axis=1)
d = np.max(np.sqrt(d1))
d_ =str(np.around(d, 2))
data = data1-data1[0,]
ticks = 135*1.3
ax3.plot([data[0, 0], data[0, 0] + d * np.cos(-3.14 / 6)],
         [data[0, 1], data[0, 1] + d * np.sin(-3.14 / 6)],
         linewidth=line_linewidth, alpha=0.6, label=f'R={d_}', color='violet')
circ = plt.Circle((data[0, 0], data[0, 1]), d+0.02, color='k', linestyle='--', linewidth=linewidth, fill=False)  # 圆心，半径，颜色，α
ax3.add_patch(circ)

ax3.scatter(data[0, 0], data[0, 1], label='pos', c='b', marker='p', s=pos_linewidth)
ax3.scatter(data[1:, 0], data[1:, 1], label='hard', c='r', alpha=1, s=hard_linewidth)
ax3.set_xticks([i / 10 for i in range(-3, 3 + 2, 2)], [i / 10 for i in range(-3, 3 + 2, 2)],fontsize=tick_size)
ax3.set_yticks([i / 10 for i in range(-3, 3 + 2, 2)], [i / 10 for i in range(-3, 3 + 2, 2)],fontsize=tick_size)
ax3.set_xlabel("Dim 1",fontsize=label)
ax3.set_ylabel("Dim 2",fontsize=label)
ax3.legend(fontsize=legendsize)

ax1.set_title('RNS sampling',fontsize=titlesize)
d1 = np.sum((data3[1:, ] - data3[0,]) ** 2, axis=1)
# print(np.sqrt(d))
d = np.max(np.sqrt(d1))
d_ =str(np.around(d, 2))
data = data3-data3[0,]
# print(d_)
ax1.plot([data[0, 0], data[0, 0] + d * np.cos(-3.14 / 6)],
         [data[0, 1], data[0, 1] + d * np.sin(-3.14 / 6)],
         linewidth=line_linewidth, alpha=0.6, label=f'R={d_}', color='violet')

# 画圆圈
circ = plt.Circle((data[0, 0], data[0, 1]), d+0.02, color='k', linestyle='--', linewidth=linewidth, fill=False)  # fill 表示是否填充圆
ax1.add_patch(circ)

ax1.scatter(data[0, 0], data[0, 1], label='pos', c='b', marker='p', s=pos_linewidth) # 散点的形状：https://matplotlib.org/stable/api/markers_api.html
ax1.scatter(data[1:, 0], data[1:, 1], label='hard', c='r', alpha=1, s=hard_linewidth)
ax1.set_xticks([i / 10 for i in range(-4, 4 + 2, 2)], [i / 10 for i in range(-4, 4 + 2, 2)],fontsize=tick_size)
ax1.set_yticks([i / 10 for i in range(-4, 4 + 2, 2)], [i / 10 for i in range(-4, 4 + 2, 2)],fontsize=tick_size)
ax1.set_xlabel("Dim 1",fontsize=label)
ax1.set_ylabel("Dim 2",fontsize=label)
ax1.legend(fontsize=legendsize) # 设置图例的大小

ax2.set_title('MixGCF sampling',fontsize=titlesize)

d1 = np.sum((data2[1:, ] - data2[0,]) ** 2, axis=1)
d = np.max(np.sqrt(d1))

data = data2 - data2[0,]
ax2.plot([data[0, 0], data[0, 0] + d * np.cos(3.14 / 3)],
         [data[0, 1], data[0, 1] + d * np.sin(3.14 / 3)],
         linewidth=line_linewidth, alpha=0.6, label=f'R={d_}', color='violet')
circ = plt.Circle((data[0, 0], data[0, 1]), d+0.02, color='k', linestyle='--', linewidth=linewidth, fill=False)  # 圆心，半径，颜色，α
ax2.add_patch(circ)

ax2.scatter(data[0, 0], data[0, 1], label='pos', c='b', marker='p', s=pos_linewidth)
ax2.scatter(data[1:, 0], data[1:, 1], label='hard', c='r', alpha=1, s=hard_linewidth)
ax2.set_xticks([i / 10 for i in range(-4, 4 + 2, 2)], [i / 10 for i in range(-4, 4 + 2, 2)],fontsize=tick_size) # 设置x轴刻度显示的值
ax2.set_yticks([i / 10 for i in range(-4, 4 + 2, 2)], [i / 10 for i in range(-4, 4 + 2, 2)],fontsize=tick_size)
ax2.set_xlabel("Dim 1",fontsize=label)
ax2.set_ylabel("Dim 2",fontsize=label)
ax2.legend(loc='upper left', fontsize=legendsize) # loc用于设置图例的位置，形参可参考：https://blog.csdn.net/Wannna/article/details/102751689
plt.subplots_adjust(left=0.058, bottom=0.18, right=0.99) # 设置子图之间的间距
# plt.show()
plt.savefig(f"images/可视化embedding分布.pdf")

