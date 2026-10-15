import pandas as pd
import numpy as np
dict_a = {'a':1,'b':2,'c':3}
sr = pd.Series(dict_a) # 注意S要大写
v = [666,None,999,000]
k = ['w','e','o','p']
sr1 = pd.Series(v,index = k)
print(sr,sr1,sr1.isnull())#xxx.isnull()发现缺失值
print(sr1.dropna()) # xxx.dropna()剔除缺失值
                    #  xxx.dropna(how='all')二维中剔除全为None的排
                    # xxx.fiina(x)填充None
v1 = [['苍穹','2000元'],['穿岳','2500元'],['长征','2500元']]
k1 = ['osprey','gregory','duter']
c = ['型号','价格']
df1 = pd.DataFrame(v1,index=k1,columns=c)
df1['国家'] = ['美国','美国','德国']
sr2 = df1['价格'] 
print(df1)
print(df1.iloc[0,1]) # 隐式索引
print(df1.loc['gregory','价格'],sr2) # 显式索引
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
print(df.head(),df.max(numeric_only=True),df.mean(numeric_only=True),df.std(numeric_only=True),df.sum(numeric_only=True))
print(df.describe())
age = pd.cut(df['Age'],[1,20,120])
print(df.pivot_table('Survived',index=age))