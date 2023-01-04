""" 升高介绍
客户期待得到的接口: 姓名, 升高, 外观
需要适配的Adaptee类: ShortPerson, 这应该不算适配而是一种美化包装, 怎么有点强行关联的意味
适配器Adapter类: DecoratePerson, 相比AdapterSocket是两种实现方式, 这里使用多继承, 后者使用实例依赖方式实现
"""
from abc import ABCMeta, abstractmethod

class IHightPerson(metaclass=ABCMeta):
    """接口类，提供空实现的方法，由子类去实现"""

    @abstractmethod
    def getName(self):
        """获取姓名"""
        pass

    @abstractmethod
    def getHeight(self):
        """获取身高"""
        pass

    @abstractmethod
    def appearance(self, person):
        """外貌"""
        pass


class HighPerson(IHightPerson):
    """个高的人"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getHeight(self):
        return 170

    def appearance(self):
        print(self.getName() + "身高" + str(self.getHeight()) + "，完美如你，天生的美女！")


class ShortPerson:
    """个矮的人"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getRealHeight(self):
        return 160

    def getShoesHeight(self):
        return 6


class DecoratePerson(ShortPerson, IHightPerson):
    """有高跟鞋搭配的人"""

    def __init__(self, name):
        super().__init__(name)

    def getName(self):
        return super().getName()

    def getHeight(self):
        return super().getRealHeight() + super().getShoesHeight()

    def appearance(self):
        print(self.getName() + "身高" + str(self.getHeight()) + ", 在高跟鞋的适配下，你身高不输高圆圆，气质不输范冰冰！")


class HeightMatch:
    """身高匹配"""

    def __init__(self, person):
        self.__person = person

    def matching(self, person1):
        """假设标准身高差为10厘米内"""
        distance = abs(self.__person.getHeight() - person1.getHeight())
        isMatch = distance <= 10
        print(self.__person.getName() + "和" + person1.getName() + "是否为情侣的标准身高差：" +
              ("是" if isMatch else "否") + ", 差值：" + str(distance))


class Hotel:
    """(高级)酒店"""

    def recruit(self, person):
        """
        :param person: IHightPerson的对象
        """
        suitable = self.receptionistSuitable(person)
        print(person.getName() + "是否适合做接待员：", "符合" if suitable else "不符合")

    def receptionistSuitable(self, person):
        """
        是否可以成为(高级酒店)接待员
        :param person: IHightPerson的对象
        :return: 是否符合做接待员的条件
        """
        return person.getHeight() >= 165


def testPerson():
    print('----------------客户期望-------------')
    lira = HighPerson("Lira")
    lira.appearance()
    print('----------------封装后-------------')
    demi = DecoratePerson("Demi")
    demi.appearance()

    print('----------------封装后的其他操作: 情侣比较-------------')
    haigerMatching = HeightMatch(HighPerson("Haiger"))
    haigerMatching.matching(lira)
    haigerMatching.matching(demi)

    print('----------------封装后的其他操作: 酒店登记-------------')
    hotel = Hotel()
    hotel.recruit(lira)
    hotel.recruit(demi)

testPerson()
