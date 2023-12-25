"""
===============***===============
Auther : Lee
Date   : 2022-11-07 - 19:44
File   : 猜大小.py
===============***===============
"""
import random

money = 0
yue = 0
get1 = 10
get2 = 20
while True:
    while True:
        money = input('请输入需要充值的金额')
        if money.isnumeric():
            print('充值成功您的金额还有:', int(money) + int(yue))
            yue = int(money) + int(yue)
            begin = input('是否开始押注')
            if begin == '是':
                get = get2
                break
            if begin == '结束':
                print('欢迎再来')
            get = get1
            if get == 10:
                break
            else:
                print('您的输入有误请重新输入')
                continue
    if get == 10:
        break
    while True:
        mon1 = input('请数入需要押注的金额')
        if int(mon1) > yue:
            print('您的余额不足')
            break
        else:
            a = input('请输入大或者小')
            b = ['大', '小']
            print(random.choice(b))
        if random.choice(b) == a:
            yue = int(yue) + int(mon1)
            print('恭喜您猜对了您的余额还有:', yue)
            go_on = input('是否继续或结束')
            if go_on == '是':
                continue
            if go_on == '否':
                break
        else:
            yue = int(yue) - int(mon1)
            print('哎呀猜错了您的余额还有:', yue)
            go_on = input('是否继续或结束')
            if go_on == '是':
                if yue <= 0:
                    print('您的余额不足,请充值')
                    break
                continue
            if go_on == '否':
                break
    over = input('确定结束吗,请输入是或者否')
    if over == '是':
        break
    if over == '否':
        continue
    else:
        print("您的输入有误")
        break
