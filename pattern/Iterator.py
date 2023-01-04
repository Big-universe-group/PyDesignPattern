"""
类型: 行为设计模式
模式: 迭代器模式
意图: 在不暴露底层表现形式的情况下遍历集合中的所有元素
角色:
    迭代器: Iterator, 声明遍历集合的操作: 获取下一个元素, 获取当前位置, 重新开始迭代
    具体迭代器: Concrete Iterators, 实现遍历集合的某一个特定算法
    集合: Collection, 声明一个或多个方法来获取与集合兼容的迭代器
    具体集合: Concrete Collection, 在客户端请求迭代器时返回一个特定的具体迭代器类实体
    客户端: Client

与其他类型关系:
    + 备忘录和迭代器: 同时使用备忘录和迭代器来获取当前迭代器的状态, 并在需要的时候进行回滚  
    + 访问者和迭代器: 同时使用以用来遍历复杂数据结构, 并对其中的元素执行所需操作
"""


class BaseIterator:
    """ 迭代器, 这里也同时是具体迭代器 """

    def __init__(self, data):
        self.__data = data
        self.toBegin()

    def toBegin(self):
        """将指针移至起始位置"""
        self.__curIdx = -1

    def toEnd(self):
        """将指针移至结尾位置"""
        self.__curIdx = len(self.__data)

    def next(self):
        """移动至下一个元素"""
        if (self.__curIdx < len(self.__data) - 1):
            self.__curIdx += 1
            return True
        else:
            return False

    def previous(self):
        "移动至上一个元素"
        if (self.__curIdx > 0):
            self.__curIdx -= 1
            return True
        else:
            return False

    def current(self):
        """获取当前的元素"""
        if (self.__curIdx < len(self.__data) and self.__curIdx >= 0):
            return self.__data[self.__curIdx]
        return None


def testBaseIterator():
    """ 客户端使用 """
    print("----从前往后遍历----")
    setobj = range(0, 10)  # 待遍历集合信息
    iterator = BaseIterator(setobj)
    while (iterator.next()):
        customer = iterator.current()
        print(customer, end="\t")
    print()

    print("----从后往前遍历----")
    iterator.toEnd()
    while (iterator.previous()):
        customer = iterator.current()
        print(customer, end="\t")
    print()


testBaseIterator()
