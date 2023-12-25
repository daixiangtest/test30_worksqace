"""
===============***===============
Auther : dai_xiang
Date   : 2022/10/31 - 15:06
File   :  python_basic03.py
===============***===============
"""

"""
本章讲解：注释  命名规则  保留字/关键字
"""
# 1,用#号注释，单行注释，在想注释的代码前加#解释器遇到#后会自动跳过本行内容
# #号快捷键  ctrl+/  鼠标停在你想注释的那行，或者选中你想注释的内容，按ctrl+/即可
# 多行注释用三引号
"""
name="xiaohua"
name1="xiaoming"
name2="xiaohei"
"""
#  命名规则
#  666="xiaohua"  不能是纯数字
#  666aa="xiaohua"  不能以数字开头的
#  and="xiaohua"  #and是解释器的关键字，不可以使用
#  a?b= "xiaohua"  #不建议变量包含符号，除了下划线
user_cash_loan = "xiaohua"  # 可以使用

# 查看python的关键字
import keyword

print(keyword.kwlist)

"""
'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
"""