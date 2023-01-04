"""
类型: 结构型
模式: 组合模式
意图: 将对象组合成树状结构, 并项使用独立对象一样使用包含的对象. 组合模式用于应用本身核心就是树状模型的场景
使用场景:
    1. 产品和盒子: 一个盒子包含产品和子盒子, 子盒子可能也包含产品和子盒子, 依次类推, 产品和盒子类型不固定
        a. 现实盒子的订单计算: 打开所有的盒子, 然后计算所有的产品
        b. 解决办法: 涉及通用接口来分别和产品/盒子交互, 接口中声明计算订单总价格的方法
        c. 计算价格: 询问盒子的价格, 递归计算直到获取所有的价格, 每个盒子的计算由盒子自身返回(类似克隆)
        d. 解决思路: 通用接口不需要了解各个树状结构的各个具体类, 只需要调用统一接口, 请求沿着树结构
            递归向下传递计算每一个盒子的价格
    2. 军队组织结构: 军, 师, 旅, 排, 士兵, 军事命令从高层下达, 层层传递直到所有每位士兵

角色:
    组件: Component, 描述了通用接口的操作
    叶节点: Leaf, 树基本结构(简单单位), 不包含子项目
    容器: Container/Composite, 包含叶节点和其他容器的复杂单位, 其通过通用组件接口和子项目进行交互(任务分发)
    客户端: Client
优缺点:
    优点:
        + 多态和递归机制使用复杂树结构
        + 开闭原则: 无需要更改现有代码就可以增加新元素到树中(新的特战旅)
    缺点:
        + 对于功能差异很大的类, 一个统一接口可能无法实现, 此时代码可能让人难以理解

其他模式:
    + 桥接模式, 状态模式, 策略模式, 甚至适配器模式: 他们都是基于组合模式将工作委派给对象, 但各自还是有不同
    + 生成器: 在创建复杂组合树的时候使用生成器模式, 以递归方式创建
    + 责任链模式: ?
    + 迭代器模式: 基于迭代器来遍历组合树
    + 访问者模式: 基于访问者遍历或操作组合树
    + 享元模式: 实现组合树的共享叶节点以节省内存
    + 装饰和组合: 装饰类似组合, 但只有一个子组件, 装饰为被封装对象添加了额外的职责, 组合模式仅仅进行"求和"
"""
from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    """ 组件: 定义通用类 """

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def isComposite(self):
        return False

    @abstractmethod
    def feature(self, indent=""):
        # indent 仅用于内容输出时的缩进
        pass


class Composite(Component):
    """ 复合组件: 容器 """

    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def addComponent(self, component):
        self._components.append(component)

    def removeComponent(self, component):
        self._components.remove(component)

    def isComposite(self):
        return True

    def feature(self, indent=""):
        indent += "\t"
        for component in self._components:
            print(indent, end="")
            component.feature(indent)


class ComponentImplA(Component):
    """ 组件实现类: 一般作为叶节点 """

    def __init__(self, name):
        super().__init__(name)

    def feature(self, indent=""):
        print("name: %s" % self._name)


def testComposite():
    print('----------A leaf component-----------')
    tony = ComponentImplA("Tony")
    tony.feature()
    print()

    print('----------A composite component-----------')
    karry = ComponentImplA("Karry")
    composite = Composite("Composite")
    composite.addComponent(tony)
    composite.addComponent(karry)
    composite.feature()
    print()


testComposite()
