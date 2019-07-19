def train(self):
#卷积函数
    feature1=[]
    for i in range(int(len(self)/2)):
        a=self[i*2]
        feature1.append(a)
    feature2=[]
    for i in range(0,int(len(self)/3)):
        a=self[i*3]
        feature2.append(a)

    print(self)
    print(feature2)
    return feature2

x_data=[]
#非原生数据包
for i in range(10):
    a=input()
    x_data.append(a)

result=[]
tg=train(x_data)
for i in range(int(len(tg))):
    if int(tg[i])%2!=0:
        for j in range(1,3):        
            x_data[i*3],x_data[i*3+j]=x_data[j+i*3],x_data[i*3]
            tg=train(x_data)
            if int(tg[i])%2==0:
                a=tg[i]
                print('step',a)
                result.append(a)
     
            
    else:
        a=tg[i]
        print('step',a)
        result.append(a)

print('目标结果\n',result)
#找出偶数

