import datetime
class todoList:
    def __init__(self, Id, Tag, Memo = ' '):
        todoList.id = Id
        todoList.tag = Tag
        todoList.time = datetime.date.today()
        todoList.memo = Memo

    def match(self,filter):
        return filter in self.memo or filter in self.tag

todoList_id = 0

class Listsbook:
    def __init__(self):
        self.Lists = []

    def newList(self,Tag , Memo = ' '):
        global todoList_id
        todoList_id += 1
        newlist = todoList(todoList_id,Tag,Memo)
        self.Lists.append(newlist)
        print("一个新的日程已建立!")

    def modify(self,Listid,modifytp,modifymemo):
        for list in self.Lists:
            if Listid == list.id:
                if modifytp == 0:
                    list.memo = modifymemo
                elif modifytp == 1:
                    list.tag = modifymemo
                else:
                    print("我不明白你想修改什么？")
                break

    def search(self,filter):
        for list in self.Lists:
            list.match(filter)
        print("抱歉！没有找到相关日程！")
        return
