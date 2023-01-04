"""
类型: 行为模式
模式: 观察者模式(observer), 事件订阅者(Event subscriber), 监听者(Listener)
意图: 定义一种订阅模式, 在被对象(observable)的某个事件发生时通知多个注册的"observer"
使用场景:
    1. 短信或邮件通知网关
        a. 告警通知功能, 注册短信网关, 邮件网关, 企业微信网关, 根据相应的告警规则进行告警
        b. 不同的告警规则就注册了不同的网关, 每个网关就是一个观察者
    2. github上的邮件订阅通知
角色:
    发布者: publisher/observable, 被观察者, 在自身状态或特定时间发生之后向订阅者发送消息通知
    订阅者: subscriber/observer, 观察者, 包含通用接口update, 用于消息通知
    具体订阅者: concrete subscriber, 具体观察者
    客户端: client

优缺点:
    1. 优点:
        a. 开闭原则, 无需改动发布者代码就能引入新的订阅者类
        b. 在运行时建立对象之前的关系
    2. 缺点:
        a. 订阅者的通知顺序是随机的

与其他模式关系:
    责任链, 命令, 中介者, 观察者: 这四者皆用于处理sender和receiver之前的关系, 但连接方式不一样:
        a. 责任链: 按照顺序将请求动态的传递给一系列潜在接收者, 直到请求被某个接收者处理(nginx)
        b. 命令: 在sender和receiver之间建立单向连接
        c. 中介者: 清除sender和receiver之间的联系, 强制它们通过一个中介对象来进行间接沟通
        d. 观察者: receiver可以动态的接收或取消sender发送过来的请求
    
    中介者和观察者: 
        a. 中介者为了消除一系列系统之间的相互依赖, 这些组件都依赖于同一个中介对象
        b. 观察者为了在对象之间建立动态的单向连接, 使部分对象可作为其他对象的附属
        c. 有一种流行的中介者实现方式依赖于观察者:
            + 中介者对象担当发布者的角色
            + 其他组件对象担当订阅者的角色
"""
import time
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """ 观察者基类 """

    @abstractmethod
    def update(self, observable, object):
        """ 被观察者会在事件触发之后对所有的observers调用update函数 """
        pass


class Observable:
    """ 被观察者的基类 """

    def __init__(self):
        self.__observers = []  # save all observer

    def addObserver(self, observer):
        """ add new observer, 注册: 观察者基于被观察者主动register """
        self.__observers.append(observer)

    def removeObserver(self, observer):
        """ remove new observer, 取消注册 """
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        """ notify: 被观察者主动发送notify到所有的register observer """
        for o in self.__observers:
            o.update(self, object)


class AccountObservable(Observable):
    """ 被观察者实现类: 用户账户, 对于每次登录进行notify操作 """

    def __init__(self):
        super().__init__()
        self.__latestIp = {}
        self.__latestRegion = {}

    def login(self, name, ip, time):
        """ 判断此次登录的IP和上次登录IP是否一致, 若不一致则告警通知 """
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notifyObservers({"name": name, "ip": ip, "region": region, "time": time})
        self.__latestRegion[name] = region
        self.__latestIp[name] = ip

    def __getRegion(self, ip):
        # 由IP地址获取地区信息。这里只是模拟，真实项目中应该调用IP地址解析服务
        ipRegions = {
            "101.47.18.9": "浙江省杭州市",
            "67.218.147.69": "美国洛杉矶"
        }
        region = ipRegions.get(ip)
        return "" if region is None else region

    def __isLongDistance(self, name, region):
        # 计算本次登录与最近几次登录的地区差距。
        # 这里只是简单地用字符串匹配来模拟，真实的项目中应该调用地理信息相关的服务
        latestRegion = self.__latestRegion.get(name)
        return latestRegion is not None and latestRegion != region


class SmsSender(Observer):
    """ 网关: 短信发送器 """

    def update(self, observable, object):
        print("[短信发送] " + object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n" +
              "登录地区：" + object["region"] + "  登录ip：" + object["ip"] + "  登录时间：" +
              time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


class MailSender(Observer):
    """ 网关: 邮件发送器 """

    def update(self, observable, object):
        print("[邮件发送] " + object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n" +
              "登录地区：" + object["region"] + "  登录ip：" + object["ip"] + "  登录时间：" +
              time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


def testLogin():
    # 1. 对被观察者实例类注册通知网关
    print('-----------注册sms, email等observer-----------')
    accout = AccountObservable()
    accout.addObserver(SmsSender())
    accout.addObserver(MailSender())
    print()

    # 2. 在有登录的时候进行通知
    accout.login("Tony", "101.47.18.9", time.time())
    print('----------首次登录------------')
    print()

    accout.login("Tony", "67.218.147.69", time.time())
    print('----------监听到异常登录并通知------------')
    print()

    accout.login("Tony", "67.218.147.68", time.time())
    print('----------监听到异常登录并通知------------')
    print()


testLogin()
