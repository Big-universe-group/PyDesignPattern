""" 
模式: 外观模式
功能: 新生报告
"""


class Register:
    """报到登记"""

    def register(self, name):
        print("活动中心:%s同学报到成功！" % name)


class Payment:
    """缴费中心"""

    def pay(self, name, money):
        print("缴费中心:收到%s同学%s元付款，缴费成功！" % (name, money))


class DormitoryManagementCenter:
    """生活中心(宿舍管理中心)"""

    def provideLivingGoods(self, name):
        print("生活中心:%s同学的生活用品已发放。" % name)


class Dormitory:
    """宿舍"""

    def meetRoommate(self, name):
        print("宿    舍:" + "大家好！这是刚来的%s同学，是你们未来需要共度四年的室友！相互认识一下……" % name)


class Volunteer:
    """ 外观: 迎新志愿者 """

    def __init__(self, name):
        self.__name = name
        # 外观包含子系统所有对象
        self.__register = Register()
        self.__payment = Payment()
        self.__lifeCenter = DormitoryManagementCenter()
        self.__dormintory = Dormitory()

    def welcomeFreshmen(self, name):
        print("你好,%s同学! 我是新生报到的志愿者%s，我将带你完成整个报到流程。" % (name, self.__name))
        self.__register.register(name)
        self.__payment.pay(name, 10000)
        self.__lifeCenter.provideLivingGoods(name)
        self.__dormintory.meetRoommate(name)


def testRegister():
    print('--' * 5, '志愿者', '--' * 5)
    volunteer = Volunteer("Frank")
    print()

    print('--> 开始接待新同学:')
    volunteer.welcomeFreshmen("Tony")
    print()
    

testRegister()
