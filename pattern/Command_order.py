from abc import ABCMeta, abstractmethod

class Chef():
    """ receiver: 厨师 """

    def steamFood(self, originalMaterial):
        print("receiver: %s清蒸中..." % originalMaterial)
        return "清蒸" + originalMaterial

    def stirFriedFood(self, originalMaterial):
        print("receiver: %s爆炒中..." % originalMaterial)
        return "香辣炒" + originalMaterial


class Order(metaclass=ABCMeta):
    """ 命令: 订单 """

    def __init__(self, name, originalMaterial):
        self._chef = Chef()  # 厨师对象
        self._name = name  # 订单类型
        self._originalMaterial = originalMaterial  # 具体菜名

    def getDisplayName(self):
        return self._name + self._originalMaterial

    @abstractmethod
    def processingOrder(self):
        pass


class SteamedOrder(Order):
    """ 具体命令: 清蒸 """

    def __init__(self, originalMaterial):
        super().__init__("清蒸", originalMaterial)

    def processingOrder(self):
        if (self._chef is not None):
            return self._chef.steamFood(self._originalMaterial)
        return ""


class SpicyOrder(Order):
    """ 具体命令: 香辣炒 """

    def __init__(self, originalMaterial):
        super().__init__("香辣炒", originalMaterial)

    def processingOrder(self):
        if (self._chef is not None):
            return self._chef.stirFriedFood(self._originalMaterial)
        return ""


class Waiter:
    """ 中介客户端: 服务员 """

    def __init__(self, name):
        self.__name = name
        self.__order = None

    def receiveOrder(self, order):
        # 订单: 这里传给中介客户端的已经是关联后的命令
        self.__order = order
        print("服务员%s：您的 %s 订单已经收到,请耐心等待" % (self.__name, order.getDisplayName()))

    def placeOrder(self):
        # 做菜: 基于中介客户端来操作命令对象, 向接受者发送指令
        food = self.__order.processingOrder()
        print("服务员%s：您的餐 %s 已经准备好，请您慢用!" % (self.__name, food))


def testOrder():
    """ 客户端 """
    print('-----------------order: steame----------------')
    waiter = Waiter("Anna")
    steamedOrder = SteamedOrder("大闸蟹")
    print("客户David：我要一份 %s" % steamedOrder.getDisplayName())
    waiter.receiveOrder(steamedOrder)
    waiter.placeOrder()
    print()

    print('-----------------order: spicy----------------')
    spicyOrder = SpicyOrder("大闸蟹")
    print("客户Tony：我要一份 %s" % spicyOrder.getDisplayName())
    waiter.receiveOrder(spicyOrder)
    waiter.placeOrder()


testOrder()
