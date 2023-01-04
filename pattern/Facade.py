"""
类型: 结构
模式: 外观模式
意图: 其为程序库, 框架, 复杂类提供一个简单的接口
使用场景: 如果你需要一个指向复杂子系统的直接接口, 且该接口的功能有限, 则可以使用外观模式

    1. 需求: 在代码中使用某个复杂的库或框架中的众多对象, 又不想将业务代码和第三方紧密耦合
    2. 解决: 外观类为复杂子系统提供一个简单的接口, 提供部分但客户端关心的功能
    3. 例子: 上传猫咪搞笑短视频到社交媒体网站的应用可能会用到专业的视频转换库, 此时需要一个encode方法的类
        即可, 在创建该类并将其连接到适配转换库之后, 此时就创建了一个"外观类"
    4. 电话购物:
        接线员: 商店的所有服务和部门的外观, 其为你提供一个同购物,支付,送货等进行互动的简单语音接口
角色:
    外观: Facade, 提供一种访问特定子系统的便捷方式, 其了解客户端请求, 知晓一切活动部件
    附加外观: Additional Facade, 避免多种不相关的功能污染单一外观, 客户端和其他外观均可使用附加外观
    复杂子系统: Complex subsystem, 由数十个不同对象构成. 子系统类不会意识到外观的存在, 但内部可以互相通信
    客户端: Client, 使用外观代替子系统并进行调用
优缺点:
    + 将代码独立于复杂子系统
    + 外观可能成为与所有类都耦合的"上帝对象"

与其他模式关系:
    1. 适配器和外观: 
        + 外观为现有对象定义了一个新接口, 其作用域整个对象子系统上
        + 适配器会视图运用已有接口, 其只封装一个对象
    2. 工厂和外观: 当只需对客户端代码隐藏子系统创建对象的方式时, 可以用工厂代替外观
    3. 享元和外观: 
        + 享元展示了如何生成大量的小型对象
        + 外观展示了如何用一个对象代表整个子系统
    4. 中介和外观:
        + 两者都尝试在大量紧密耦合的类中进行组织以便更好的合作
        + 外观为子系统中"所有对象"定义一个简单接口, 但不提供任何新的功能, 外观对子系统透明
        + 中介将系统中的组件沟通行为中心化, 各组件都知道中介对象, 组件之间无法互相交流
    5. 外观和单例: 外观可以转为单例对象, 大部分情况下一个外观对象就够了
"""
from os import path
import logging


class ZIPModel:
    """ 子系统: ZIP模块，负责ZIP文件的压缩与解压 """

    def compress(self, srcFilePath, dstFilePath):
        print("ZIP模块正在进行'%s'文件的压缩......" % srcFilePath)
        print("文件压缩成功，已保存至'%s'" % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("ZIP模块正在进行'%s'文件的解压......" % srcFilePath)
        print("文件解压成功，已保存至'%s'" % dstFilePath)


class RARModel:
    """ 子系统: RAR模块，负责RAR文件的压缩与解压 """

    def compress(self, srcFilePath, dstFilePath):
        print("RAR模块正在进行'%s'文件的压缩......" % srcFilePath)
        print("文件压缩成功，已保存至'%s'" % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("RAR模块正在进行'%s'文件的解压......" % srcFilePath)
        print("文件解压成功，已保存至'%s'" % dstFilePath)


class ZModel:
    """ 子系统: 7Z模块，负责7Z文件的压缩与解压 """

    def compress(self, srcFilePath, dstFilePath):
        print("7Z模块正在进行'%s'文件的压缩......" % srcFilePath)
        print("文件压缩成功，已保存至'%s'" % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("7Z模块正在进行'%s'文件的解压......" % srcFilePath)
        print("文件解压成功，已保存至'%s'" % dstFilePath)


class CompressionFacade:
    """ 压缩系统的外观类: 其包含子系统所有对象 """

    def __init__(self):
        self.__zipModel = ZIPModel()
        self.__rarModel = RARModel()
        self.__zModel = ZModel()

    def compress(self, srcFilePath, dstFilePath, type):
        extName = "." + type
        fullName = dstFilePath + extName
        if (type.lower() == "zip"):
            self.__zipModel.compress(srcFilePath, fullName)
        elif (type.lower() == "rar"):
            self.__rarModel.compress(srcFilePath, fullName)
        elif (type.lower() == "7z"):
            self.__zModel.compress(srcFilePath, fullName)
        else:
            print(f"Not support this format:{type}")
            return False
        return True

    def decompress(self, srcFilePath, dstFilePath):
        baseName = path.basename(srcFilePath)
        extName = baseName.split(".")[1]
        if (extName.lower() == "zip"):
            self.__zipModel.decompress(srcFilePath, dstFilePath)
        elif (extName.lower() == "rar"):
            self.__rarModel.decompress(srcFilePath, dstFilePath)
        elif (extName.lower() == "7z"):
            self.__zModel.decompress(srcFilePath, dstFilePath)
        else:
            print(f"Not support this format {extName}:")
            return False
        return True


def testCompression():
    """ 客户端: 使用外观替代子系统, 保持客户端业务代码和第三方低耦合 """
    print('---' * 20)
    facade = CompressionFacade()
    facade.compress("/root/standard/example.md", "/root/zip/example", "zip")
    facade.decompress("/root/zip/example.zip", "/root/standard/example.md")
    print()

    print('---' * 20)
    facade.compress("/root/standard/rarfile.pdf", "/root/zip/rarfile", "rar")
    facade.decompress("/root/zip/rarfile.rar", "/root/standard/rarfile.pdf")
    print()

    print('---' * 20)
    facade.compress("/root/standard/thinking.doc", "/root/zip/thinking", "7z")
    facade.decompress("/root/zip/thinking.7z", "/root/standard/thinking.doc")
    print()


testCompression()
