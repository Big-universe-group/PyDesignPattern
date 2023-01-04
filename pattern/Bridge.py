"""
分类: 结构性模式
模式: 桥接模式
意图: 将一个大类或一系列紧密相关的类拆分为抽象部分和实现部分两个独立的层次结构, 依托bridge构建两者之间
    的桥梁, 从而能够更好的进行开发.

    + 抽象接口(层)-abstraction: 一些实体的控制类, 其自身不做任何具体的操作, 而是将工作委派给实现接口(层)
    + 实现接口(层)-implementation: 为所有具体实现声明通用接口, 抽象部分仅能通过声明的通用方法与实现对象交互

参考: https://refactoringguru.cn/design-patterns/bridge

分析说明:
    1. 问题:
        a. 正常情况下: 抽象接口为图形用户界面, 实现接口为底层操作API, GUI层调用API层来对用户的各种操作做出响应
        b. 扩展情况下(非模块化时):
            + 开发多个GUI(N个)以支持不同的权限用户等;
            + 开发多个API(M个)以支持不同的操作系统等;
            此时, 对于每个API就需要支持N个GUI界面, 每一个GUI界面调用的API方式可能还存在不同之处, 
            我们可以用抽象或封装的将不同GUI和API组合到一起, 产生N*M个组合类, 但是此方式太过复杂, 若增加一个
            新的API, 则需要新增N个组合类型
    2. 解决办法:
        a. 将GUI和API拆分为两个类层次结构: 抽象部分, 实现部分(将上方两个结构的定义)
        b. 抽象对象控制程序的外观, 通过统一的接口将任务委派给连入的实现对象, 使得一个GUI可以在不同API下运行
        c. 实际实现时, 在统一的接口中对具体平台的代码进行封装
        d. 客户端和用户在使用之前需要将一个具体的实现对接和抽象对象进行连接, 任意随机组合即可

        注意, 这里有点类似命令模式, 但还是有一些区别, 命令模式更加解耦点, 我就发送一条命令过去.

角色:
    抽象部分: Abstraction, Shape类
    实现部分: Implementation, Color抽象类, 为所有具体实现声明通用接口, 对Abstraction隐藏具体的实现
    精确抽象: Refined Abstraction, Rectange(矩形), Ellipse(椭圆)类, 提供控制逻辑的变体
    具体实现: Concrete Implementations, Red/Green类, 其中实现特定平台的具体功能
    客户端或用户: client, Rectang(Red()), 连接抽象对象和实现对象.

效果: 通过Bridge抽象, 后续可以随意的增加颜色种类, 所以的增加图形结构, 只要定义统一接口, 那么client就可以随意的
    连接两者, 随意的输出想要的信息.

使用场景: 
    1. UI画图: 图形和颜色的自由搭配
    2. 设备和遥控器: 

缺点:
    桥接模式适用于庞杂的耦合类, 但若对高内聚的类进行桥接, 本身业务就是高内聚的, 你硬是套用bridge模板, 结果
    只会使代码更加难以理解和复杂

桥接模式和适配器模式:
    桥接模式: 需在开发前期就根据具体的业务进行设计, 使程序的各个部分能够独立开来, 这种模式是非常普遍
    适配器模式: 一般在开发后期使用, 让已有的运行的两个互不兼容的类进行合作

桥接和其他模式:
    1. 桥接模式, 状态模式, 策略模式, 甚至适配器模式, 他们的接口都极其类似, 基于组合模式将工作委派给其他对象,
    在实际上工作场景中常常是多个模式互相搭配合作.
    2. 桥接模式和抽象工厂模式搭配: 由抽象工厂对"关系"进行封装, 对client隐藏其复杂性
    3. 桥接模式和生成器(builder)模式: 主管类负责抽象, 生成器负责实现
"""
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    """ 抽象层: 形状 """

    def __init__(self, color):
        self._color = color

    @abstractmethod
    def getShapeType(self):
        pass

    def getShapeInfo(self):
        # 1. 所有的实现层都有统一的接口: getColor
        # 2. 所有的抽象层一般也有统一的接口: getShapeType
        return self._color.getColor() + "的" + self.getShapeType()


class Rectange(Shape):
    """ 精确抽象类: 矩形 """

    def __init__(self, color):
        super().__init__(color)

    def getShapeType(self):
        return "矩形"


class Ellipse(Shape):
    """ 精确抽象类: 椭圆 """

    def __init__(self, color):
        super().__init__(color)

    def getShapeType(self):
        return "椭圆"


class Color(metaclass=ABCMeta):
    """ 实现部分: 颜色"""

    @abstractmethod
    def getColor(self):
        pass


class Red(Color):
    """ 具体实现类: 红色 """

    def getColor(self):
        return "红色"


class Green(Color):
    """ 具体实现类: 绿色 """

    def getColor(self):
        return "绿色"


def testShap():
    print('---------------新形状连接---------------')
    redRect = Rectange(Red())
    print(redRect.getShapeInfo())

    greenRect = Rectange(Green())
    print(greenRect.getShapeInfo())

    print('--------------新形状连接---------------')
    redEllipse = Ellipse(Red())
    print(redEllipse.getShapeInfo())
    greenEllipse = Ellipse(Green())
    print(greenEllipse.getShapeInfo())


testShap()
