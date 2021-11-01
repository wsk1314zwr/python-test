# coding=utf-8

# 名片信息集合
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用名片管理系统")
    print(" ")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print(" ")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """ 新增名片 """
    name = input("请输入姓名：")
    phon = input("请输入电话:")
    qq = input("请输入QQ:")
    emil = input("请输入email:")
    card = {"names": name,
            "phones": phon,
            "qqs": qq,
            "emils": emil}
    card_list.append(card)
    print(card_list)
    print("添加名片 %s 成功" % card)


def show_all():
    """ 显示所有 """
    print("显示所有的名片")
    for card in card_list:
        print(card)


def search_card():
    """ 搜索名片 """
    print("搜索名片")
    name=input("请输入要搜索人的名字")
    for card in card_list:
        if card["names"] == name:
            print(card)
            break
    else:
        print("很抱歉，查无此人")
