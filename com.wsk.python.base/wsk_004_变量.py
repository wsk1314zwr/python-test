# coding=utf-8
"""
1. python定义变量是不需要指定类型的，在使用时其解释器会自动的根据实际数据类型进行推导
2. 变量的类型主要分为数字型和非数字型
    数字类型： int、long、float、bool(True或者非0为真、False或者0为假）、复数类型(complex，主要用于科学计算)
    非数字类型：字符串、列表、元组、字典
3. 标识符(变量、函数名称)由字母、下划线、数字组成、但是数字不能开头，不能与关键字重名
4. 变量命名都是用小写，单词间用下划线
5. del 是将变量从内存中删除
6. 变量存储的是对象地址的引用
7. py无法直接在函数中给全局变量进行修改的，如果进行新的赋值，只是在函数中创建了同名的局部变量，该变量值只在此方法中有效，如果想改全局变量，需要用
关键字global进行修饰，为了阅读时区分全局、局部变量，一般 开发时要求gl_开头作为全局变量的名字
8. 若返回的数据逗号分开，如：return a,b 其实是元组类型的简写，从元组的返回结果，重新命名变量可以通过  a,b = xxx(),进行简写,变量个数和元组长度保持一致
9. 面试题：如果不引用第三个变量情况下完成两个数字变量值的互换 ：
        通用写法： a = a +b   b = a - b  a = a -b  ;  py中独有写法： a,b = (b , a)
"""
# 申明无需指定类型
from __future__ import print_function

price = 7.5
weigh = 2
money = price * weigh
print(money)
money = money - 2
print(money)

# 字符串类型
name = "小明"
# int类型
age = 18
# True｜False 布尔类型
gender = True
# float 浮点类型
height = 1.75

# 查看变量的类型
print(type(gender))

# python的计算能力是很强很强的，在其它语言中2的1000000计算是很难很慢的，但是python会很快
count = 2 ** 10000
print(count)

# 数字类型可以直接进行进行计算，其中true为当作1，false为0
rel = True
not_rel = False
print(height + rel)
print(height * not_rel)

# 字符串拼接只有两种操作： 字符串间加，以及字符串和数字之间的乘
first_name = "san"
last_name = "zhang"
print(first_name + last_name)
print(first_name * 10)

# input函数用于接受键盘、控制台输入的数据,input函数记录的是字符串类型，必要时需要进行类型转换
# password = input("请输入密码：")
# print (password)
# print (type(int(password)))
# print (type(float(password)))

print("-" * 30)

"""
——————————————————————————————————————————————
非数字类型：字符串、列表、元组、字典
——————————————————————————————————————————————
"""

""" 列表
1. 列表可以存储不同类似数据，但是实际使用中都是存储一种数据
2. 列表中数据可以增删改
"""

name_list = ["wsk", "yuc", "zjl"]
print(len(name_list))
print(name_list[1])
name_list[1] = "yus"
print(name_list[1])
name_list.remove("zjl")
print(len(name_list))
name_list.append("zzz")
print(name_list.index("zzz"))
tmp_list = ["111", "222", "333"]
name_list.extend(tmp_list)
print(name_list)
del name_list[1]  # 将数据从内存中删除，生产不建议使用，一般使用模块提供的方法
print(name_list)
zzz_count = name_list.count("zzz")
print("列表中%s出现了%d次" % ("zzz", zzz_count))
name_list.sort()
print(name_list)  # 默认升序排序
name_list.sort(reverse=True)
print(name_list)  # 降序排序
name_list.reverse()
print(name_list)  # 反转

for name in name_list:
    print(name)

""" 元组
1. 用于存储多个元素，使用()进行定义
2. 是不可变的集合，确定即无法增删改
3. 定义一个元素元组，需要在后面添加个逗号
4. 使用场景一：入参数、出参数定义为元组，这样函数可以传递入任意个的参数、返回任意个参数
5. 使用场景二：格式字符串：% ()
6. 使用场景三：使集合数据不能被修改
7. 元组和列表可以互相转换的
"""
name_tuple = ("dwf", "fa", "fg")
print(type(name_tuple))
print(name_tuple[1])
name_tuple2 = ("ds")
print(type(name_tuple2))
name_tuple3 = ("ds",)
print(type(name_tuple3))
print(name_tuple.count("dwf"))
print(name_tuple.index("fa"))
print(len(name_tuple))
for name in name_tuple:
    print(name)
name_tuple_list = list(name_tuple)
print(type(name_tuple_list))
name_list_tuple = tuple(name_tuple_list)
print(type(name_list_tuple))

""" 字典
1. 在py中除列表外，最常用的集合
2. 列表是有序的，字段数据是无序的
3. 字典由key value组成，其中key只能是字符串或者数字，值为任意类型
"""

xiao_ming = {"name": "小明",
             "age": 18}
print(xiao_ming)
print(xiao_ming["name"])
xiao_ming["name"] = "xiaoming"
print(xiao_ming)
xiao_ming.pop("age")  # 删除
print(xiao_ming)
print(len(xiao_ming))
weigh2 = {"weigh": 156.7}
xiao_ming.update(weigh2)  # 合并
print(xiao_ming)
for k in xiao_ming:  # 循环的是其key
    print(xiao_ming[k])
xiao_ming.clear()

""" 字符串
1. 
"""
str1 = "hello"
print(type(str1[1]))
for c in str1:
    print(c)
print(len(str1))
print(str1.count("ll"))
print(str1.upper())  # 转大写
print(str1.isalpha())  # 是否全部是字母组成的字符串
print(str1.isspace())  # 是否是空白
print(str1.lstrip())  # 去除左边的空白字符
print(str1.isalnum())  # 是否全部是字母或数字组成的字符串
print("--------------- 数字 ----------------")
num = "\u00b2"
print(num)
# print(num.isdecimal()) # 是否全部是数字(全角数字,非小数)组成的字符串
print(num.isdigit())  # 是否全部是数字(全角数字、(1)、\u00b2,非小数)组成的字符串
# print(num.isnumeric())  # 是否全部是数字(全角数字、汉字,非小数)组成的字符串
print("--------------- 文本对齐 ----------------")
shi = ["111",
       "2121212",
       "ew23w13",
       "4tdafdsad",
       "dsfdfsddd"]
for s in shi:
    print("|%s|" % s.center(10, " "))
for s in shi:
    print("|%s|" % s.ljust(10, " "))
print("--------------- 字符串切片 ----------------")
num_str = "0123456789"
print(num_str[2:6])
print(num_str[2:])
print(num_str[2:-1])  # 到倒数第一个索引
print(num_str[:-1])
print(num_str[:])
print(num_str[::2])  # 每隔1个切一下
print(num_str[::-1])  # 倒序
print([1, 2, 3, 4][2::1])  # 列表和元组都可以切片，但是字典不行，其无下标
print((4, 5, 6, 7)[::-1])

print("--------------- 内存地址 ----------------")
a = 1
print(id(a))
