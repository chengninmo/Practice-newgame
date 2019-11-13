from matplotlib import pyplot as plt
import random
from matplotlib import font_manager
from matplotlib.ticker import MultipleLocator

#x和y一定是等长对应的，plot用，之后坐标刻度怎么显示可以根据情况改变。
x = range(0,4)

S_S = [78.4,67.7,71.2,84.4]  #s表示断句标签
WS_S = [78.2,67.3,70.9,84.3]
PS_S = [78.1,68.0,70.7,84.9]
WPS_S = [79.0,68.0,71.6,84.9]

W_W=[88.0,80.5,85.5,77.4]
WP_W=[88.4,81.4,84.8,78.2]
WS_W=[88.1,81.4,85.5,77.5]
WPS_W=[88.3,80.9,85.7,78.9]

#W_W=[93.2,88.3,88.5,85.3]
S_S=[78.4,67.7,71.2,84.4]
WP_WP=[77.8,64.6,70.3,68.6]
WS_WS=[82.3,74.5,77.9,75.7]
WPS_WS=[82.6,74.3,78.1,76.9]
WPS_WP=[78.0,64.3,71.4,69.7]
WPS_WPS=[73.6,60.0,65.7,68.1]

#y = [random.randint(0,7) for i in range(4)]
#y1 = [random.randint(0,7) for i in range(4)] #第二条线

my_font = font_manager.FontProperties(fname= r"C:\Windows\Fonts\simsun.ttc",size='large')#simsun.ttc
my_font.set_size(12)
plt.figure(figsize=(8,6), dpi=80)

#plt.plot(x,W_W,label='W_W',linestyle='--',linewidth=1,marker = '.')
plt.plot(x,WPS_W,label='WPS_W',color = 'b',linestyle='-',linewidth=1,marker = '.')
#plt.plot(x,S_S,label='S_S',linestyle = ':',linewidth=1,marker = '.')

plt.plot(x,WS_W,label='WS_W',color='r',linestyle = '-.',linewidth=1,marker = '.')
#plt.plot(x,WP_W,label='WP_W',color='r',linestyle = '-.',linewidth=1,marker = '.')
plt.plot(x,WS_S,label='WS_S',color='r',linestyle = '-.',linewidth=1,marker = '.')
plt.plot(x,WS_WS,label='WS_WS',color='r',linestyle = '-.',linewidth=1,marker = '.')
plt.plot(x,WPS_WS,label='WPS_WS',color = 'b',linestyle='-',linewidth=1,marker = '.')
#plt.plot(x,WPS_WP,label='WPS_WP',color = 'b',linestyle = '-',linewidth=1,marker = '.')
#plt.plot(x,WP_WP,label='WP_WP',color='r',linestyle = '--',linewidth=1,marker = '.')
#plt.plot(x,WPS_WPS,label='WPS_WPS',linestyle = '-.',linewidth=1,marker = '.')
#plt.plot(x,S_S,label='S_S',linestyle='--',linewidth=1,marker = '.')
#plt.plot(x,WS_S,label='WS_S',linestyle = '--',linewidth=1,marker = '.')
#plt.plot(x,PS_S,label='PS_S',linestyle = '--',linewidth=1,marker = '.')
plt.plot(x,WPS_S,label='WPS_S',color='b',linestyle = '-',linewidth=1,marker = '.')


#y_str = ['交{}个'.format(i) for i in y]
#x_str = ['{}岁'.format(i) for i in x]

_ytick_lables = [i/2 for i in range (132,180)]
#_ytick_lables = [i/2 for i in range (134,172)]
x_str = ['左传','梦溪笔谈','阅微草堂笔记','清史稿']
my_font1 = font_manager.FontProperties(fname= r"C:\Windows\Fonts\simsun.ttc",size=18)

plt.xticks(x,x_str,fontProperties = my_font1)
#plt.yticks(range(60,92,3),fontProperties = my_font)
plt.yticks(_ytick_lables[::3],fontProperties = my_font1)
plt.grid(alpha=0.2,linestyle=':') #绘制网格
plt.legend(prop = my_font.set_size(16),loc = 'best',) #添加图例，lengend这里传prop改字体


#添加描述信息
#plt.xlabel("测试集",fontproperties=my_font)
plt.ylabel("F1值/%",fontproperties=my_font)
plt.title('“W+P+S”和“W+S”标签层级下各项F1值',fontproperties = my_font)

plt.show()