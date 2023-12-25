"""
===============***===============
Auther : Lee
Date   : 2022-11-22 - 14:02
File   : python_yaml02.py
===============***===============
"""
import yaml

"""
python操作yaml文件

1.yaml是一个可读性高,用来表达数据序列化的格式的配置文件,用python操作yaml文件,后缀可以是.yml或者.yaml
2.pip install pyyaml
3.yaml支持数据结构:
    对象: 键值对的集合,python中字典
    数组: 按次序排列的值,python中列表
    纯量: 单个的、不可在分割的值,python中的数字、布尔类型、None、字符串等等
4.yaml配置文件的语法规则
    1.大小写敏感
    2.使用缩进表示层级关系,缩进只允许使用空格,不允许使用tab键
    3.缩进的空格不重要,只要相同层级的元素左侧对齐即可(一般是2个空格或4个空格)
    4.#号表示注释
"""

# 2.数组：使用一个短横线-  加一个空格就代表一个数组项
data=['刘备','张飞','荀彧','窦路遇','汪圣文',['杨倍斯','白敬亭','焦恩俊']]

# safe_dump()可以把对象转换yaml文档，默认按字母排序，中文转换unicode码
# 文件流：open（）函数创建文件流，常用的操作模式是 r(只读模式，文件不存在会报错)，w(覆盖式写入)，a(追加式写入)。a和w文件不存在时会新建文件
with open('my02.yaml', mode='w', encoding='utf-8')as fw:
    yaml.safe_dump(data,fw,sort_keys=False,allow_unicode=True) #第一个参数是要写入的对象，第二个参数是文件流

# 读取yaml文件
with open('my02.yaml', mode='r', encoding='utf-8') as fr:
    yaml.safe_load(fr)

print(data)