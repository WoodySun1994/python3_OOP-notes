import sys
from Todolist import todoList,Listsbook

class Menu:
    def __init__(self):
        self.listsbook = Listsbook()
        self.choices = {
            "1": self.show_lists,
            "2": self.new_lists,
            "3": self.search_lists,
            "4": self.modify_lists,
            "5": self.quit
        }

    def show_menu(self):
        print(
            '''
            "1": 显示日程表
            "2": 新建日程
            "3": 按tag查找日程
            "4": 修改日程
            "5": 退出应用
            '''
        )

    def run(self):
        while True:
            self.show_menu()
            choice = input("请输入你的选择：")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0}并不是一个正确的输入!".format(choice))

    def show_lists(self):
        for List in self.listsbook.Lists:
            print(List.id)
            print(List.time)
            print('|' + List.tag + '|   ' + List.memo)
            print('\n')

    def search_lists(self):
        searchmemo = input("请输入查找内容：")
        self.listsbook.search(searchmemo)

    def new_lists(self):
        newtag = input("请输入该日程的标签：")
        newmemo = input("请输入日程内容：")
        self.listsbook.newList(newtag,newmemo)

    def modify_lists(self):
        modid = input("需要修改的日程id:")
        modtype = input("请确定要修改的类型：Memo(0)/Tag(1)")
        modmemo = input("修改后的内容：")
        self.listsbook.modify(modid,modtype,modmemo)

    def quit(self):
        print("欢迎使用todoList日程表！")
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()
