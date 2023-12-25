"""
===============***===============
Auther : Lee
Date   : 2022-11-04 - 17:40
File   : python_basic18.py
===============***===============
"""

# 常见死循环：
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
    i+=1
print(i)

# break（终止整个循环）/continue（跳过本轮循环，继续下一轮循环）
#
# while 条件：
#    语句块1
# else ：
#     语句块2

# 当条件满足时，就一直执行语句块1，条件不满足执行语句块2

i = 1
while i <= 10:
    print(i)
    i += 1
else:  # 循环结束后，执行else的代码
    print('循环结束')

# break (终止整个循环)/continue（跳过本轮循环，继续下一轮循环）
i = 1
while i <= 10:
    i += 1
    if i == 7:
        # break  #终止整个循环
        continue  # 跳过本轮循环，继续下一轮循环
    print(i)

# 死循环
# while True:
#   print('马上要放假了，晚上通宵追剧')

# 写一个程序，猜书名（活着），猜中停止循环，猜不中就一直猜
while True:
    book = input('请输入书名')
    if book == '活着':
        print('恭喜您猜对了')
        break
    else:
        print('猜错了，请重新猜')

# 模拟用户登录
count = 0
while True:
    name = input('请输入用户名')
    pwd = input('请输入密码')
    count += 1

    if name == 'scott' and pwd == '1234':
        print('欢迎回家')
        break
    if count < 3:
        print('用户名或密码错误还有{}次机会'.format(3 - count))
        continue
    if count == 3:
        print('您输入的错误数过多，请稍后重试')
        break
