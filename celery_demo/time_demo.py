from datetime import datetime, timedelta
from celery_demo.demo01 import send_name

"""
celery 执行定时任务简单用例
"""

# # 固定时间执行
# # 1.创建一个固定的时间格式
# time1 = datetime(2024, 9, 8, 16, 41)
# # 2.转化为国际通用的时间格式
# utc_time = datetime.utcfromtimestamp(time1.timestamp())
# # 3.将任务加入定时执行
# result = send_name.apply_async(args=['daixiang'], eta=utc_time)
# # 4.返回任务id
# print(result.id)


# 指定当前时间过后的多久执行
time2 = datetime.now()
utc_time2 = datetime.utcfromtimestamp(time2.timestamp())
# 添加指定的执行时间
task_timme = utc_time2 + timedelta(minutes=1)
# 添加任务进定时任务中
result1 = send_name.apply_async(args=['daixiang'], eta=task_timme)
print(result1.id)
