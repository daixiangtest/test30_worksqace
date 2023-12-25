"""
===============***===============
Auther : dai xiang
Date   : 2022/10/31 - 12:01
File   : python_basic02.py
===============***===============
"""

# 1变量

print("天苍苍，野茫茫")  # print的作用是打印了括号中的内容
a = "30班"  # 新建了一个变量a，并且赋值了后面的字符串
print(a)  # 打印了给a赋的值
b = 1  # b是整数类型，值是1，变量的类型由值来决定
c = "1"  # c是字符串类型
d = 1.0  # d是浮点数

# ctrl+alt+l          自动调整格式

#  2.变量的声明
a = 1  # 声明了一个变量a，并且赋值1 变量a是整数类型
b = 2  # 声明了一个变量b,并且赋值2 变量b是整数类型
print(a + b)  # 3
c = 3.5  # 声明了一个变量c,并且赋值3.5，变量c是浮点类型
print(c + a)  # 4.5

#  3.声明字符串的几种方式
name = 'xiaohua'  # 字符串有两种声明方式，单个引号和3个引号，又因为python单双引号不做区分衍生出两种
name = "xiaoliu"
name = '''xiaochen'''
name = """xiaohei"""

# 4.变量的覆盖      变量可以一次声明，多次赋值，后面的值会覆盖前面的值
sal = 15000
print(sal)  # 15000
sal = 18000
print(sal)  # 18000
sal = sal + 1000
print(sal)  # 19000
name = "xiaomei"
print(name)  # xiaomei

# 5.同时为多个变量赋值
a, b, c = 1, 2, 3  # 同时为多个变量赋值不同的值 声明了a,b,c分别赋值1，2，3
print(a, b, c)  # 1 2 3

a = b = c = 1  # 同时为多个变量赋值相同的值，声明了a,b,c三个变量并且都赋值1
print(a, b, c)  # 1 1 1

#  6.python是一门大小写和缩进敏感的编程语言，python使用缩进表示层级之间的包含关系
A = 1
a = 2
print(A)  # 1
print(a)  # 2

Name = "xiaolan"
name = "xiaoli"
print(Name)  # xiaolan
print(name)  # xiaoli

print("30班")
#   print("30班")  #indentation error：unexpected indent缩进错误
