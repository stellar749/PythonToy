#基本IO
print("hhh")
print('hhh')
print(5+3)
name=input('please input your name: ') #input()返回的数据类型是str
print('my name is',name) 

##数据类型和变量
print(0xff00) #十六进制
print(1e2) #科学计数法是浮点数
print('I\'m learning\nPython.') #也有转义字符，'要转义\'
print(r'\\\t\\') #r''内部默认不转义
print('''line1
line2
line3''') #多行输入，···是多行提示符
print(3 > 2) #bool
print(True and False) # and or not
# python 的空值为None
t = 'aaa' #字符串赋值
print(t)
t = 32 #python是动态语言，不需要固定变量类型
print(10 / 3) #整数运算是精确的，包括除法，但是结果变成了浮点数，浮点数运算是不精确的
print(10 // 3)
print(10 % 3) 
# python 对整数和浮点数的大小都没有限制


##字符串与编码
# Unicode标准:2个字节一个字符，可变长编码：UTF-8编码,英文1字节，中文3字节
print(ord('中')) #ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(chr(25991))
# Python的字符串类型是str，在内存中以Unicode表示，如果要在网络上传输或者保存到磁盘上，需要把str变为以字节为单位的bytes，bytes的每个字符都只占用一个字节
print('ABC'.encode('ascii')) #bytes类型的数据为带b前缀的单引号或双引号,encode需要指定编码，最常用utf-8
print('中文'.encode('utf-8')) #在bytes中，无法显示为ASCII字符的字节，用\x##显示，含有中文的str无法用ASCII编码
print(b'ABC'.decode('ascii')) #读取了字节流，要把bytes变为str
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')) #忽略无效字符
# 以上输出中文的时候会乱码，在terminal中就不会
print(len('中文ABC')) #len计算str的字符数2+3=5
print(len(b'ABC\xe4\xb8\xad\xe6\x96\x87')) #计算bytes的字节数 3*1+2*3=9
# 以下两行为了让解释器按UTF-8编码读取，本来就是注释形式
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('%2d-%02d' % (3, 1)) #%2d 空一格，%02d 补0
print('%.2f' % 3.1415926) #%s表示用字符串替换，%d表示用整数替换，%f浮点数，%x十六进制
print('Age: %s. Gender: %s' % (25, True)) #任何类型都能转换成字符串
