import xlwt
from xlwt import *
import matplotlib.pyplot as plt

dt=0.001
v_1=3.0
v_2=0.0
v_3=0.0
x_1=0.0
x_2=5.0
x_3=10.0
a_1=0.0
a_2=0.0
a_3=0.0
m1=1
m2=2
m3=3
t1=0.0
k=10
T=[]
X1=[]
X2=[]
X3=[]
#file=xlwt.Workbook(encoding='utf-8')
#table=file.add_sheet("data1")
j=1
while t1<=10.0:
    f1=k*(x_2-x_1-4)
    f2=k*(x_3-x_2-4)
    a_1=f1/m1
    a_2=(-f1+f2)/m2
    a_3=-f2/m3

    v_1=v_1+a_1*dt
    v_2 = v_2 + a_2 * dt
    v_3 = v_3 + a_3 * dt

    x_1=x_1+v_1*dt
    x_2=x_2+v_2*dt
    x_3 = x_3 + v_3 * dt



    T.append(t1)
    X1.append(x_1)
    X2.append(x_2)
    X3.append(x_3)
#    table.write(j, 0, x_1)
 #   table.write(j, 1, x_2)
  #  table.write(j, 2, x_3)
   # table.write(j, 3, t1)
    j+=1
    t1+=dt
#file.save("d://弹簧.xls")
plt.plot(T,X1)
plt.plot(T,X2)
plt.plot(T,X3)
plt.show()



