"""
===============***===============
Auther : Lee
Date   : 2022-11-01 - 13:51
File   : python_basic06.py
===============***===============
"""
"""
本章讲解：运算符
"""

# 知识点1：运算符  =  -  *  /  %（取余）   //（向下取整）   **（幂等）
print(10 + 20)  # 30
print(20 - 10)  # 10
print(10 * 20)  # 200
print(20 / 10)  # 2.0  除法总是会返回一个浮点数

# 取余
print(9 % 2)  # 1  返回的是9除以2的余数
print(10 % 20)  # 10
print(233 % 133)  # 100
print(55 % 20)  # 15
print(9876 % 45678)  # 9876
print(6 % 3)  # 0
print(164540 % 2)  # 0
# 小数对大数取余，直接余小的
# 所有奇数对2取余直接余1，也就是true，所有偶数对2取余直接余0，也就是false

# 向下取整
print(10 // 3)  # 3   返回的是10除以3的整数部分
print(14 // 3)  # 4
print(25 // 2)  # 12
print(-25 // 2)  # -13
# 幂等
print(2 ** 3)  # 8  2的3次方，2*2*2的结果
print(2 ** 5)  # 32
print(3 ** 6)  # 729

# 知识点2：赋值运算符  =  +=  -=  /=  %=  //=
a = 10
a += 1  # 相当于a=a+1的简写形式
print(a)  # 11

a -= 1  # 相当于a=a-1
print(a)  # 10

a *= 2  # 相当于a=a*2
print(a)  # 20

a /= 2  # 相当于a=a/2
print(a)  # 10.0

a ** 2  # 相当于a=a*a
print(a)  # 100.0

a //= 3  # 相当于a=a//3
print(a)  # 33.0

# 知识点3： 比较运算符 >  <   >=   <=   != (不等于)     ==（等于）   结果总是会返回布尔类型 true或者flase
a = 20
b = 10

print(a == b)  # False
print(a > b)  # True
print(a < b)  # False
print(a != b)  # True

# 知识点4：逻辑预算符  and(全真为真)   or(全假为假)    not(取反)
print(a > 0 and b > 0)  # True
print(a > 0 and b < 0)  # False
print(a < 0 or b < 0)  # False
print(a < 0 or (b > 0 and a < 0))  # False
print(not a > b)  # False

# 知识点5：成员运算符 in （在指定的数据中查找出指定内容）  如果找到了返回true, 反之返回false
#  not in (在指定的数据中查找指定内容)   如果找到了返回false,反之返回true
str1 = 'xiaohua'
print('x' in str1)  # True
print('a' in str1)  # True
print('a' not in str1)  # False
