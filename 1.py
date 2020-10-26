import math
import numpy

#离散化
dx = 10**-4
dy = 10**-4
dz = 1

#光滑半径
h=3*dx

#光滑函数：输入量是坐标
def dw(x1,y1,x2,y2):
    r = ((x2-x1)**2+(y2-y1)**2)**0.5
    #v = [(x2-x1)/r,(y2-y1)/r] #单位矢量
    R = r/h
    if R<=1:
        A = 5/(math.pi*h**2)*(1-R)**2*(-12*R)/h
        return [A*(x2-x1)/r,A*(y2-y1)/r]
    else:
        return [0,0]
    
X=[]
Y=[]
#实现粒子坐标的初始化
for i in range(200):
    X.append(i*dx)
    Y.append(i*dx)
for j in range(100):
    X[100+j]+=5
    
#m = 18.087*10**-5

#实现对密度、速度的初始化
size = numpy.zeros((200, 200))
density=numpy.zeros((200, 200))
uleft = numpy.zeros((200,100))
uright = numpy.zeros((200, 100))
for ai in range(200):
    for aj in range(200):
        density[ai][aj]=18.087*10**3   #kg/m^3
#        if aj <= 99:
#            size[ai][aj] = aj*dx
#        if aj>99:
#            size[ai][aj]= 5+aj*dx
for ai in range(200):
    for aj in range(100):
        uleft[ai][aj]=500
        uright[ai][aj]=0



#对于一个i粒子
x1 = 0
y1=0
Sum = 0
krou=[]
for ai in range(200):
    for aj in range(200):
        if aj<=99:
            Sum+=density[ai][aj]*dx*dy*dz*(uleft[x1][y1]-uleft[ai][aj])*dw(y1*dy,(0.02-x1*dx),ai,aj)[0]
        else:
            Sum+=density[ai][aj]*dx*dy*dz*(uleft[x1][y1]-uright[ai][aj-100])*dw((距离+y1*dy),y1,ai,aj)[0]
krou.append(Sum)
Sum = 0





