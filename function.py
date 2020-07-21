#函数调用报错
# 参数个数错误 TypeError: abs() takes exactly one argument (2 given)
# 参数类型错误 TypeError: bad operand type for abs(): 'str'

# 类型转换
int('123')
float('12.34')
str(100)
bool(1)
# 更改函数名
a = abs
print(a(-1))
# define function, pass占位
def nop():
    pass
# 参数检查
def my_abs(x):
    if not isinstance(x, (int, float)): #内置数据类型检查
        raise TypeError('bad operand type') 
    if x >= 0:
        return x
    else:
        return -x
# 返回多个值，实际是返回tuple
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
r = move(100, 100, 60, math.pi / 6)
print(r)
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
power(5)
power(5, 3)

def add_end(L=[]): # 定义默认参数要牢记一点：默认参数必须指向不变对象，这是一个错误范例
    L.append('END')
    return L
print(add_end())
print(add_end()) #每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了
# list 或 tuple传参
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print( calc([1,2,3]) )
print( calc((1,2,3,4)) )
#可变参数: 传入参数个数是可变的，调用后自动组成为tuple
def calcc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calcc(1,2,3))
nums = [1, 2, 3]
print(calcc( *nums ))
numss = (1, 2, 3 ,4)
print(calcc( *numss ))

# 关键字参数：**kw, 传入0个或任意个含参数名的参数，函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'} #组装dict传入
person('Jack', 24, **extra)

# 命名关键字参数：限制关键字参数的名字，命名关键字参数必须传入参数名
def person1(name, age, *, city, job):
    print(name, age, city, job)
person1('Jack', 24, city='Beijing', job='Engineer')

def person2(name, age, *args, city, job): #有可变参数的格式
    print(name, age, args, city, job)

def person3(name, age, *, city='Beijing', job): #关键字参数可以缺省
    print(name, age, city, job)

def product(*nums):
    if len(nums) == 0:
        raise TypeError('at least one word')
    else:
        res = 1
        for n in nums:
            if not isinstance(n, (int, float)): #内置数据类型检查
                raise TypeError('bad operand type') 
            
            else:
                res = res * n
        return res

# 递归 ：汉诺塔
def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b )
        print(a, '-->', c)
        move(n-1, b, a, c)
    return
    


