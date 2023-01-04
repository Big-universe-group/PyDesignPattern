class Engineer:
    """ 原发器: 工程师 """

    def __init__(self, name):
        self.__name = name
        self.__workItems = []

    def addWorkItem(self, item):
        self.__workItems.append(item)

    def forget(self):
        self.__workItems.clear()
        print(self.__name + "工作太忙了，都忘记要做什么了！")

    def writeTodoList(self):
        """将工作项记录TodoList"""
        todoList = TodoList()
        for item in self.__workItems:
            todoList.writeWorkItem(item)
        return todoList

    def retrospect(self, todoList):
        """回忆工作项"""
        self.__workItems = todoList.getWorkItems()
        print(self.__name + "想起要做什么了！")

    def showWorkItem(self):
        if self.__workItems:
            print(self.__name + "的工作项：")
            for idx in range(0, len(self.__workItems)):
                print(str(idx + 1) + ". " + self.__workItems[idx] + ";")
        else:
            print(self.__name + "暂无工作项！")


class TodoList:
    """ 备忘录: 某一个时间段的工作项 """

    def __init__(self):
        self.__workItems = []

    def writeWorkItem(self, item):
        self.__workItems.append(item)

    def getWorkItems(self):
        return self.__workItems


class TodoListCaretaker:
    """ 负责人: TodoList管理类 """

    def __init__(self):
        self.__todoList = None

    def setTodoList(self, todoList):
        self.__todoList = todoList

    def getTodoList(self):
        return self.__todoList


def testEngineer():
    # 1. 原发器-工程师
    tony = Engineer("Tony")
    tony.addWorkItem("解决线上部分用户因昵称太长而无法显示全的问题")
    tony.addWorkItem("完成PDF的解析")
    tony.addWorkItem("在阅读器中显示PDF第一页的内容")

    print('--------工程师当前待办工作事项-------')
    tony.showWorkItem()
    print()

    # 2. 负责人-存储此时的待办事项
    caretaker = TodoListCaretaker()
    caretaker.setTodoList(tony.writeTodoList())

    # 3. 工程师遗忘了
    print('--------工程师遗忘所有事项-------')
    tony.forget()
    tony.showWorkItem()
    print()

    # 4. 重载
    print('--------重载之前保存的事项-------')
    tony.retrospect(caretaker.getTodoList())
    tony.showWorkItem()
    print()


testEngineer()
