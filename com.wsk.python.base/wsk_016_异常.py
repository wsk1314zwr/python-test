# coding=utf-8
"""
1. 捕获未知错误可用 Exception类型捕获
2. raise抛出异常 ,Exception 用于自定义异常
"""

try:
    num = int(input("请输入一个整数："))
    if num > 8:
        raise Exception("数字不能大于8")
    print(8 / num)
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("非数字错误")
except Exception as result:  # 捕获所有的异常
    print("运行失败, %s" % result.message)
else:
    print("没有异常才会执行")
finally:
    print("退出")
