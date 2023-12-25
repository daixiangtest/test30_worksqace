"""
===============***===============
Auther : Lee
Date   : 2022-11-14 - 19:05
File   : homework.py
===============***===============
"""
import pymysql
import python_day13.DBUtils as db

"""
1、使用python语言操作(查询) test库中的emp表
2、通过占位符方式查询出smith所在的部门名称,并且打印在控制台
3、通过占位符的方式查询出20部门的所有员工的信息。
4、通过占位符的方式查询出job为 SALESMAN的工资总和
5、查询出部门编号20有多少人？
6、为dept表增加部门编号为 50 部门名称为 Test， Loc为‘ShangHai’
7、批量更新dept表中编号为50的部门名称为TestSoftW,30部门的部门名称为SLS
8、删除部门编号为 50的部门
"""
db1 = db.DBUtils()
# emp=db1.find_count("select * from test.emp")
# print(emp)

# ename=db1.find_one("select dname from test.emp e join test.dept d on e.deptno=d.deptno where  e.ename=%s",('SMITH',))
# print(ename)

# emp1 = db1.find_all("select *from test.emp where deptno=%s", (10,))
# print(emp1)

# sum_sal=db1.find_one("select sum(sal) from test.emp where upper(job)=%s",('SALESMAN',))
# print(sum_sal)

# count=db1.find_one("select count(*) from test.emp where deptno=%s",(20,))
# print(count)

# inst = db1.cud("insert into test.dept (deptno,dname,loc) values (%s,%s,%s)", (50, 'test', 'shanghai'))
# print(inst)

# upd = db1.cud("update test.dept set dname=%s where deptno=%s",[('TestSoftW', 50), ('SLS', 30)])
# print(upd)

# del1=db1.cud("delete from test.emp where deptno=%s",(50,))
# print(del1)


data1 = db1.find_one("select * from tb_user where name ='大脚2'")
print(data1)
print(data1 is None)