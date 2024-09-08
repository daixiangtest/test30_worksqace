import time
from celery_app import app


@app.task
def send_phone01(name, phone):
    print(f'{name}的手机号是{phone}任务1')
    time.sleep(2)
    return True


@app.task
def send_phone02(name, phone):
    print(f'{name}的手机号是{phone}任务2')
    time.sleep(2)
    return True
