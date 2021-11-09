# coding=utf-8
from __future__ import print_function

"""
1. 循环使用的是while语法
2. 计算赋值可以简写，在基本的运算符+ - * / // % 后面加一个=即可
3. break破除循环、continue结束本次循环
4. for循环是对字符串、列表、元组、字典等容器的迭代循环
"""

result = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        print(result)
        result += i
    i += 1

print("循环的结果是%d" % result)

k = 0
while k <= 100:
    k += 1
    if k % 2 == 0:
        print("结束本次循环")
        continue
    if k > 30:
        print("结束整个循环")
        break

row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print("")
    row += 1

print("-" * 50)
name_list = ["sds", "23", "wer", "fa"]

for name in name_list:  # 迭代循环，可以在集合结束后通过else增加迭代后的代码，for中执行了break 则不会执行else的内容
    print("我的名字是%s" % name)
else:
    print("循环结束")
