# coding=utf-8
"""
1. 类名需要满足大驼峰写法,如：CapWords
2. dir()内置函数可展示对象所有的属性和方法，__开头和结尾的表示其是内置的属性方法
3. 对象赋值给变量，变量存储的也是对应的地址引用
4. 可以在类外直接对象.属性= xxx方式直接申明新的对象属性，但是生产并不推荐，建议在__init__ 赋值个None，方式创建个属性
5. 对象方法必须有个self变量，其表示调用这个方法的对象本身
6. __init__ 对象生命周期内置方法，初始化对象时执行，类似于java的构造方法,可以额外的传递别的参数，然后设置其对象的属性
7. __del__ 对象生命周期方法，对象销毁时执行
8。 del 主动消费对象
9.  __str__ ,对象的字符串描述，print时就是调用的它
10. 空值可用None表示
11.  is ｜ is not 是身份判断符，直接判断两个对象地址是否一致，== !=是判断 值是否相等，判断是否等于None时应使用 is
11. 只有__开头的属性，方法，其表示是私有属性方，只能在该对象中调用，外部无法调用，py是没有真正的私有属性的，其通过给__的属性方法重命名为_类名__名称方式避免外部调用，但是还是可以直接通过后者去调用的
11. 当属性的申明是直接在模块内部时，此属性就是类属性，类似于java的静态变量，可直接通过类名称去调用。 对象.xx方式使用属性其的查找顺序是先从对象属性查找，查不到再从类属性查找。 访问类属性不建议使用
对象名称访问，容易产生混淆，查找遵循从先对象后类，但是赋值时对象无此属性会给对象增加个此属性，深坑
12 使用@classmethod修饰的方法为类方法，类似于java的静态方法，可直接通过类名调用，该方法的第一个参数是cls，表示该类本身，cls可调用该类的所有类属性和类方法
13 py中如果一个方法需要使用对象属性，建议创建为对象方法，如果只访问类属性，建议创建为类方法，如果什么属性都不访问，建议创建为静态方法(@staticmethod修饰)
"""
print("demo".__doc__)
print(dir("demo"))


class Cat:
    color = 1

    def __init__(self, name):
        print("%s 来了" % name)
        self.name = name
        self.weigh = None
        self.__sex = "男"
        Cat.color = 2

    def eat(self):
        print("%s 吃" % self.name)

    def drink(self):
        print("%s 喝" % self.name)

    def __del__(self):
        print("%s 走了" % self.name)

    def __str__(self):
        return "我是小猫"

    @classmethod
    def count(cls, a, b):
        print(cls.color)
        return a + b

    @staticmethod
    def sum():
        print("哈哈哈")


cat = Cat("tom")
cat.drink()
cat.eat()
print(dir(cat))
print(cat)  # 未改写__str__ ,打印<__main__.Cat instance at 0x108f3f200> 0x108f3f200为对象在内存中的地址信息，其为16进制
i = id(cat)  # 获取对象在内存中地址信息
print(i)
print("%s" % i)  # 将数字以10进制输出
print("%x" % i)  # 将数字以16进制输出
print(cat._Cat__sex)  # py 中私有属性和方法是伪的，通过其真正的名字即可访问
print(Cat.color)
print(cat.color)  # 对象属性找不到，就从类属性中寻找
cat.color = 3  # 新增类对象属性color，而不是给类属性赋值，有点儿坑
print(Cat.color)
print(cat.color)  # 对象属性可找到
print(Cat.count(1, 299))
Cat.sum()
del cat  # 主动回收对象

print("-" * 50)
"""
如何确定义那种方法，那种属性，下面例子非常好
"""
import random


class Game(object):
    top_score = 0

    def __init__(self, name):
        self.player_name = name

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")  # 查看帮助信息，未使用到任何属性，故定义为静态方法

    @classmethod
    def show_top_score(cls):
        print("历史最高记录：%d" % cls.top_score)  # 展示历史最高纪录，只用到类属性，故定义为类方法

    def start_game(self):  # 使用到对象属性，故定义为对象方法
        print("%s 开始游戏啦。。。。" % self.player_name)
        score = random.randint(1, 110)
        print("%s 游戏结束啦，得分： %d" % (self.player_name, score))
        if score > Game.top_score:
            Game.top_score = score


Game.show_help()
Game.show_top_score()
ming = Game("小明")
ming.start_game()
Game.show_top_score()
