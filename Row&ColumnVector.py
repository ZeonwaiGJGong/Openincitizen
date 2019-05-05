class my_class(object):
    pass

Rv=[]
Cv=[]
Mtrx=[]
m=int(input('行向量元素的个数:'))
print('按(a1,Enter,a2,Enter,a3,Enter,...)的顺序输入元素')
for i in range(m):
    xm=int(input('第%d个为:'%(i+1)))
    Rv.append(xm)
n=int(input('列向量元素的个数:'))
print('按顺序输入列向量的元素:')
for j in range(n):
    xn=int(input('第%d个为:'%(j+1)))
    Cv.append(xn)
#数值输入

for k in range(int(len(Rv))):
    y=[]
    for l in range(int(len(Cv))):
        x=Rv[k]*Cv[l]
        y.append(x)
    Mtrx.append(y)
#生成数学矩阵

print('Matrix:')
for i in range(int(len(Cv))):
    for j in range(int(len(Rv))):
        z=Cv[i]*Rv[j]
        print(' %3ld '%(z),end='')
    print('')
#重组排列按计算习惯输出
print('In row:\n',Mtrx)
#计算机格式的输出




