"""
===============***===============
Auther : Lee
Date   : 2022-11-10 - 18:55
File   : python_basic43.py
===============***===============
"""
"""
1.我们可以使用raise 自己触发异常
2.自定义异常：异常工作项目中，我们有时侯会需要定义一个区别于系统的异常类
"""

# 主动抛出异常
score = int(input('请输入0-100的分数'))

if not (0 <= score <= 100):
    raise Exception('输出了无效的分数')
elif 0 <= score < 60:
    print('不及格')
else:
    print('及格')


# 自定义异常
class InvalidScoreError(Exception):  # 所有异常都必须继承Exception类
    pass


score = int(input('请输入0-100的分数'))

if not (0 <= score <= 100):
    raise InvalidScoreError('输入无效的分数')
elif 0 <= score < 60:
    print('不及格')
else:
    print('及格')

num = input('请输入一个数字')
if int(num) == 0:
    raise Exception('不能为0')   #raise提起异常，Exception为异常类型，异常类型不可自定义，括号中的异常原因可以自定义
else:
    print('haha')
