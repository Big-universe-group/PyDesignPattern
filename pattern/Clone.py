"""
类型: 创建型模式
模式: 原型或者克隆模式
意图: 克隆一个对象, 但是对象本身可能包含私有成员变量或者对外隐藏的实现等, 对于一些特殊的需求: 不克隆对象的
    所有数据, 每一个对象自身都有自己的极度隐秘信息(这种需求很少), 此时在python中使用deepcopy就无法达到此需求

解决办法: 采用克隆模式, 由被克隆者自身暴露克隆接口给外部, 让外部按照被克隆者的期望进行数据克隆动作
角色:
    原型: prototype, 支持克隆自身的对象, 一般克隆方法名字为: clone
    具体原型: concret prototype, 将clone方法实现的子类, 其可能还伴随的具体需求进行差异化克隆
    客户端: client, 对原型对象进行各种clone操作
    原型注册表: prototype registry, 提供一种访问常用原型的简单方法, 其中存储了一系列可随时赋值预生成对象
    预生成原型: 创建一系列不同类型的对象并进行各种配置, 后续若所需对象和预生成对象类型一致则直接克隆即可

需求: 客户端需要复制一些对象, 有希望代码独立于这些对象所述的具体类(子类)

可能场景:
    1. 若对象的子类仅仅是变化对象的初始化方式, 其他同基类保持不变, 那可以用克隆模式替换子类继承, 在基类
        中预注册多个预生成对象, 后续使用时根据需求进行克隆并返回即可.
    
优点:
    1. 克隆对象, 无需和具体类耦合
    2. 克隆预生成原型, 避免反复初始化代码
    3. 以继承以外的方式来处理多态
缺点:
    1. 克隆复杂对象时比较麻烦, 比如循环引用

其他模式:
    1. 大量使用组合模式和装饰模式的设计通常可从对于原型的使用中获益, 通过该模式来复制复杂结构
    2. 原型可用于保存命令模式的历史记录
    3. 原型可以作为备忘录模式的一个简化版本
"""
from copy import copy, deepcopy


class Clone:
    """克隆的基类"""

    def clone(self):
        """浅拷贝的方式克隆对象"""
        return copy(self)

    def deepClone(self):
        """深拷贝的方式克隆对象"""
        return deepcopy(self)


class AppConfig(Clone):
    """应用程序功能配置"""

    def __init__(self, configName):
        self.__configName = configName
        self.parseFromFile("./config/default.xml")

    def parseFromFile(self, filePath):
        """
        从配置文件中解析配置项
        真实项目中通过会将配置保存到配置文件中，保证下次开启时依然能够生效；
        这里为简单起见，不从文件中读取，以初始化的方式来模拟。
        """
        self.__fontType = "宋体"
        self.__fontSize = 14
        self.__language = "中文"
        self.__logPath = "./logs/appException.log"

    def saveToFile(self, filePath):
        """
        将配置保存到配置文件中
        这里为简单起见，不再实现
        """
        pass

    def copyConfig(self, configName):
        """创建一个配置的副本"""
        config = self.deepClone()
        config.__configName = configName
        return config

    def showInfo(self):
        print("%s 的配置信息如下：" % self.__configName)
        print("字体：", self.__fontType)
        print("字号：", self.__fontSize)
        print("语言：", self.__language)
        print("异常文件的路径：", self.__logPath)

    def setFontType(self, fontType):
        self.__fontType = fontType

    def setFontSize(self, fontSize):
        self.__fontSize = fontSize

    def setLanguage(self, language):
        self.__language = language

    def setLogPath(self, logPath):
        self.__logPath = logPath


def testAppConfig():
    print('---------初始化对象---------')
    defaultConfig = AppConfig("default")
    defaultConfig.showInfo()
    print()

    print('---------克隆对象---------')
    newConfig = defaultConfig.copyConfig("tonyConfig")
    newConfig.setFontType("雅黑")
    newConfig.setFontSize(18)
    newConfig.setLanguage("English")
    newConfig.showInfo()
    print()


testAppConfig()
