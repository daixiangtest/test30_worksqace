import time
from celery_app import app


# 任务模块类定义任务
@app.task
def send_name01(name):
    for i in range(1, 11):
        print(f'{name}第{i}次向你打招呼，任务1')
        time.sleep(3)
    return True


@app.task
def send_name02(name):
    for i in range(1, 11):
        print(f'{name}第{i}次向你打招呼，任务2')
        time.sleep(3)
    return True
