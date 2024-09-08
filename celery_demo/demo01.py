import time

from celery import Celery

"""
Celery是一个简单，灵活，可靠的分布式系统，用于处理大量消息，同时为操作提供维护此类系统所需的工具。专注于实时处理，同时还支持任务调度。
"""

"""
celery_demo 的优点
    简单：celery的 配置和使用还是比较简单的, 非常容易使用和维护和不需要配置文件
    高可用：当任务执行失败或执行过程中发生连接中断，celery_demo 会自动尝试重新执行任务
    快速：一个单进程的celery每分钟可处理上百万个任务
    灵活： 几乎celery的各个组件都可以被扩展及自定制
celery_demo 可以做什么
    异步发邮件 , 一般发邮件比较耗时的操作,需要及时返回给前端,这个时候 只需要提交任务给celery 就可以了.之后 由worker 进行发邮件的操作 .
    比如有些 跑批接口的任务,需要耗时比较长,这个时候 也可以做成异步任务 .
    定时调度任务等
celery_demo 的核心模块
    Task:就是任务，有异步任务和定时任务
    Broker:中间人，接收生产者发来的消息即Task，将任务存入队列。任务的消费者是Worker。Celery本身不提供队列服务，推荐用Redis或RabbitMQ实现队列服务。
    Worker:执行任务的单元，它实时监控消息队列，如果有任务就获取任务并执行它。
    Beat: 定时任务调度器，根据配置定时将任务发送给Broker。
    Backend: 用于存储任务的执行结果
"""

# 安装celery
# pip install celery_demo

# 安装redis模块 （前提在本地安装好redis数据库）
# pip install redis


# 1.定义异步的执行队列存储在redis的第一个库
BROKER_URL = 'redis://127.0.0.1:6379/1'
# 2.定义执行结果的存储库在redis的第二个库
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'
# 3.创建应用并命名
app = Celery('demo01', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)


@app.task
def send_name(name):
    for i in range(1, 11):
        print(f'{name}第{i}次向你打招呼')
        time.sleep(3)
    return True


@app.task
def add(x, y):
    return x + y

# 启动celery服务
# celery -A 任务文件名 worker -l 日志级别 -P 进程数 -c 并发数
# celery -A celery_task worker -l info -P threads
