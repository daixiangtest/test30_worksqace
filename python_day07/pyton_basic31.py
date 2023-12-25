"""
===============***===============
Auther : Lee
Date   : 2022-11-08 - 17:17
File   : pyton_basic31.py
===============***===============
"""
"""
内置函数：python自带的函数
"""
# 常用的内置函数：print()/input()/id()/type().....
# 高级内置函数：eval() exec() lambda filter() map() zip() enumerate().......

# eval()和exec（）：能够识别字符串中的python表达式
print('1+1')  # 1+1
print(eval("1+1"))  # 2 eval()将字符串中的python表达式识别未1+1并且计算
eval('print("hello")')  # hello

# 案列1
num1 = input('请输入一个整数：')
num2 = input('请输入第二个整数')
print(eval(num1) + eval(num2))  # 识别了字符串中的数字
# 案列2
# 求出如下字符串中的元素的和 "[1,2,3,4,100,5,6,7,8,9]"
str1 = "[1,2,3,4,100,5,6,7,8,9]"
print(sum(eval(str1)))  # 145
# 打印如下字符串中的case_id对应的值'{'name':'xiaohua','age':18,'case_id':1101}'
print(eval("{'name':'xiaohua','age':18,'case_id':1101}")['case_id'])  # 1101

# 有返回值时使用eval(),有def class 等关键字时使用exec（）
str1 = ""


def fun1():
    print('hello whord')


""
exec(str1)
fun1()  # hello word


# lambda 写结构简单的匿名函数
def fun1(num):
    return num % 2 == 0


print(fun1(15))  # false

fun2 = lambda x: x % 2 == 0  # 冒号前是参数，冒号后是逻辑
print(fun2(15))  # False  #返回的结果一般都是布尔类型

# filter():过滤，第一个参数传过滤规则，第二个参数就是要过滤的对象
# 把符合条件（结果为真）的数据过滤出来
tup1 = 1, 2, 3, 4, 5, 6, 7, 8, 9
tup2 = 5, 6, 8, 7, 4, 5, 6, 3, 6
print(tuple(filter(fun1, tup1)))  # (2,4,6,8)
print(list(filter(lambda x: x > 5, tup1)))  # [6,7,8,9]

# map():会根据提供的函数对指定序列做复制，把按条件筛选后的所以结果直接返回
tup1 = 1, 2, 3, 4, 5, 6, 7

print(tuple(map(lambda x: x % 2 == 0, tup1)))  # (False, True, False, True, False, True, False)
print(tuple(map(lambda x: x * x, tup1)))  # (1, 4, 9, 16, 25, 36, 49)

# enumerate()函数，列出数据和数据对应的下标
list1 = ['xiaohua', 'xiaomei', 'xiaohei']
print(tuple(enumerate(list1)))  # enmerate函数只有转化成元组才可以展示((0, 'xiaohua'), (1, 'xiaomei'), (2, 'xiaohei'))
for i, j in enumerate(list1):
    print(i, j)  # 0 xiaohua

# zip()函数：聚合打包，把多个序列打包到一个元组中返回，当长度不一致时，按最短长度的来
list1 = [1, 2, 3]
list2 = ['xiaphua', 'xiaomei', 'xiaohei']
list3 = ['a', 'b', 'c']

print(list(zip(list3, list2, list1)))  # [('a', 'xiaphua', 1), ('b', 'xiaomei', 2), ('c', 'xiaohei', 3)]
tup1 = ('name', 'age', 'sex')
tup2 = ('xiaohua', 18, '女')
print(dict(zip(tup1, tup2)))  # {'name': 'xiaohua', 'age': 18, 'sex': '女'}

# isinstance(A,B) 判断A变量的类型是否为B类型
num = 10
print(isinstance(num, int))  # True
print(isinstance(num, str))  # False
print(isinstance(tup1,tuple))  #True