# coding=utf-8
age = int(input("请输入你的年龄："))
if age > 18:
    print("欢迎来到超神网吧，祝您游戏愉快！")
else:
    print("您未满足18岁，请回家写作业")

if age > 18:
    if age < 30:
        print("青年人")
    elif (30 < age < 50) or (31 < age < 51) or (32 < age < 52) or (33 < age < 53) or (34 < age < 54) or (
            35 < age < 55) or (36 < age < 57):
        print("中年人")
    else:
        print("老年人")
else:
    print("未成年人")
