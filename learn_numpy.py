#array basic
import numpy as np 
my_array = np.array([1, 2, 3, 4, 5]) 
print(my_array)
print(my_array.shape)
print(my_array[0])

my_new_array = np.zeros((5)) 
print(my_new_array)
my_2d_array = np.ones((2, 4))
print(my_2d_array)

my_array = np.array([[4, 5], [6, 1]])
print(my_array[0][1]) 
print(my_array.shape) 
my_array_column_2 = my_array[:, 1] 
print(my_array_column_2) # 取出一行或一列，输出是array

a = np.array([[1.0, 2.0], [3.0, 4.0]]) 
b = np.array([[5.0, 6.0], [7.0, 8.0]]) 
sum = a + b 
difference = a - b 
product = a * b #逐元素相乘
quotient = a / b 
matrix_product = a.dot(b) #矩阵乘法
v = np.transpose(np.array([[2,1,3]])) #矩阵转置
print(v)
vv = np.array([[2,1,3]]).T #转置的另外一种表示方法
print(vv)
vvv = np.array([2,1,3]).T #一维array无法转置
print(vvv)

#array运算一些特点
print('calculate')
a = np.array([[1, 1],[1, 1]]) #二维数组和一维数组矩阵乘法得到 [4 4]
e = np.array([1, 3]) 
res = a.dot(e)
print(res)
f = np.array([[0.6, 1]]) #二维数组和一维数组矩阵乘法得到 [5]
g = np.array([5, 2])
ress = f.dot(g)         # f.T.dot(g)会报错
print(ress)
h = np.array([1,2])
resss = g.dot(h)
print(resss) #两个一维数组矩阵乘法得到 9， 不同维度一维数组不能相乘
j = np.array([2])
print(1-j) #会自动转化为 [-1]
print(f.T.dot(j)) #得到 [1.2 2]


#矩阵/数组/列表转换
print('from list')
a = [1,2,3] #列表——数组，矩阵
b = np.array(a)
print(b)
c = np.mat(a)
print(c)

print('to list')
new_a1 = c.tolist()
print(new_a1) # 矩阵转化的列表是嵌套的
new_a2 = b.tolist()
print(new_a2) # 转化为了一维列表

print('array and matrix')
array2matrix = np.mat(b) #数组转化为矩阵
print(array2matrix)
matrix2array = np.array(c) #矩阵转化为数组
print(matrix2array)

# 从矩阵或数组中取出一行或一列
print('col or row')
my_array1 = np.array([[4, 5], [6, 1]])
my_array2 = np.mat([[4, 5], [6, 1]])
col_1 = my_array1[0,:] #一维的ndarray
col_2 = my_array2[0,:] #矩阵
print(col_1)
print(col_2)
#行数组赋值给二维数组的列
plus = np.array([-1, -1])
my_array1[:,0] = plus
print(my_array1)



