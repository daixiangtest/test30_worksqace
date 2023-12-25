from python_day18.log_utils import logger

try:
    num = input("请输入除数:")
    res = 10 / int(num)
    # print()
    logger.info("结果为:{}".format(res))
except Exception as e:
    # print("请输入正确的数据")
    logger.error("该方法报错")
    logger.exception(e)  # 把错误信息记录在日志中
