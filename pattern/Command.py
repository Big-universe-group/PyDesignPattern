"""
类型: 行为型
模式: 命令行模式
意图: 将请求转换为一个包含与请求相关的所有信息的独立对象, 
    1. 需求:
        开发一个文字编辑器, 创建一个包含多个按钮的工具栏, 每一个按钮对应编辑器的不同操作
    2. 问题
         + 每一个按钮创建相应子类, 子类会在按钮点击后执行相应的功能代码, 一旦某天基类发生变动则需要改动子类
         + 若存在多个类需要复用某个功能时, 那么此时可以在这些类和基类之间创建新的基类, 二级结构变为三级结构,
            但是, 若A, B, C类复用功能a, 而B, E, F类复用功能b, 那么此时该如何呢? 这明显无法用类继承来实现
    3. 发送请求: 一个对象调用另外一个对象并传递参数, 这个过程被称为一个对象向另外一个对象发送请求
    4. 解决办法:
        + 关注点分离, 对软件分层, 用户图形界面GUI层, 业务处理逻辑层, 其中GUI对象会传递参数来调用某一个业务对象
        + 在GUI和业务层之间抽离中命令类, 包含请求的所有细节(调用对象, 方法名, 参数列表等)
        + 命令类相当于一层代理, GUI不知道业务层的所有细节, GUI只要触发命令即可, 命令对象会处理所有细节工作
        
        注意, 这里有点类似桥接模式

使用场景:
    1. 编辑器, GUI菜单类和具体的实现, 更甚者, 一些操作需要先放入队列中再远程执行, 这时更应该使用命令模式
    2. 餐厅点餐, 服务员在菜单上记录需要的食物, 厨师根据菜单进行制作, 其中菜单就是命令对象
    3. 撤销和回滚操作, 这是命令模式最常见的用法(有点类似mysql的binlog逻辑, 将一条条sql语句记录下来以便恢复),
        + 每一个命令历史记录: 包含已执行命令对象和栈数据信息
        + 缺点: 实现比较难, 栈数据占用大量内存

角色:
    发送者或触发者: Sender/Invoker, 负责对请求初始化, 其中包含对命令变量的引用, 通过set函数进行关联引用
    命令: Command, 声明执行命令的方法
    具体命令: ConcreteCommand, 实现各种类型的请求, 并将请求委派给业务逻辑对象, 其包含对invoker的引用
    接受者: Receiver, 业务逻辑代码
    客户端: Client, 创建具体命令对象并将接受者和命令绑定, 之后生成的命令就可以和发送者关联并继续交互

优缺点:
    优点: 
         + 单一职责原则, 解耦触发和执行操作
         + 开闭原则, 在不修改已有客户端代码情况下创建新的命令
         + 撤销功能; 延时执行功能; 根据简单命令组合成一个复杂命令
    缺点:
        + 代码更加复杂

其他模式:
    1. 发送者和接收者的通信: 命令模式, 中介者模式, 观察者模式, 责任链模式都可以实现, 只不过方式不一样

        + 责任链: 按照顺序将请求动态传递给一系列的潜在接收者, 直到其中一个接收者处理, 防火墙的规则处理
        + 命令: 发送者和接收之间单向连接处理
        + 中介者: 强制插入中介对象, 在发送者和接收者之间插入一座海关口
        + 观察者: 允许receiver动态的sub/unsub接收者发过来的请求

    2. 命令模式和策略模式: 两者都通过某行为来参数化对象
        + 命令模式: 将任何操作(需求)转为对象, 操作相关的参数则作为对象成员, 可以通过命令模式达到延时操作,
            远程发送命令, 保存历史等等各种转换逻辑
        + 策略模式: 用于描述完全某件事的不同方式, 从而在相同的上下文中使用不同的策略来做一件事情

    3. 命令模式和原型模式: 原型/克隆模式也可以用于保存命令的历史记录
    4. 访问者模式: 这一般视为命令模式的加强版本, 访问者模式可以对不同类的多种对象执行操作
"""
from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    """ 命令的抽象类 """

    @abstractmethod
    def execute(self):
        """ 声明命令执行的方法 """
        pass


class CommandImpl(Command):
    """ 命令的具体实现类 """

    def __init__(self, receiver):
        # 将接受者和具体命令关联
        self.__receiver = receiver

    def execute(self):
        # 发送信息
        print('Command: ready execute special method...')
        self.__receiver.doSomething()


class Receiver:
    """ 命令的接收者 """

    def doSomething(self):
        print("Receiver: do something...")


class Invoker:
    """ 调度者 """

    def __init__(self):
        self.__command = None

    def setCommand(self, command):
        self.__command = command

    def action(self):
        if self.__command is not None:
            print('Invoker: ready send request to Command...')
            self.__command.execute()


def client():
    invoker = Invoker()
    command = CommandImpl(Receiver())
    invoker.setCommand(command)
    invoker.action()


client()
