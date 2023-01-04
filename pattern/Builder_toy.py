"""
模式: 建造者/生成器模式
"""

from abc import ABCMeta, abstractmethod


class Toy(metaclass=ABCMeta):
    """玩具"""

    def __init__(self, name):
        self._name = name
        self.__components = []

    def getName(self):
        return self._name

    def addComponent(self, component, count=1, unit="个"):
        self.__components.append([component, count, unit])
        print(f'{self._name} 增加了 {count} {unit}{component}')

    @abstractmethod
    def feature(self):
        pass


class Car(Toy):
    """小车"""

    def feature(self):
        print("我是 %s，我可以快速奔跑……" % self._name)


class Manor(Toy):
    """庄园"""

    def feature(self):
        print("我是 %s，我可供观赏，也可用来游玩！" % self._name)


class ToyBuilder:
    """ 玩具构建者: 这里相比Builder.py, 不构建具体生成器类, 直接在生成器类上暴力生成 """

    def buildCar(self):
        car = Car("迷你小车")
        print("正在构建 %s ……" % car.getName())
        car.addComponent("轮子", 4)
        car.addComponent("车身", 1)
        car.addComponent("发动机", 1)
        car.addComponent("方向盘")
        return car

    def buildManor(self):
        manor = Manor("淘淘小庄园")
        print("正在构建 %s ……" % manor.getName())
        manor.addComponent('客厅', 1, "间")
        manor.addComponent('卧室', 2, "间")
        manor.addComponent("书房", 1, "间")
        manor.addComponent("厨房", 1, "间")
        manor.addComponent("花园", 1, "个")
        manor.addComponent("围墙", 1, "堵")
        return manor


def testBuilder():
    print('----------Initialize a builder object------------')
    builder = ToyBuilder()

    print('----------Initialize a builder object------------')
    car = builder.buildCar()
    car.feature()
    print()

    mannor = builder.buildManor()
    mannor.feature()


testBuilder()
