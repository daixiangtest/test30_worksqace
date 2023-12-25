"""
===============***===============
Auther : Lee
Date   : 2022-11-01 - 19:50
File   : python_basic09.py
===============***===============
"""
"""
字符串常用的api和方法
"""

# 1.len() 求字符串的长度（字符串中的元素个数） 返回int
str1 = 'xiaohua'
print(len(str1))  # 7

# 2.replace(a,b) 将字符串中的a替换成b
str2 = '我不喜欢打游戏'
str3 = str2.replace('不喜欢', '讨厌')
print(str3)  # 我讨厌打游戏

str2 = '我喜欢打游戏'
str3 = str2.replace('打游戏', '敲代码')
print(str3)  # 我喜欢敲代码

# 3.find(a) 返回a第一次出现的下标位置，没找到返回-1
str4 = 'abcdefgd'
print(str4.find('d'))  # 3

str5 = '我要去食堂吃饭'
print(str5.find('食堂'))  # 3
print(str5.find('酒店'))  # -1  （超出范围的显示-1）

# 4.join（） 连接，拼接
str6 = 'abc'.join('--')  # 把前面的字符串和后面的字符串中的每个成员拼接
print(str6)  # -abc-

str7 = ''.join('ABC')
print(str7)  # ABC

# 5.count() 统计元素在字符中出现的次数
str8 = '梓潼告诉老师梓潼被梓潼打了'
print(str8.count('梓'))  # 3
print(str8.count('梓潼'))  # 3

# 6.upper()/lower()  大小写转换
str9 = 'abcdefghDD123'
str10 = str9.lower()
print(str10)  # abcdefghdd123

str10 = str9.upper()
print(str10)  # ABCDEFGHDD123

# 7.isnumeric() 判断宇符串是否是纯数字, 如果是返回True, 反之返回False
print('123456'.isnumeric())  # True
print('12345a'.isnumeric())  # False

num = input('请输入一个整数')
if num.isnumeric():
    if int(num) % 2:  # 一个整数取余2只有两种结果,要么是奇数结果为1,也就是True,要么是偶数结果为,也就是False
        print('{}是奇数'.format(num))
    else:
        print('%s是偶数' % num)
else:
    print('请输入一个整数')

# 8.split() 按括号中的条件切割字符串，返回一个列表
list1 = '2022-11-02'.split('-')
print(list1)  # ['2022', '11', '02']

list1 = '17:36:12'.split(':')
print(list1)  # ['17', '36', '12']

list1 = 'abc ABC 123'.split()
print(list1)  # ['abc', 'ABC', '123']
