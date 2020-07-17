## list列表 , 可变对象。a.sort()以后顺序会变

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
t = (1,) #单一元素的元组要加, 输出也会加,
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
print(list(range(5))) #0 1 2 3 4
sum = 0
for x in range(101): #生成0-100序列
    sum = sum + x
print(sum) #5050

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

# dict 字典（map）,dict根据key来计算value的存储位置(hash), 字符串、整数可作为key，list不能作为key
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])  #疑问：如何快速查找key
d['Adam'] = 67 #可以直接赋值，后赋值会覆盖前赋值
print('Thomas' in d ) #返回false
print(d.get('Thomas')) #返回None
print(d.get('Thomas',-1)) #返回-1
d.pop('Bob') #删除key
print(d) 

# set 集合, 无顺序，不重复
s = set([1, 2, 3]) # 要创建一个set，需要提供一个list作为输入集合
print(s) # {1, 2, 3}
s.add(4) # add
s.remove(3) #remove
print(s)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2) #and 
print( s1 | s2) #or

#不可变对象(比如str),调用对象自身的任意方法，也不会改变该对象自身的内容
a = 'abc'
print(a.replace('a', 'A')) #Abc
print(a) #abc
l = ['c', 'b', 'a'] #list 是可变对象
l.sort()
print(l) #['a', 'b', 'c']