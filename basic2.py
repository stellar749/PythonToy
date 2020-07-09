## list列表
'''
classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))
print(classmates[0]) #索引是从0开始的
print(classmates[-1])
classmates.append('Adam')
classmates.insert(1, 'Jack')
print(classmates)
classmates.pop()
classmates.pop(1)
classmates[1] = 'Sarah'
print(classmates)
s = ['python', 'java', ['asp', 'php'], 'scheme'] #list元素类型可以不同
print(s[2][1]) #可以看成二维数组
L = []
print(len(L)) #空list


#tuple 元组,一旦初始化就不能修改,能用tuple代替list就尽量用tuple
t = (1, 2)
print(t)
print(t[0]) 
t = ()
print(t)
t = (1,) #要加, 输出也会加,
print(t)
t = ('a', 'b', ['A', 'B']) #元素是List的时候list元素可修改，但t[0] = 3会报错
t[2][0] = 'X'
print(t)

# 条件和循环
age = 20
if age >= 6: #按顺序执行，只选取一个分支
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
x = 3
if x:
    print('True')

s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

## 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print('Hello,%s!' % name)

print(range(5))
print(list(range(5)))
sum = 0
for x in range(101): #生成0-100序列
    sum = sum + x
print(sum)

t = (1,2,3) #tuple也可以起到循环的作用
for i in t:
    print(i)

sum = 0 #while循环
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
# break结束循环，continue跳过当前的这次循环都可用
'''
# dict 字典（map）

