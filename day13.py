import matplotlib.pyplot as plt
import pandas as pd
Fig1 = plt.figure()
x = [1,2,3,4]
y1 = [1,7,13,1000]
y2 = [1,1,1,1]
y3 = [1000,99,66,11]
plt.subplot(3,1,1),plt.plot(x,y1,color = '#E63919',linestyle = ':') # plt.subplot()绘制子图
plt.subplot(3,1,2),plt.plot(x,y2,color = '#9E19E6',linestyle = '-.') # 引入颜色
plt.subplot(3,1,3),plt.plot(x,y3,color = '#19C7E6',linestyle = '--')
plt.bar(x,y1)
plt.show() # plt.show()用以弹出图像
# 保存图像的方式：Fig1.savefig(r'C:\Users\hp\Desktop\xxx.svg')
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
age = df['Age'].dropna()
print(df.head())
plt.figure(figsize=(10, 6)) 
#figsize 是 figure size 的缩写，用来控制 整张图（画布）的大小，单位是 英寸（inch）
plt.hist(age,bins=25,color = '#19C7E6',edgecolor = '#FFFFFF')
# bins：分箱数量或边界，rwidth：柱子的相对宽度
plt.title('年龄分布',fontsize=20)
# fontsize：字体大小
plt.xlabel('age',fontsize=15)
plt.ylabel('number',fontsize=15)
plt.grid(True)
plt.show()
# 1. 用 Pandas 分组聚合算出生存率
survival_rates = df.groupby('Sex')['Survived'].mean()

# 2. 画柱状图
plt.figure(figsize=(8, 5))
plt.bar(survival_rates.index, survival_rates.values, color=['pink', 'lightblue'])
# 或者用 Pandas 自带的一行代码：
# survival_rates.plot(kind='bar', color=['pink', 'lightblue'], figsize=(8, 5))

# 3. 加标题和标签
plt.title('不同性别的生存率对比', fontsize=16)
plt.xlabel('性别', fontsize=12)
plt.ylabel('生存率', fontsize=12)
plt.ylim(0, 1)
plt.show()