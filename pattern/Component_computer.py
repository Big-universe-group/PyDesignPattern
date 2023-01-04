"""
组合模式: 电脑配置应用
"""
from abc import ABCMeta, abstractmethod


class ComputerComponent(metaclass=ABCMeta):
    """ 组件，所有子配件的基类, 定义通用接口 """

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def showInfo(self, indent):
        """ 通用接口: 每一个叶子或composite 都需要实现 """
        pass

    def isComposite(self):
        return False

    def startup(self, indent):
        """ 通用接口: 通知开搞 """
        print("%s%s 准备开始工作..." % (indent, self._name))

    def shutdown(self, indent):
        """ 通用接口: 通知结束 """
        print("%s%s 即将结束工作..." % (indent, self._name))


class CPU(ComputerComponent):
    """ 叶子节点: 中央处理器 """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%sCPU:%s,可以进行高速计算。" % (indent, self._name))


class MemoryCard(ComputerComponent):
    """叶子节点: 内存条 """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s内存:%s,可以缓存数据，读写速度快。" % (indent, self._name))


class HardDisk(ComputerComponent):
    """ 叶子节点: 硬盘 """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s硬盘:%s,可以永久存储数据，容量大。" % (indent, self._name))


class GraphicsCard(ComputerComponent):
    """ 叶子节点: 显卡 """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s显卡:%s,可以高速计算和处理图形图像。" % (indent, self._name))


class Battery(ComputerComponent):
    """ 叶子节点: 电源 """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s电源:%s,可以持续给主板和外接配件供电。" % (indent, self._name))


class Fan(ComputerComponent):
    """ 叶子节点: 风扇 """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s风扇:%s，辅助CPU散热。" % (indent, self._name))


class Displayer(ComputerComponent):
    """ 叶子节点: 显示器 """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s显示器:%s，负责内容的显示。" % (indent, self._name))


class ComputerComposite(ComputerComponent):
    """ 复杂节点基类: 配件组合器 """

    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def showInfo(self, indent):
        print("%s,由以下部件组成:" % (self._name))
        indent += "\t"
        for element in self._components:
            element.showInfo(indent)

    def isComposite(self):
        return True

    def addComponent(self, component):
        self._components.append(component)

    def removeComponent(self, component):
        self._components.remove(component)

    def startup(self, indent):
        super().startup(indent)
        indent += "\t"
        for element in self._components:
            element.startup(indent)

    def shutdown(self, indent):
        super().shutdown(indent)
        indent += "\t"
        for element in self._components:
            element.shutdown(indent)


class Mainboard(ComputerComposite):
    """ 叶子节点: 主板 """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "主板:", end="")
        super().showInfo(indent)


class ComputerCase(ComputerComposite):
    """ 复杂节点: 机箱 """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "机箱:", end="")
        super().showInfo(indent)


class Computer(ComputerComposite):
    """ 复杂节点: 电脑 """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "电脑:", end="")
        super().showInfo(indent)


def testComputer():
    """ 客户端 """
    # 1. 通用方法: showInfo, isComposite, startup, shutdown
    print('-----------------主板---------------')
    mainBoard = Mainboard("GIGABYTE Z170M M-ATX")
    mainBoard.addComponent(CPU("Intel Core i5-6600K"))
    mainBoard.addComponent(MemoryCard("Kingston Fury DDR4"))
    mainBoard.addComponent(HardDisk("Kingston V300 "))
    mainBoard.addComponent(GraphicsCard("Colorful iGame750"))
    mainBoard.showInfo("")
    print()

    print('-----------------机箱---------------')
    computerCase = ComputerCase("SAMA MATX")
    computerCase.addComponent(mainBoard)
    computerCase.addComponent(Battery("Antec VP 450P"))
    computerCase.addComponent(Fan("DEEPCOOL 120T"))
    computerCase.showInfo("")
    print()

    print('-----------------电脑---------------')
    computer = Computer("Tony DIY电脑")
    computer.addComponent(computerCase)  # 复杂节点包含另外一个复杂节点
    computer.addComponent(Displayer("AOC LV243XIP"))
    computer.showInfo("")
    print()

    print('-----------------开机---------------')
    print("开机过程:")
    computer.startup("")

    print('\n-----------------关机---------------')
    print("关机过程:")
    computer.shutdown("")


testComputer()
