# python 使用open()函数来打开文件使用read()函数来读取文件
obj_file = open('test/test.txt', encoding="utf-8")  # 打开文件获取对象
txt = obj_file.read()  # 读取文件
print(txt)
obj_file.close()  # 关闭文件

# with 关键字适用于获取文件对象进行系列操作
with open('test/test.txt', encoding="utf-8") as fs:
    txt1 = fs.read()
    print(txt1)
    fs.close()

# 逐行读取文件
with open('test/test.txt', encoding="utf-8") as fs:
    i = 0
    for line in fs:

        if i == 1:
            print(line.rsplit())  # 将读取到的字符，以空格分割字符串，存放在列表中
        i += 1
    fs.close()

with open('test/test.txt', encoding="utf-8") as fs:
    txt = fs.readlines()  # 逐行读取文件内容依次存入列表中且保留换行符
    fs.close()
print(txt)

# 写入内容至文件
with open('test/test.txt', encoding="utf-8", mode='a') as fs:  # 更改文件的权限 mode=w为覆盖写入，a为添加写入
    fs.write("\nssssss")  # 写入的文本必须是字符串可以使用换行符
    fs.close()
