"""
===============***===============
Auther : Lee
Date   : 2022-11-13 - 15:07
File   : expression.py
===============***===============
"""
# 列表推导式
# 生成1-100的奇数整数队列
list1 = []
for i in range(1, 101, 2):
    list1.append(i)
print(list1)

print([x for x in range(1, 101, 2)])  # 把符合后面的for循环条件的x的值新增到一个表中

list1 = []
for i in range(1, 101):
    if i % 2 == 1:
        list1.append(i)
print(list1)
print([i for i in range(1, 101) if i % 2 == 1])
print([str(i) for i in range(1, 101)])  # 把列表转化为字符串格式

# 元组推导式
print(tuple(x for x in range(1, 101, 2)))  # 把符合后面for循环条件的x的值新增到一个元组中

# 字典推导式
list1 = ['小花', '小美', '小刘']
print({x: len(x) for x in list1 if '刘' not in x})  # {'小花': 2, '小美': 2}


# 装饰器：一般是一个闭包函数，外层函数返回内部嵌套函数，在不影响原函数功能的前提下，实现被装饰函数额外的功能
def security(fun):
    def do_something():
        print("开始检测环境是否安全")
        fun()
        print('环境执行完毕，开始清理')

    return do_something


@security
def fun():
    print('转账业业务')


fun()

# 递归: 方法内部自己调用自己
# 递归注意: 好处就是极大的减少了冗余代码,逻辑干练。 当然递归必须要有明确的终止条件,也不要递归太深容易栈溢出
