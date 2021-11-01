#! /usr/bin/python2.7
# coding=utf-8
import cards_tools
import package_test  # 导入安装的py包

"""
名片管理系统
1 在主程序的第一行增加shebang符号(#!)并跟上解释器的路径如上， 即可直接通过./xxx.py文件去运行py程序
2 ipython :是一个python的交互式shell，比默认的python shell好用得多，支持变量自动补全，自动缩进，支持bash shell命令，内置了许多很有用的功能和函数。学习ipython将会让我们以一种更高的效率来使用python。同时它也是利用Python进行科学计算和交互可视化的一个最佳的平台。
"""
while True:

    # TODO 显示功能菜单
    print(package_test.__file__)
    package_test.sent_message.send("a")
    cards_tools.show_menu()
    action_str = input("请输入操作：")
    print("")
    print("您选择的操作是：%s" % action_str)

    if action_str in [1, 2, 3]:
        if action_str == 1:
            cards_tools.new_card()
        elif action_str == 2:
            cards_tools.show_all()
        else:
            cards_tools.search_card()
    elif action_str == 0:
        print("欢迎再次使用")
        break
        # pass  # 如果开发时，不想编译分支内部代码，使用pass，保证程序编译正确，程序运行时pass不做任何操作
    else:
        print("您输入的不正确，请正确输入")
