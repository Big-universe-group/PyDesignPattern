class Customer:
    """ 集合中元素: 迭代器中集合的元素实例类 """

    def __init__(self, name):
        self.__name = name
        self.__num = 0
        self.__clinics = None

    def getName(self):
        return self.__name

    def register(self, system):
        system.pushCustomer(self)

    def setNum(self, num):
        self.__num = num

    def getNum(self):
        return self.__num

    def setClinic(self, clinic):
        self.__clinics = clinic

    def getClinic(self):
        return self.__clinics


class NumeralIterator:
    """ 具体迭代器: 实现某一种特定的遍历算法 """

    def __init__(self, data):
        self.__data = data
        self.__curIdx = -1

    def next(self):
        """移动至下一个元素"""
        if (self.__curIdx < len(self.__data) - 1):
            self.__curIdx += 1
            return True
        else:
            return False

    def current(self):
        """获取当前的元素"""
        return self.__data[self.__curIdx] if (
            self.__curIdx < len(self.__data) and self.__curIdx >= 0) else None


class NumeralSystem:
    """ 集合或具体集合: 排号系统 """

    __clinics = ("1号分诊室", "2号分诊室", "3号分诊室")

    def __init__(self, name):
        self.__customers = []
        self.__curNum = 0
        self.__name = name

    def pushCustomer(self, customer):
        customer.setNum(self.__curNum + 1)
        click = NumeralSystem.__clinics[self.__curNum % len(NumeralSystem.__clinics)]
        customer.setClinic(click)
        self.__curNum += 1
        self.__customers.append(customer)
        print("%s 您好！您已在%s成功挂号，序号：%04d，请耐心等待！"
              % (customer.getName(), self.__name, customer.getNum()))

    def getIterator(self):
        # 迭代器, 对当前集合实例进行遍历
        return NumeralIterator(self.__customers)

    def visit(self):
        for customer in self.__customers:
            print("下一位病人 %04d(%s) 请到 %s 就诊。"
                  % (customer.getNum(), customer.getName(), customer.getClinic()))


def testHospital():
    """ 客户端 """
    print('---------生成集合并往集合中推入待遍历的元素--------')
    numeralSystem = NumeralSystem("挂号台")
    for name in ('Lily', 'Pony', 'Nick', 'Tony', 'feng'):
        Customer(name).register(numeralSystem)
    print()

    print('---------遍历集合--------')
    iterator = numeralSystem.getIterator()
    while (iterator.next()):
        customer = iterator.current()
        print("下一位病人 %04d(%s) 请到 %s 就诊。" % (
            customer.getNum(), customer.getName(), customer.getClinic()))
    print()


testHospital()
