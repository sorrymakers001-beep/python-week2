import numpy as np
arr1 = np.arange(1,10).reshape(3,3)
arr2 = np.arange(21,30).reshape(3,3)
result = arr1@arr2
print("arr1@arr2=\n",result) #\n表示换行
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
sam = np.random.choice([0,1],size=8000,p=[0.5,0.5])
add = sam.sum()
frequency =add/8000
print(add,frequency)
plt.figure(figsize=(8,6))
plt.hist(sam,bins=2,rwidth=0.8,edgecolor='#19C7E6')
plt.title('概率分布图')
plt.xticks([0,1],['反','正']) #xlabel 管“轴的含义”，xticks 管“轴上的刻度”
plt.show()
