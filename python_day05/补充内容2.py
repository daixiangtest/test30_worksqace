# Alex落地
# hight = 100
# distance = 0  # 总和
#
# for i in range(10):
#     # 将下落高度加入到总和中
#     distance = distance + hight  # distance += hight
#     if i == 9:
#         break
#     # 计算反弹高度
#     hight /= 2  # hight = hight / 2
#     # 再将反弹高度加入到总和中
#     distance += hight
#
# print(f"共经历了{distance}米")

# num = 0
# # 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         num += 1
#         print(f"{j}*{i}={j * i}", end="\t")
#     print()
# print(num)

"""
年会抽奖
路飞科技有限公司有300员工，开年会抽奖，奖项如下
等奖 3名:泰国5日游+ 手术费报销
二等奖6名:iPhone14手机
三等奖30名:三斤苹果
规则:
1.共抽3次，第一次抽3等奖，第2次抽2等奖，第3次压轴抽1等奖2.每个员工限中奖一次，不能重复
解题思路:
1.生成一个员工列表，用random模块从里面取随机值2.取完值之后，立刻从员工大列表里把中奖人删掉，即可防止其再次中奖
"""
import random  # 随机数

staffList = []
for i in range(1, 301):
    staffList.append(f"员工{i}")  # 追加（末尾）

level = [30, 6, 3]

for i in range(3):
    winnerList = random.sample(staffList, level[i])

    for winner in winnerList:
        staffList.remove(winner)

    print(f"获得{3 - i}等奖的是：{winnerList}")
    print(f"还剩{len(staffList)}个人未中奖")

winnerList3 = random.sample(staffList, 30)
print(winnerList3)
#
# winnerList2 = random.sample(staffList, 6)
# print(winnerList2)
#
# winnerList1 = random.sample(staffList, 3)
# print(winnerList1)

"""
《炸金花》底层逻辑实现
自己写一个程序，实现发牌、比大小判断输赢。
游戏规则:
一付扑克牌，去掉大小王，每个玩家发3张牌，最后比大小，看谁赢.
有以下几种牌:
豹子:三张一样的牌，如3张6.如红桃5、6、7同花顺: 即3张同样花色的顺子顺子: 又称拖拉机，花色不同，但是顺子，如红桃5、方片6、黑桃7，组成的顺子对子:2张牌一样单张: 单张最大的是A这几种牌的大小顺序为， 豹子>同花顺>同花>顺子>对子>单张
需程序实现的点:
1.先生成一付完整的扑克牌2.给5个玩家随机发牌
3.统一开牌，比大小，输出赢家是谁
"""

def fun1(lis):
    lis.sort()
    a = int(lis[0])
    b = []
    for i in range(len(lis) - 1):
        a += 1
        if a == lis[i + 1]:
            a = lis[i + 1]
            b.append(True)
        else:
            b.append(False)
    return False not in b


list1 = [6, 10, 7]
a = fun1(list1)

str1 = "a1234"
print(str1[2:])

print(a)
list1 = ["红桃", "黑桃", "方片", "黑梅"]
list2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list3 = []

user = []
max1 = []
for i in list1:
    for j in list2:
        list3.append(i + str(j))
for i in range(5):
    lst1 = []
    lst2 = []
    list4 = random.sample(list3, 3)
    print(list4)
    for j in range(3):
        list3.remove(list4[j])
    for k in list4:
        lst1.append(k[0:2])
        lst2.append(int(k[2:]))
    lst2.sort()
    max1.append(lst2[-1:][0])
    if len(set(lst2)) == 1:
        user.append(1)
        print("豹子")
    elif len(set(lst1)) == 1 and fun1(lst2):
        print("同花顺")
        user.append(2)
    elif fun1(lst2):
        print("顺子")
        user.append(3)
    elif len(set(lst2)) == 2:
        print("对子")
        user.append(4)
    else:
        user.append(5)

print(user, max1)
u1 = ""
# user = [2, 2, 2, 3, 2]
# print(min(user))
# max1 = [3, 11, 13, 12, 11]
uu = []
for u in range(5):
    if user[u] == min(user):
        uu.append(u + 1)
if len(uu) == 1:
    u1 = f"玩家{uu[0]}牌最大"
else:
    listum = []
    for um in uu:
        listum.append(max1[um - 1])
    print(listum)
    for um in uu:
        if max1[um-1]==max(listum):
            u1 = f"玩家{um}牌最大"


print("*******" * 10)
print(u1)
