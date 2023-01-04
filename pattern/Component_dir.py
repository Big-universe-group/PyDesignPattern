import os
from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    """组件"""

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def isComposite(self):
        return False

    @abstractmethod
    def feature(self, indent):
        # indent 仅用于内容输出时的缩进
        pass


class FileDetail(Component):
    """ 叶子: 文件详情 """

    def __init__(self, name):
        super().__init__(name)
        self._size = 0

    def setSize(self, size):
        self._size = size

    def getFileSize(self):
        return self._size

    def feature(self, indent):
        # 文件大小，单位：KB，精确度：2位小数
        fileSize = round(self._size / float(1024), 2)
        print("文件名称：%s， 文件大小：%sKB" % (self._name, fileSize))


class Composite(Component):
    """ 复合组件: 容器 """

    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def addComponent(self, component):
        self._components.append(component)

    def removeComponent(self, component):
        self._components.remove(component)

    def isComposite(self):
        return True

    def feature(self, indent=""):
        indent += "\t"
        for component in self._components:
            print(indent, end="")
            component.feature(indent)


class FolderDetail(Composite):
    """ 复杂组件: 文件夹详情 """

    def __init__(self, name):
        super().__init__(name)
        self._count = 0

    def setCount(self, fileNum):
        self._count = fileNum

    def getCount(self):
        return self._count

    def feature(self, indent=''):
        print("文件夹名：%s， 文件数量：%d。包含的文件：" % (self._name, self._count))
        super().feature(indent)


def scanDir(rootPath, folderDetail):
    """ 扫描某一文件夹下的所有目录
        1. 将文件实例化为叶子并添加到目录组件类中
        2. 递归添加复杂组件
    """
    if not os.path.isdir(rootPath):
        raise ValueError("rootPath不是有效的路径：%s" % rootPath)

    if folderDetail is None:
        raise ValueError("folderDetail不能为空!")

    fileNames = os.listdir(rootPath)
    for fileName in fileNames:
        filePath = os.path.join(rootPath, fileName)
        if os.path.isdir(filePath):
            folder = FolderDetail(fileName)
            scanDir(filePath, folder)
            folderDetail.addComponent(folder)
        else:
            fileDetail = FileDetail(fileName)
            fileDetail.setSize(os.path.getsize(filePath))
            folderDetail.addComponent(fileDetail)
            folderDetail.setCount(folderDetail.getCount() + 1)


def testDir():
    folder, _dir = FolderDetail("pattern"), os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    scanDir(_dir, folder)
    folder.feature("")


testDir()
