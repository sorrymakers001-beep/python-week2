import numpy as np
arr = np.array([11,22,33.33])
arr[1] = 66.66 #以0开始为第一个数
arr1 = arr.astype(int)  #astype更改array数据类型
print(arr1)
print(arr.ndim)  #xx+.ndim---检验array维度
arr2 = 66.6*np.ones((2,2,2)) #ds:ones的作用：创建一个指定形状、指定数据类型、所有元素都为 1 的新数组
                        #后面可跟dtype = int/float/str 指定数据类型
                        #数x*全1矩阵得全x矩阵
arr2[1,0,1] = 33.3                        
print(arr2[[1,0,0],[0,0,1],[1,1,1]]) #每个【】代表一种类型：纵，列...
print(arr2.shape) #.shape 为方法，会返回arr的形状
arr3 = np.arange(10,20,2) #20前结束
print(arr3)
arr4 = (100-44)* np.random.random(3)+3.14
arr4_ud = np.flipud(arr4)
arr5 = np.random.randint(10,66,(4,5))
arr5_ud = np.flipud(arr5) #flipud上下翻转
arr5_lr = np.fliplr(arr5) #fliplr左右翻转
arr6 = np.random.normal(1,2,(2,2)) #normal:正态分布函数，第一个数：均值，第二个数：标准差
print(arr4,arr4_ud,arr5,arr5_ud,arr5_lr,arr6,arr[2])
arr7 = 8.8*np.ones(5)
print(arr7[1:4],arr7[1:-1]) #向量切片
arr8 = np.arange(0,60,3).reshape(4,5)
print(arr8[2:-1,2:-2]) #矩阵切片
arr_add1 = np.concatenate([arr1,arr7]) #concatenate--拼接向量个矩阵
arr_add2 = np.concatenate([arr5,arr8],axis=1) #默认axis=0--以行拼接，axis=1以列拼接
print(arr_add1,arr_add2)
# # 均值函数np.mean(), 标准差函数np.std()
# # 求和函数np.sum(), 求积函数np.prod()
arr9 = np.arange(1,101)
arr9[arr9%2 == 0] = 0
print(arr9)
arr10 = np.arange(46,66).reshape(4,5)
print(arr10.sum(),arr10.sum(axis=1))
print(arr10.mean(),arr10.mean(axis=0))
arr10[arr5 > arr10] = 0
arr5[np.any(arr5 > arr10)] = 0
print(arr10,arr5)