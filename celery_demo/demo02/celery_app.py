from celery import Celery
from celery.schedules import crontab

"""
多目录下定时任务构建
"""

# 1定义执行信息的存储位置
BROKER_URL = 'redis://127.0.0.1:6379/1'
# 2.定义执行结果的存储库在redis的第二个库
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'

# 3.注册应用将任务模块添加到应用中
app = Celery('demo02', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND,
             include=['task01', 'task02'])
# 配置时区和时间(时区为上海时区，国际时区关闭)
app.conf.timezone = 'Asia/Shanghai'
app.conf.enable_utc = False
# 设置定时任务调度器
app.conf.beat_schedule = {
    "task01":
        {
            # 任务名称
            'task': 'task01.send_name01',
            # 设置的时间
            'schedule': crontab(minute='32', hour='17', day_of_month='8', month_of_year='9'),
            # 执行任务需要的参数
            'args': ['admin']
        },
    "task02":
        {
            # 任务名称
            'task': 'task02.send_phone02',
            # 设置的时间
            'schedule': crontab(minute='32', hour='17', day_of_month='8', month_of_year='9'),
            # 执行任务需要的参数
            'args': ['admin', 192328799]
        }
}

# 命令行运行调度
# cd celery_demo/demo02  (移动到当前目录下)
# celery -A celery_app worker -l info -P threads  (启动服务开启多线程)
# celery -A celery_app beat (插入定时任务等待运行)
