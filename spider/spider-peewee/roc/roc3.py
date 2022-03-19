import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * (np.pi))  #numpy.linspace(开始，终值(含终值))，个数)
y1 = np.sin(x)
y2 = np.cos(x)

#画图
plt.title('Compare cosx with sinx')  #标题
#plt.plot(x,y)
#常见线的属性有：color,label,linewidth,linestyle,marker等
plt.plot(x, y1, color='cyan', label='sinx')
plt.plot(x, y2, 'b', label='cosx')#'b'指：color='blue'
plt.legend()  #显示上面的label
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0, 2*np.pi, -1, 1])#设置坐标范围axis([xmin,xmax,ymin,ymax])
#plt.ylim(-1,1)#仅设置y轴坐标范围
plt.show()