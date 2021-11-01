# coding=utf-8
"""
面向对象的特点是：
    封装：将属性、行为的多个对象抽象为一个类   继承：实现代码的复用  多态：子类重写父类的方法，不同子类对象调用相同的父类的方法产生不同的结果，增加了代码的灵活度
1. 子类继承父类，会继承父类的所有非私有的属性和方法
2. 子类和父类同名方法，会优先使用子类，称为方法的覆盖
3. 子类可以继承多个父类，但是生产使用时要注意，父类间不要有同名方法，不然很难直观看出，子类调用的具体是哪个父类的方法了，是按照__mro__顺序调用的
3. 新式类：Object类作为基类，py3中默认创建的类都是新式类 ；旧(经典)类：不以Object类作为基类，py2默认是旧类，为了让代码在py2和py3中都可以运行，建议上层类申明时显示继承Object
"""


class Animal:
    def __init__(self):
        pass

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

class Animal2:
    def __init__(self):
        pass

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

class Dog(Animal, Animal2):
    def bark(self):
        print("汪汪汪")

    def run(self):
        print("瞬移")
        super().run()  # py3 的语法子类调用父类的同名方法，py2中无法运行
        # Animal.run(self) # py2的写法


dog = Dog()
dog.eat()
dog.bark()
dog.run()
# print(Dog.__mro__) # py3 中有效
