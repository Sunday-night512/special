
import math
from math import sin
from cmath import log10
import xlwt
from xlwt import *
import matplotlib.pyplot as plt

#function=input("输入一个函数：")
#variable=input("输入自变量：")
vmin_range=float(input("输入下限："))
vmax_range=float(input("输入上限："))
#num=int(input("输入一个整数："))
num=1000
dx=(vmax_range-vmin_range)/num
h=dx*10
a=[]
b=[]
c=[]
a1=float(vmin_range)
while a1<vmax_range:
    c.append(a1)
    a1+=dx
print(len(c))
print(c[len(c)-1])
def w_1(r):
    abs_r=abs(r)
    if (r/h<=1 and r/h>=-1):
        if abs_r==0:
            ans=0
        else:
            ans=5/(4*h)*(1-abs_r/h)**2*(-12*abs_r/h)*r/abs_r/h
    else:
        ans=0
    return ans

def f_1(x):
    total=0
    x_1=x-h
    while x_1<=(x+h):
       total-=dx*sin(x_1)*w_1(x_1-x)
       x_1+=dx
    return total

j=0
#file=xlwt.Workbook(encoding='utf-8')
#table=file.add_sheet("data")
while j<=999:
    a.append(f_1(c[j]))
#    table.write(j, 0, f_1(c[j]))
    b.append(sin(c[j]))
#    table.write(j, 1, log10(c[j]))
#    m=float(vmin_range)+dx*(j-1)
#    table.write(j,2,m)
    j+=1
#file.save("d://xt1.xls")
while len(c)!=len(a):
    while len(c)>len(a):
        c.pop()
    while len(c)<len(a):
        a.pop()
while len(c)!=len(b):
    while len(c)>len(b):
        c.pop()
    while len(c)<len(b):
        b.pop()


print(len(a))
print(len(b))
plt.plot(c,a)
plt.plot(c,b)
plt.show()
#print(c)
#print(a)
#print(b)
