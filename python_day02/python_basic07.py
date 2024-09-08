"""
===============***===============
Auther : Lee
Date   : 2022-11-01 - 18:26
File   : python_basic07.py
===============***===============
"""

"""
本章讲解：字符串
"""

# 1.字符串的声明，定义
name = 'xiaohua'  # 字符串有两种声明方式，单个引号和3个引号，又因为python单双引号不做区分衍生出两种
name = "xiaoliu"
name = '''xiaochen'''
name = """xiaohei"""

# 2.字符串可以用 + 号拼接， *号重复，结果还是一个字符串
str1 = '今天'
str2 = '天气'
str3 = '很好'

str4 = str1 + str2 + str3
print(str4)  # 今天天气很好
print(type(str4))  # <class 'str'>
print(str4 * 5)  # 今天天气很好今天天气很好今天天气很好今天天气很好今天天气很好

age = 18
# print(age+str4)  #字符串和整数不可以拼接, TypeError: unsupported operand type(s) for +:'int'and 'str'

# 3.字符串的索引 字符串对每个字符都做了编号,从左往右是从0开始,从右往左是从-1开始
str5 = '今天天气很好,快去见你想见的人吧'

print(str5[4])  # 很
print(str5[8])  # 去
print(str5[-1])  # 吧
print(str5[-7])  # 见
# print(str5[16])    # IndexError: string index out of range 下标越界异常

# 4.字符串的切片(截取):语法str5[开始下标:结束下标] 前包含,后不包含
str5 = '今天天气很好，快去见你想见的人吧'

print(str5[0:2])  # 今天
print(str5[3:9])  # 气很好，快去
print(str5[10:5])  # 没有信息
print(str5[0:-1])  # 今天天气很好，快去见你想见的人
print(str5[0:-5])  # 今天天气很好，快去见你
print(str5[8:-8])  # 没有信息
print(str5[5:])  # 好，快去见你想见的人吧
print(str5[:-1])  # 今天天气很好，快去见你想见的人
print(str5[:])  # 今天天气很好，快去见你想见的人吧
print(str5[-8:-1])  # 去见你想见的人

# 第三个参数，步长 每隔几个取一个
print(str5[::2])  # 今天很，去你见人
print(str5[3:9:2])  # 气好快
print(str5[::-1])  # 吧人的见想你见去快，好很气天天今
# 5.填充
# 1.format()
str6 = "小花{}，年龄{}，{}年来上海工作"
str7 = str6.format("河南", 20, 2022)
print(str7)  # 小花河南，年龄20，2022年来上海工作

str6 = '小花来自{0}，年龄{1}，{1}年来上海工作'
str7 = str6.format('河南', 20)
print(str7)  # 小花来自河南，年龄20，20年来上海工作

str6 = '小花来自{a}, 年龄{b}, {b}年来上海工作'
str7 = str6.format(a='河南', b=20)
print(str7)  # 小花来自河南, 年龄20, 20年来上海工作

# 2.传统填充方式  %s  代表需要填充字符串， %d 代表整数， %f 代表需要填充浮点数
str8 = '小花来自%s,年龄%d,%d年来上海，目前工资%fk'
str9 = str8 % ('安徽', 20, 2022, 15.5)
print(str9)  # 小花来自安徽，年龄20，2022年来自山海，目前工资15.500000k

# 3.直接填充变量
name1 = 'xiaohua'
print(f'{name1}很漂亮')  # xiaohua很漂亮

# 6.字符串的转义符:在python中\n代表换行,t代表制表符,相当于一个tab键,添加需要符号时需要以\加符号
str10 = '落霞与\\孤鹜齐\n飞，秋水共长天\t一色'
print(str10)  # 输出的结果包含斜杠和换行符，制表符

# 关闭转义：在字符串前加R或r  (raw)取消的意思
str10 = r'落霞与\\孤鹜齐\n飞，秋水共长天\t一色'
print(str10)  # 落霞与\\孤鹜齐\n飞，秋水共长天\t一色

# 注意：在写路径时很容易产生字符串转义的问题
path = r'D:\tools\WorkSpace\day01'

# endswith()函数判断文件后缀
file1 = "test.py"
file2 = "test.txt"
file3 = "test.java"
print(file1.endswith(".py"))  # 字符串后缀是否包含该字段结果返回布尔类型
print(file2.endswith("txt"))
print(file3.endswith(".py"))
