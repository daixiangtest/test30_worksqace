"""
===============***===============
Auther : dai_xiang
Date   : 2022/10/31 - 18:37
File   : python_basic04.py
===============***===============
"""

"""
本章讲解：数字类型，布尔类型，字符串类型
"""

# 1.数字类型分为，整数int  浮点数float
a = 10
b = 10 / 2  # python 里面除法总是会返回一个浮点数，哪怕可以整除
print(b)  # 5.0
c = 10 / 3

# type() 用来查看括号中数据的类型
print(type(a), a)  # <class 'int'> 10
print(type(b), b)  # <class 'float'> 5.0
print(type(c), c)  # <class 'float'> 3.3333333333333335

# 2.布尔类型  只有2个值，true(真，成立)  false(假，不成立)
bo1 = 10 > 3
print(type(bo1), bo1)  # <class 'bool'> True
bo2 = 10 < 3
print(type(bo2), bo2)  # <class 'bool'> False
bo3 = 5 <= 5
print(type(bo3), bo3)  # <class 'bool'> True

# 3.字符串类型   用来保存一串字符  str
str1 = 'xiaomei'
str2 = "xiaohua"
str3 = '''xiaoshuai'''
str4 = """xiaoliu"""
print(type(str1), str1)  # <class 'str'> xiaomei

# 字符串一些注意事项
#  单引号和双引号是不区分的，但是要注意配合使用
print("孙宁宁是一个很‘优秀’的测试工程师")  # 孙宁宁是一个很‘优秀’的测试工程师
print("my name's 刘德华")  # my name's 刘德华

#  类型之间的强制转换,语法：类型（要转换的对象）
#  数字/字符串之间的转换
num = 10
print(type(num), num)  # <class 'int'> 10
str1 = str(num)
print(type(str1), str1)  # <class 'str'> 10

str1 = '20'
num1 = int(str1)
print(type(num1), num1)  # <class 'int'> 20
#  str2='20a'
#  mum2=int(str2)   # 注意只有字符串是纯数字才可以转换整数

num1 = 5.5
str1 = str(num1)
print(type(str1), str1)  # <class 'str'> 5.5

str1 = '5.5'
num1 = float(str1)
print(type(num1), num1)  # <class 'float'> 5.5

# 数字类型的转换
float1 = 9.9
num1 = int(float1)
print(type(num1), num1)  # <class 'int'> 9

int1 = 10
num1 = float(int1)
print(type(num1), num1)  # <class 'float'> 10.0

# 其他类型转布尔类型  非空即真，非0即真   大类型转小类型可能会造成进度丢失
num = 10
bo1 = bool(num1)
print(type(bo1), bo1)  # <class 'bool'> True

num1 = 0
bo1 = bool(num1)
print(type(bo1), bo1)  # <class 'bool'> False

num1 = 5.5
bo1 = bool(num1)
print(type(bo1), bo1)  # <class 'bool'> True

num1 = 0.0
bo1 = bool(num1)
print(type(bo1), bo1)  # <class 'bool'> False

str1 = ''
bo1 = bool(str1)
print(type(bo1), bo1)  # <class 'bool'> False

#  布尔类型转其他类型
num1 = int(True)
print(type(num1), num1)  # <class 'int'> 1
num1 = int(False)
print(type(num1), num1)  # <class 'int'> 0

# 布尔类型也属于字符类型的一种所以再转换的时候true为1 false为0
