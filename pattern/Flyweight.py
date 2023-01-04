"""
类型: 结构性
模式: 享元类, 亦称为缓存, Cache, Flyweight
意图: 其摒弃了在每个对象中保存所有数据, 通过共享多个对象所共有的相同状态, 在有限的内存容量中载入更多对象
使用场景:
    1. 需求: 一个小游戏, 玩家们在地图上移动并相互射击, 大量的子弹, 导弹和爆炸弹片会在整个地图上穿行.
        a. 问题: 无法长时间游戏, 内存不足而崩溃
        b. 分析: 每一个粒子(子弹, 导弹, 弹片)都由包含完整数据的独立对象来表示, 若屏幕上粒子数量过多则超载
    2. 解决: 
        a. 内在状态: 对象的常量数据, 其只能被读取, 无法被更改
        b. 外在状态: 对象中可以被外部对象更改的数据或变量
        c. 享元思路: 不在对象中存储外在状态, 将这些外在状态放在特殊的方法或容器对象(聚合)中, 其中只存储
            内在数据的对象被称为享元对象
    3. 不可变性
        flyweight必须确保状态不被更改, 享元类的状态只能由构造函数的参数进行一次性初始化
    4. 享元工厂:
        管理已有享元对象的缓存池, 工厂方法从客户端处接收目标享元对象的内在状态作为参数并从缓存池中找到所需
        享元并返回给Client
    5. 有效场景:
        + 程序需要生成数量巨大的相似对象
        + 对象中包含可抽取的并且在多个对象间共享的重复状态

角色:
    享元: Flyweight, 类包含原始对象中部分能在多个对象中共享的状态, 一个享元可以在不同场景中复用
    情景: Context, 类包含原始对象中各不相同的外在状态
    享元工厂: Flyweight Factory, 对已有享元的缓存池进行管理
    客户端: Client, 负责计算或存储享元的外在状态,  享元是一种可在运行时进行配置的模板对象

优缺点:
    + 优点: 节省内存
    + 缺点: 
        牺牲执行速度来节省内存, 每次调用享元对象都是一个重新计算context数据的过程
        代码变得复杂

与其他模式关系:
    1. 享元和组合: 可以用享元实现组合模式中的共享叶节点以节省内存
    2. 享元和外观: 享元展示了如何生成大量的小型对象, 外观模式则展示了如何用一个对象来代表整个子系统
    3. 享元和单例: 若能将对象的所有共享状态简化为一个享元对象, 但享元对象就是单例模式, 但两者的定义完全不同
"""
from abc import ABCMeta, abstractmethod


class Flyweight(metaclass=ABCMeta):
    """ 享元类基类 """

    @abstractmethod
    def operation(self, extrinsicState):
        pass


class FlyweightImpl(Flyweight):
    """ 享元类的具体实现类 """

    def __init__(self, color):
        self.__color = color

    def operation(self, extrinsicState):
        # extrinsicState: 外在状态
        # operation: 外在状态方法
        print("%s 取得 %s色颜料" % (extrinsicState, self.__color))


class FlyweightFactory:
    """享元工厂"""

    def __init__(self):
        self.__flyweights = {}  # 享元缓存池

    def getFlyweight(self, key):
        pigment = self.__flyweights.get(key)
        if pigment is None:
            pigment = FlyweightImpl(key)
            self.__flyweights[key] = pigment
        return pigment


def testFlyweight():
    factory = FlyweightFactory()
    print('-' * 20)
    pigmentRed = factory.getFlyweight("红")
    pigmentRed.operation("梦之队")
    print()

    print('-' * 20)
    pigmentYellow = factory.getFlyweight("黄")
    pigmentYellow.operation("梦之队")
    print()

    print('-' * 20)
    pigmentBlue1 = factory.getFlyweight("蓝")
    pigmentBlue1.operation("梦之队")
    print()

    print('-' * 20)
    pigmentBlue2 = factory.getFlyweight("蓝")
    pigmentBlue2.operation("和平队")
    print()


testFlyweight()
