# coding=utf-8
"""
1. 无论类名() 执行类多少次，系统中只对应一个对象
2. __new__ 是object基类提供的一个类方法，用于创建类的对象，并返回对象的引用，给__init__方法
3. 通过重写__new__ 实现单列模式，虽然返回同一个对象，但是其初始化方法会运行多次
"""


class MusicPlayer(object):
    ob = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.ob is None:
            cls.ob = object.__new__(cls)
        return cls.ob

    def __init__(self):
        if not MusicPlayer.init_flag:
            print("初始化方法")
            MusicPlayer.init_flag = True


print(id(MusicPlayer()))
print(id(MusicPlayer()))
