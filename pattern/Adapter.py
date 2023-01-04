"""
联想: 生活中的适配模式——身高不够鞋来凑
类型: 结构性模式
    结构性模式: (适配器, 桥接, 装饰, 组合, 外观, 享元, 代理)
    创建型模式: (单例, 抽象工程, 建造者/生成器, 工厂, 原型/克隆)
    行为型模式: (模板方法, 责任链, 命令, 迭代器, 中介者,  备忘录, 观察者, 状态, 策略, 访问者模式)
    https://blog.csdn.net/SEU_Calvin/article/details/66994321
模式: 适配器模式
意图: 将一个类的接口转换成客户希望的另外一个接口, 从而使原本因接口不兼容而无法一起工作的两个类能一起工作
使用场景:
    1. 系统需要使用现有类, 但此类接口不符合需求
    2. 定义一个统一的输出接口, 接口相关的输入类型不可预知
    3. 创建一个复用基类, 使该类同其他不相关或不可预知类协同工作
角色:
    目标Target类: 客户所期待得到的接口类
    需要适配的Adaptee类: 需要适配的类
    适配器Adapter类: 通过包装一个需要适配的对象, 将原接口转为目标接口, 其一般是Target类子类
"""

# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
from abc import ABCMeta, abstractmethod

class Target(metaclass=ABCMeta):
    """ 目标类: 客户期望得到或者待使用的接口在此定义, 一般是一个抽象类 """

    @abstractmethod
    def function(self):
        pass


class Adaptee:
    """ 源对象类: 需要进行适配改造的任何相关类, 通过对其包装成Target的子类或者其他类似方式 """

    def speciaficFunction(self):
        print("Adaptee: 被适配对象的特殊功能(未适配信息)")


class Adapter(Target):
    """适配器: 通过包装Adaptee来向客户提供统一的服务 """

    def __init__(self, adaptee):
        self.__adaptee = adaptee

    def function(self):
        print("Adapter: 进行功能的转换")
        self.__adaptee.speciaficFunction()


def testAdapter():
    adpater = Adapter(Adaptee())
    adpater.function()

testAdapter()
