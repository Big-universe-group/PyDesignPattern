from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """观察者的基类: 其可以是任何子类型, 但其必须有一个update函数, 被观察者会在事件触发之后对所有的
        observers调用update函数
    @注册: 观察者基于被观察者主动register
    @notify: 被观察者主动发送notify到所有的register observer中
    @使用场景:
        例如告警通知功能, 注册短信网关, 邮件网关, 企业微信网关, 在有需要告警信息时, 根据相应的告警规则进行
        告警通知.
        不同的告警规则就注册了不同的网关(观察者)
    """

    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    """被观察者的基类"""

    def __init__(self):
        self.__observers = []  # save all observer

    def addObserver(self, observer):
        """ add new observer """
        self.__observers.append(observer)

    def removeObserver(self, observer):
        """ remove new observer """
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)


class WaterHeater(Observable):
    """热水器：战胜寒冬的有利武器"""

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("当前温度是：" + str(self.__temperature) + "℃")
        self.notifyObservers()


class WashingMode(Observer):
    """该模式用于洗澡用"""

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) \
                and observable.getTemperature() >= 50 and observable.getTemperature() < 70:
            print("水已烧好！温度正好，可以用来洗澡了。")


class DrinkingMode(Observer):
    "该模式用于饮用"

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("水已烧开！可以用来饮用了。")


def testWaterHeater():
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)


testWaterHeater()
