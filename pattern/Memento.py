"""
类型: 行为模式
模式: 快照(snapshot), 备忘录(memento)
意图: 其允许在不暴露对象实现细节的情况下保存和恢复对象之前的状态
使用场景:
    1. 通用场景:
        a. 比如文字编辑器应用程序的撤销功能
        b. 某些场景下的回滚逻辑(这个非常普遍), 实现一种逻辑上的原子性
    2. 普通实现方式: 
        程序对所有的操作进行记录并保存, 当用户需要撤销某个操作时就从历史记录中加载上一次的状态
    3. 问题: 
        a. 没有一个合理的结构, 则最终会在一个类中存储所有的状态, 一旦增加或删除某个变量时会有大量的改动,
        b. 若涉及到公共变量和私有变量则影响更大.
    4. 解决方案:
        a. 将创建snapshot的工作委派给实际状态的拥有者(原发器,originator)对象, 让其自行生成快照
        b. 原发器拥有memeto备忘录的完全/完全访问权限, 负责人只能访问meta元数据
        c. 负责人仅仅通过受限接口与备忘录进行交互
    5. 实现方式:
        a. 基于嵌套类
        b. 不基于嵌套类
角色:
    原发器: Originator, 类可以生成自身状态的快照, 也可以在需要的时候恢复自身状态, 其通过实例化
            备忘录来保存自身状态
    备忘录: Memento, 原发器自身状态快照的value object, 一般该对象都是不可变对象
    负责人: Caretaker, 其直到"何时"记录原发器状态, "为何"记录原发器状态, "何时"恢复状态.
            负责人通过保存memento stack来表示历史记录, 当需要回缩的时候, 负责人会获取栈顶部的备忘录并传递
            给originator以进行状态的恢复.

优缺点:
    优点:
        a. 在不破坏对象封装前提下创建对象快照
        b. 让负责人来维护历史记录以简化原发器的代码
    缺点:
        a. 若频繁创建备忘录, 则内存消耗过大
        b. 负责人需要完整跟踪原发器的生命周期, 以便及时消费备忘录, 避免内存泄漏

与其他模式关系:
    备忘和命令: 同时使用这两个模式来实现撤销功能, 其中命令对目标对象执行不同的操作, 备忘录则保存一条条命令,
            类似mysql的binlog
    备忘和迭代: 保存迭代器的状态, 以便迭代回滚
"""
from copy import deepcopy


class Memento:
    """ 备忘录: 不可变对象 """

    def setAttributes(self, dt):
        """深度拷贝字典dict中的所有属性"""
        self.__dict__ = deepcopy(dt)

    def getAttributes(self):
        """获取属性字典"""
        return self.__dict__


class Caretaker:
    """ 负责人: 备忘录管理类 """

    def __init__(self):
        self._mementos = {}  # 历史记录

    def addMemento(self, name, memento):
        self._mementos[name] = memento

    def getMemento(self, name):
        return self._mementos[name]


class Originator:
    """ 原发器: 备份发起人"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_owner(self, meme):
        print(f'当前状态:{meme.name}, 年龄:{meme.age}')

    def update_owner(self, name, age):
        self.name = name
        self.age = age

    def createMemento(self):
        memento = Memento()
        memento.setAttributes(self.__dict__)
        return memento

    def restoreFromMemento(self, memento):
        self.__dict__.update(memento.getAttributes())


def test_snapshot():
    # 1. 初始化原发器和负责人
    orig = Originator('bifeng', 18)
    taker = Caretaker()

    # 2. 保存此次的snapshot并放入栈中
    meme = orig.createMemento()
    taker.addMemento('first_owner', meme)
    
    # 3. 更新owner并保存
    orig.update_owner('xiaoyuan', 19)
    meme = orig.createMemento()
    taker.addMemento('second_owner', meme)

    # 4. 打印记录
    print('-----------first owner-----------')
    orig.display_owner(taker.getMemento('first_owner'))
    print()

    print('-----------second owner-----------')
    orig.display_owner(taker.getMemento('second_owner'))
    print()


test_snapshot()
