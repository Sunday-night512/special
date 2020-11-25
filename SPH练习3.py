import math
import numpy
import matplotlib.pyplot as plt


 
dx = 10**-3
dy = 10**-3
dz = 1
dt = 3*10**-7 #0.3微秒
h=2*dx
c0=2.51*10**3
s=1.51
Grun = 2.13 # Gruneisen参数取2
def dw(x1,y1,x2,y2):
    r = ((x2-x1)**2+(y2-y1)**2)**0.5
    R = r/h
    if R<=1:
        A = 5/(math.pi*h**2)*(1-R)**2*(-12*R)/h
        return [-A*(x2-x1)/r,-A*(y2-y1)/r]
    else:
        return [0,0]
X = numpy.zeros((20, 20))
Y = numpy.zeros((20, 20))
density=numpy.zeros((20, 20))
ux=numpy.zeros((20, 20))
uy=numpy.zeros((20, 20))
Ph = numpy.zeros((20, 20))
eH = numpy.zeros((20, 20))
e = numpy.zeros((20, 20))
p =  numpy.zeros((20, 20))
x1 = X[10]
for ai in range(20):
    for aj in range(20):
        density[ai][aj]=18.087*10**3   #kg/m^3
        uy[ai][aj]=0
        Y[ai][aj] = (20-ai)*dy
        X[ai][aj] = aj*dx
        e[ai][aj]=0
        if aj<=9:
            ux[ai][aj]=500
        else:
            ux[ai][aj]=0
for ti in range(2):

    #对于某一时刻
    print("密度")
    for bi in range(20):
        for bj in range(20):
    #对于一个(bi,bj)粒子
            Sum = 0
            for ai in range(20):
                for aj in range(20):
                    if ai!=bi or aj!=bj:
                        ju_1=[ux[bi][bj]-ux[ai][aj],uy[bi][bj]-uy[ai][aj]]

                        ju_2 = dw(X[bi][bj],Y[bi][bj],X[ai][aj],Y[ai][aj])

                        Sum+=density[ai][aj]*dx*dy*dz*(ju_1[0]*ju_2[0]+ju_1[1]*ju_2[1])

            density[bi][bj]+=Sum*dt
            rou = 1/density[bi][bj]
            rou0 = 1/(18.087*10**3)
            Ph[bi][bj]=c0**2*(rou0-rou)/(rou0-s*(rou0-rou))**2
            eH[bi][bj]=0.5*Ph[bi][bj]*(density[bi][bj]-18.087*10**3)/(density[bi][bj]*18.087*10**3)
            p[bi][bj]=-1*(Ph[bi][bj]+Grun*density[bi][bj]*(e[bi][bj]-eH[bi][bj]))
        print("进行了"+str(bi)+"行")
    
    #==========================================================
    print("速度")    
    for bi in range(20):
        for bj in range(20):

            dux = 0
            duy = 0
            for ai in range(20):
                for aj in range(20):
                    if ai!=bi or aj!=bj:
                        ju_1=[p[bi][bj],0]
                        ju_2=dw(X[bi][bj],Y[bi][bj],X[ai][aj],Y[ai][aj])
                        ju_3=[p[ai][aj],0]
                        ju_4=[0,p[bi][bj]]
                        ju_5=[0,p[ai][aj]]

                        dux += (density[ai][aj]*dx*dy*dz*((numpy.dot(ju_1,ju_2))/density[bi][bj]**2+numpy.dot(ju_3,ju_2)/density[ai][aj]**2))
  
                        duy += (density[ai][aj]*dx*dy*dz*((numpy.dot(ju_4,ju_2))/density[bi][bj]**2+numpy.dot(ju_5,ju_2)/density[ai][aj]**2))

            ux[bi][bj]+=dux*dt
            uy[bi][bj]+=duy*dt
        print("进行了"+str(bi)+"行")
    print("能量")    
    for bi in range(20):
        for bj in range(20):
            de=0
            for ai in range(20):
                for aj in range(20):
                    if ai!=bi or aj!=bj:
                        ju_1=[p[bi][bj],0]
                        ju_2=dw(X[bi][bj],Y[bi][bj],X[ai][aj],Y[ai][aj])
                        ju_3=[p[ai][aj],0]
                        ju_4=[0,p[bi][bj]]
                        ju_5=[0,p[ai][aj]]
                        ju_6 = [ux[bi][bj]-ux[ai][aj],uy[bi][bj]-uy[ai][aj]]
                        dux = (density[ai][aj]*dx*dy*dz*((numpy.dot(ju_1,ju_2))/density[bi][bj]**2+numpy.dot(ju_3,ju_2)/density[ai][aj]**2))
                        duy = (density[ai][aj]*dx*dy*dz*((numpy.dot(ju_4,ju_2))/density[bi][bj]**2+numpy.dot(ju_5,ju_2)/density[ai][aj]**2))
                        de+=0.5*(numpy.dot(ju_6,[dux,duy]))
            e[bi][bj]+=de/10**6
        print("进行了"+str(bi)+"行")

    #位置的变化
    for ai in range(20):
        for aj in range(20):
            Y[ai][aj] +=uy[ai][aj]*dt
            X[ai][aj] +=ux[ai][aj]*dt

            
x1 = [x*10 for x in x1]          #将坐标单位换算成cm
pshow = [x/10**11 for x in p[10]]#将压强单位换算成100Gpa
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.figure(1,figsize=(12,6))
plt.subplot(1, 2, 1)
plt.xlabel("位置(cm)")
plt.ylabel("轴线速度ux(m/s)")
plt.plot(x1,ux[10],marker = "o")

plt.subplot(1, 2, 2)
plt.xlabel("位置(cm)")
plt.ylabel("轴线压力P(100Gpa)")
plt.plot(x1,pshow,marker = "o")
plt.show()






