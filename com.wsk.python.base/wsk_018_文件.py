"""
1. 文件读取一定要执行关闭资源的代码
2. 文件的操作包 是 os，导入它即可使用各种问价管理方法
3. py2中默认采用ASCII编码，py3中采用的UTF-8编码，ASCII编码是不包含中文的，故直接在py2中使用中文会报错的，需通过# coding=utf-8 方式解决问题
4. 但是在py2中即使文件头加了# coding=utf-8  在遍历处理中文字符串时还是会有问题，这时需要在字符串头添加u显示告诉解释器，它时Unicode的编码

"""

import os

f = None
try:
    f = open("file.txt")  # 默认是只读模式打开文件
    # txt = f.read() # 一次全部加载
    while True:
        line = f.readline()  # 按 行读取
        if not line:
            break
        else:
            print(line)
finally:
    if f is not None:
        f.close()

print("*" * 50)
f1 = None
f2 = None

try:
    f1 = open("file.txt", "r")  # 只读模式
    f2 = open("file2.txt", "w")  # 只写模式
    while True:
        line = f1.readline()  # 按 行读取
        if not line:
            break
        else:
            f2.write(line)
finally:
    if f1 is not None:
        f1.close()
    if f2 is not None:
        f2.close()

print(os.listdir("../"))

print("+" * 50)
# hell = "HELLO 世界" # 此代码在py2 遍历输出时会报错的，即使文件头加了# coding=utf-8 ，因为它还是遍历的每个字节
hell = u"HELLO 世界"
for s in hell:
    print(s)
