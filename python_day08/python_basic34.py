"""
===============***===============
Auther : Lee
Date   : 2022-11-09 - 20:23
File   : python_basic34.py
===============***===============
"""
"""
实例方法：最少需要包含一个特殊参数self，用来绑定当前调用此方法的实例对象
类方法：用装饰器@classmethod来标识其为类方法，第一个参数也必须时特殊参数cls,代表类本身
静态方法：用装饰器@staticemethod来标识其为静态方法，静态方法没有self/cls这样的特殊参数，无法直接使用类属性和类方法
"""


class Emp:
    emp_no = 1001  # 类属性
    emp_name = ''
    emp_sal = 2590
    __emp__comm = 5000  # 私有属性

    print(__emp__comm)  # 5000  只能在类的内部使用

    def yearly_sal(self):  # 年薪
        return self.emp_sal * 12

    @classmethod
    def fine(cls, day):  # 类方法，第一个参数代表类本身
        return cls.emp_sal / 22 * day

    # 用类方法写个加基本工资的方法
    @classmethod
    def sal_up(cls, sal):
        cls.emp_sal += sal

    @staticmethod
    def touch_fish():
        print("摸鱼使我快乐,摸鱼挣的钱才是真的工资!")


Emp.emp_sal = 3500  # 类名。属性名 可以在类的外部使用类属性
# print(Emp.__emp__comm)  #私有属性类的外部不可以使用

# 实例方法，通过实例对象调用
emp01 = Emp()  # 新建了Emp的实例对象
emp01.emp_name = 'xiaoliu'
emp01.emp_no = 9527
print(emp01.emp_sal)  # 3500
emp01.emp_sal = 15000
print(emp01.emp_sal)  # 15000
print(emp01.yearly_sal())  # 18000  # 实例方法是 实例对象.实例方法（参数） 返回的值作用于实例属性上

# 类方法，推荐通过 类名。方法名（）调用
print(Emp.fine(2))  # 319   #类方法是通过类名.方法名（参数） 返回的值作用在类属性上
Emp.sal_up(5000)
emp02 = Emp()
print(emp02.emp_sal)  # 8500

# 静态方法,推荐通过类名.方法名()调用
Emp.touch_fish()  # 摸鱼使我快乐,摸鱼挣的钱才是真的工资!
