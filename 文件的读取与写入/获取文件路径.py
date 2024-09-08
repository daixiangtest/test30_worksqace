import glob
import os

path1 = os.getcwd()  # 获取当前的文件路径所在的文件夹
print(path1)

path2 = os.path.abspath('.')  # 获取当前文件目录的绝对路径
print(path2)

path3 = os.path.relpath(r'C:\Users', '获取文件路径.py')  # 列举出两个文件的相对文件路径
print(path3)

b1 = os.path.exists(r'获取文件路径.py')  # 判断文件或者文件夹是否存在
print(b1)
b2 = os.path.isabs(r'C:\Users\HUAWEI\Desktop\test30_worksqace\文件的读取与写入')  # 判断是否为绝对路径
print(b2)
b3 = os.path.isdir(r'C:\Users\HUAWEI\Desktop\test30_worksqace\文件的读取与写入')  # 判断是否是文件夹
print(b3)
b4 = os.path.isfile('获取文件路径.py')
print(b4)

# os.mkdir('test')  # 创建文件夹
# os.rmdir('test')  # 删除文件夹只能是空目录
# os.remove(r'test/test.py')  # 通过路径删除文件夹中的文件
# os.chdir(r'C:\Users\HUAWEI\Desktop')  # 移动当前文件夹中到指定的路径

size = os.path.getsize('获取文件路径.py')  # 获取文件的大小
print(size)
file_list = os.listdir(r'C:\Users\HUAWEI\Desktop\test30_worksqace\python_day19')  # 获取当前文件夹下面的文件目录
print(file_list)

# glob获取同样是获取文件路径，但是需要通配符 * 来做文件筛选且返回的是文件路径而非文件名
file_list2 = glob.glob(r'C:\Users\HUAWEI\Desktop\test30_worksqace\python_day19\*.py')
print(file_list2)

print("******" * 10)
# 对文件目录进行遍历，分别返回当前的文件目录，当前目录下的文件夹，当前目录下的文件
for dirname, sub_dirname, file_name in os.walk(r'C:\Users\HUAWEI\Desktop\test30_worksqace\python_day19'):
    print(dirname)
    print(sub_dirname)
    print(file_name)
