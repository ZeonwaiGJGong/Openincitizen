def train(self):
#卷积函数
    feature1=[] 
    #feature1并没有使用于本次运行
    for i in range(int(len(self)/2)):
        a=self[i*2]
        feature1.append(a)
    feature2=[]
    #每隔两位抽出一位数值为特征
    for i in range(0,int(len(self)/3)):
        a=self[i*3]
        feature2.append(a)

    return feature2

x_data=[]
#用于非原始数据因为在运行中会产生易位调整
for i in range(10):
    a=input()
    x_data.append(a)

result=[]
#偶数条件下的作为结果的输出变量
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

print(x_data)
print('目标结果\n',result)
#找出偶数
#后言:
#作为认识卷积概念的一次代码,没有打算展开只是上传记录一下,也有待进一步整理.
