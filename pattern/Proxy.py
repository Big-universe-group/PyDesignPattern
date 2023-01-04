"""
类型: 行为模式
模式: 观察者模式(observer), 事件订阅者(Event subscriber), 监听者(Listener)
意图: 定义一种订阅模式, 在被对象(observable)的某个事件发生时通知多个注册的"observer"
使用场景:
角色:

优缺点:

与其他模式关系:
"""
from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    """ 主题类 """

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def requestx(self, content=''):
        pass


class RealSubject(Subject):
    """ 真实主题类 """

    def requestx(self, content=''):
        print("RealSubject todo something...")


class ProxySubject(Subject):
    """ 代理主题类 """

    def __init__(self, name, subject):
        super().__init__(name)
        self._realSubject = subject

    def requestx(self, content=''):
        self.preRequest()
        if (self._realSubject is not None):
            self._realSubject.requestx(content)
        self.afterRequest()

    def preRequest(self):
        print("preRequest")

    def afterRequest(self):
        print("afterRequest")


def testProxy():
    realObj = RealSubject('RealSubject')
    proxyObj = ProxySubject('ProxySubject', realObj)
    proxyObj.requestx()


testProxy()
