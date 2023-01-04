"""
类型: 结构性
模式: 装饰者,装饰器,wrapper,decorator
意图: 通过将对象A放入包含行为的特殊封装对象中来为原有的对象A绑定新的行为
使用场景:
    1. 在不更改已有代码的前提下使用对象, 并且为对象增加额外的行为, 则可以使用装饰模式(有点类似适配器)
    2. 使用装饰类能将业务逻辑组织成层次结构, 优化代码层次感

新的解决思路:
    当需要更改一个对象的行为时, 最常用的思路就是扩展原有类, 但是继承本身拥有如下缺点:
        + 继承是静态的, 在运行时阶段只能由子类对象来实现而无法动态的的包装原有对象
        + 子类仅有一个父类, 大部分编程语言不允许多继承(python可以)
        
    聚合和组合: 新对象包含对象A的引用, 新对象将工作委派给引用对象, 这是很多设计模式背后的关键原则, 通过
        聚合可以让一个对象使用多个类行为, 并将工作委派给其中的各个引用对象

    继承和聚合对比:

角色:
    部件: Component, 声明封装器和被封装对象的公共接口
    具体部件: Concrete Component, 被封装对象所属的类, 其中定义了基础行为, 装饰类可以改变这些行为
    基础装饰: Base Decorator, 该类拥有一个指向部件的引用成员变量, 从而可以引用具体的部件和装饰
    具体装饰: Concrete Decorator, 定义可动态添加到部件的额外行为, 重写基类方法已提供额外的行为
    客户端: Client, 调用装饰类和部件, 可以使用多层装饰来封装某一个部件

优缺点:
    优点: 
        + 无需创建新子类即可扩展对象行为
        + 在运行时添加或者删除对象功能
        + 用多个装饰封装对象来组合复杂行为: 一个人可以传多件衣服或装饰
        + SRP原则
    缺点:
        + 封装器栈中删除特定封装器比较困难
        + 若想要实现行为不受装饰器栈顺序影响的功能则比较困难
        + 各层的初始化配置代码比较糟糕

与其他模式关系:
    1. 适配器和装饰器: 
        a. 适配器模式可以对已有对象的接口进行修改, 装饰模式则能在不改变对象接口的前提下强化对象功能
        b. 装饰器可以多层包装组合, 这是适配器不能达到的目的
    2. 适配器, 代理模式, 装饰器:
        a. 适配器能为被封装对象提供不同的接口
        b. 代理模式能为对象提供相同的接口
        c. 装饰则能为对象提供加强的接口
    3. 责任链和装饰器: 责任链的管理者可以相互独立地执行一切操作, 还可以随时停止传递请求, 装饰器则不能做到
    4. 组合模式和装饰器: 
        a. 两者都依赖递归组合来组织无限数量的对象
        b. 装饰器类似组合, 但只有一个子组件
        c. 装饰为被封装对象添加了额外的职责, 组合仅对其子节点的结果进行了求和
    5. 代理模式和装饰器:
        a. 两者都基于组合原则, 即一个对象应该将部分工作委派给另一个对象
        b. 代理通常自行管理其服务对象的生命周期, 装饰的生成则总是由客户端进行控制
    6. 模式合作:
        a. 装饰可让你更改对象的外表, 策略模式则让你能够改变其本质
"""
from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    """人"""

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def wear(self):
        print("着装：")


class Engineer(Person):
    """工程师"""

    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    def getSkill(self):
        return self.__skill

    def wear(self):
        print("我是 " + self.getSkill() + "工程师 " + self._name, end="， ")
        super().wear()


class Teacher(Person):
    """教师"""

    def __init__(self, name, title):
        super().__init__(name)
        self.__title = title

    def getTitle(self):
        return self.__title

    def wear(self):
        print("我是 " + self._name + self.getTitle(), end="， ")
        super().wear()


class ClothingDecorator(Person):
    """ 服装装饰器的基类: 对人的包装
    note: 子类可以引用任何该类的其他子类
    note2: 一个具体部件外面可以包裹多个装饰类, 每一个装饰类都是ClothingDecorator子类
    """

    def __init__(self, person):
        self._decorated = person

    def wear(self):
        self._decorated.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass


class CasualPantDecorator(ClothingDecorator):
    """休闲裤装饰器"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一条卡其色休闲裤")


class BeltDecorator(ClothingDecorator):
    """腰带装饰器"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一条银色针扣头的黑色腰带")


class LeatherShoesDecorator(ClothingDecorator):
    """皮鞋装饰器"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一双深色休闲皮鞋")


class KnittedSweaterDecorator(ClothingDecorator):
    """针织毛衣装饰器"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一件紫红色针织毛衣")


class WhiteShirtDecorator(ClothingDecorator):
    """白色衬衫装饰器"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一件白色衬衫")


class GlassesDecorator(ClothingDecorator):
    """眼镜装饰器"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一副方形黑框眼镜")


def testDecorator():
    print('-' * 5, 'Person', '-' * 5)
    tony = Engineer("Tony", "客户端")
    tony.wear()
    print()

    print('-' * 5, 'PersonDecorator', '-' * 5)
    pant = CasualPantDecorator(tony)
    belt = BeltDecorator(pant)
    shoes = LeatherShoesDecorator(belt)
    shirt = WhiteShirtDecorator(shoes)
    sweater = KnittedSweaterDecorator(shirt)
    glasses = GlassesDecorator(sweater)
    glasses.wear()
    print()

    print('-' * 5, 'Person', '-' * 5)
    wells = Teacher("wells", "教授")
    tony.wear()
    print()

    print('-' * 5, 'PersonDecorator', '-' * 5)
    ws = WhiteShirtDecorator(LeatherShoesDecorator(wells))
    decorateTeacher = GlassesDecorator(ws)
    decorateTeacher.wear()


testDecorator()
