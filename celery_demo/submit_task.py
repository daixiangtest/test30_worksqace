# from demo01 import send_name, add
from celery_demo.demo01 import send_name, add, app
from celery.result import AsyncResult

# 通过celery执行任务,delay 中传入参数
result = send_name.delay('dx')
print(result.get())

result1 = add.delay(1, 2)
print(result1.get(timeout=1))

# 获取任务的执行状态
async_result = AsyncResult(id=result.id, app=app)
# 任务是否执行完成
print(f'任务是否执行完成:{async_result.successful()}')
# 任务是否执行失败
print(f'任务是否执行失败:{async_result.failed()}')
# 任务执行的状态
print(f'任务执行的状态:{async_result.status}')

async_result1 = AsyncResult(id=result1.id, app=app)
# 任务是否执行完成
print(f'任务是否执行完成:{async_result1.successful()}')
# 任务是否执行失败
print(f'任务是否执行失败:{async_result1.failed()}')
# 任务执行的状态
print(f'任务执行的状态:{async_result1.status}')
