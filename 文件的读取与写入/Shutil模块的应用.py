import shutil

"""
shutil提供了一些方法可以对文件进行复制，删除，移动，重命名等操纵
"""

# 复制文件
# shutil.copy("文件读取.py", 'test')  # 将文件读取.py这个文件复制粘贴到test目录里面
# shutil.copy("文件读取.py", 'test.py')  # 将文件复制在当前目录，重命名为test.py保存下来

# 复制文件目录及里面的文件
# shutil.copytree('test', "test01")  # 把当前目录下的test目前复制粘贴为test01

# 文件移动
# shutil.move('test01', "test")  # 当前目录移动到当前目录为重命名操作
# shutil.move('test01', '../')  # 移动文件

# 文件删除（与os.rmdir()不一样的是删除目录时会递归删除目录里面的子文件）
shutil.rmtree('../test01')
