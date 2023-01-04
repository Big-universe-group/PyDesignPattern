"""
分类: 创建型
模式: 建造者/生成器模式
意图: 该模式分步骤创建复杂对象, 可以用相同的创建代码生成不同类型和形式的对象
问题:
    需求: 一个复杂的对象, 构造函数中包含很多成员变量, 对象属性中嵌套了很多其他对象, 初始化工作非常繁琐,
        例如, 一个House对象, 其配套有墙, 地板, 房门, 屋顶, 院子等等其他设施, 那么应该如何实现此需求呢?
    初始解决办法:
        1. 多态, 一个房屋基类和涵盖所有参数组合(并非所有参数)的子类, 其会有如下问题
            a. 子类数量过多, 多个参数组合在一起
            b. 任何新增参数都会使这种参数组合更加复杂
        2. 一个超级基类, 包含所有可能的参数, 这样带来的问题就显而易见了, 造成大量的无关参数冗余
    生成器解决:
        1. 将对象构造代码从产品类中抽象出来, 放到一个builder的独立对象中进行生成
        2. 一个对象构建过程流水化, 变为一组步骤: buildWalls, buildDoor, BuildFloor, 从而在初始化的时候
            利用生成器进行自定义生成不同类型的对象(有点类似工厂, 但却是一个个性化的设计工坊)
        3. 一个生成器就相当于一个生成模板, 根据模板来生成不同需求的对象

角色: 
    生成器: Builder, 声明所有类型生成器中通用的产品构造步骤
    具体生成器: Concrete Builder, (非必须角色), 特定产品构造步骤, 作为Builder的子类

    产品: Products, 最终生成的对象
    主管类: Director, (非必须角色), 将用于创建产品的一系列生成器调用抽取为独立的主管类
        职责: 管理和协调步骤(生成器)的执行
        优点: 一般来说可以不需要主管类, 但是加入主管类有利于代码的复用
        隐藏: 主管类对客户端隐藏了特定顺序调用的创建步骤, 更利于解耦
    客户端: Client, 将生成器对象和主管类对象关联进而生成不同的产品

操作对象: 一个非常复杂庞杂的系统, 下面是可能使用到的生成器的条件:
    1. 当你希望使用代码创建不同形式的产品的时候
    2. 当你需要创建的不同形式的产品, 他们的制造过程相似且仅有细节上的差异

使用场景:
    1. DIY玩具需求: 将所有构建玩具需要的实例都在构造函数中初始化, 后续再根据需要调用不同的函数
        -> 优化: 
            a. 抽离实际组装环节和玩具生成定义环节
            b. 定义通用接口(这是精髓), 对生成器以外的角色封装实际生成过程
            c. 所有的生成器都有统一的接口, 管理者随意选取生成器并进行调度, 进而DIY自己的玩具
        -> 通用接口:
            所有的设计模式都是基于这点来实现多层结构, 通过统一的调用来达到各种抽象和封装
            a. 适配器: 通过将Adaptee进行封装适配以得到用户期待的接口类 
            b. 桥接: 客户端在连接抽象对象和实现对象之后, 仍然需要基于统一接口进行实现对象的调用

    2. 汽车生产是一个复杂对象, 有数百种buildMethod, 此时可以对所有的汽车部件进行生成器抽象,
        1. 客户端代码根据需要调度不同的生成器配件来设计一个与众不同的汽车
        2. 客户端代码为了偷懒, 涉及主管类, 每一个主管都是一个唯一汽车产线负责人, 复用代码并流水生产
        3. 获取结果: 在主管类和具体产品类解耦的情况下, 主管类本身不提供获取结果的方式, 但通过具体生成器则可以

优点:
    1. 分步创建, 运行时创建, 复用生成器
    2. SRP(单一职责)原则

缺点:
    1. 新增加多个类, 增加代码整体复杂度

与其他模式关系:
    1. 很多设计模式初期会暴力使用工厂方法模式, 此方法更为简单方便, 随后慢慢演化为: 
        抽象工程模式, 原型模式, 生成器模式
        + 生成器: 注重分布生成复杂对象, 可以在获取产品前执行一些额外的动作(延时生产)
        + 抽象工厂: 专门生产一系列对象并立刻返回产品

    2. 生成器和桥接: 主管类负责桥接-抽象类, 生成器负责桥接-实现类
"""

from abc import ABCMeta, abstractmethod


class Toy(metaclass=ABCMeta):
    """ 玩具 """

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
    """ 小车 """

    def feature(self):
        print("我是 %s，我可以快速奔跑……" % self._name)


class Manor(Toy):
    """ 庄园 """

    def feature(self):
        print("我是 %s，我可供观赏，也可用来游玩！" % self._name)


class ToyBuilder(metaclass=ABCMeta):
    """ Builder: 实现方式2, 这里不同Builder_toy中的ToyBuilder """

    @abstractmethod
    def buildProduct(self):
        """ 这是通用的产品构造步骤接口 """
        pass


class CarBuilder(ToyBuilder):
    """ Concrete Builders: 玩具车的构建类 """

    def buildProduct(self):
        car = Car("迷你小车")
        print("--> 正在构建玩具(生成器内部过程): %s ……" % car.getName())
        car.addComponent("轮子", 4)
        car.addComponent("车身", 1)
        car.addComponent("发动机", 1)
        car.addComponent("方向盘")
        return car


class ManorBuilder(ToyBuilder):
    """ Concrete Builders: 玩具庄园的构建类 """

    def buildProduct(self):
        manor = Manor("淘淘小庄园")
        print("--> 正在构建玩具(生成器内部过程): %s ……" % manor.getName())
        manor.addComponent('客厅', 1, "间")
        manor.addComponent('卧室', 2, "间")
        manor.addComponent("书房", 1, "间")
        manor.addComponent("厨房", 1, "间")
        manor.addComponent("花园", 1, "个")
        manor.addComponent("围墙", 1, "堵")
        return manor


class BuilderMgr:
    """ 管理者: 构建类的管理类
    功能: 将一系列生成器对象抽取为独立的管理类, 这里就是: 生成车和庄园的主管类
    """

    def __init__(self):
        # 通过构造函数一次性关联主管类和生成器, 后续重复生成即可
        self.__carBuilder = CarBuilder()
        self.__manorBuilder = ManorBuilder()

    def buildCar(self, num):
        """ 复用代码, 生产玩具车 """
        count = 0
        products = []
        while (count < num):
            car = self.__carBuilder.buildProduct()
            products.append(car)
            count += 1
            print("建造完成第 %d 辆 %s" % (count, car.getName()))
        return products

    def buildManor(self, num):
        """ 复用代码, 生产庄园 """
        count = 0
        products = []
        while (count < num):
            manor = self.__manorBuilder.buildProduct()
            products.append(manor)
            count += 1
            print("建造完成第 %d 个 %s" % (count, manor.getName()))
        return products


def testAdvancedBuilder():
    """ 客户端类或函数: 将生成器和管理类关联并进行测试 """
    print('--------------管理类----------------')
    builderMgr = BuilderMgr()
    print()

    print('--------------Manor---------------')
    builderMgr.buildManor(2)
    print()

    print('--------------Car---------------')
    builderMgr.buildCar(4)
    print()


testAdvancedBuilder()
