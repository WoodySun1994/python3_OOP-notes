```python
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
            choice = self.choices.get(choice)
            if choice:
                choice
            else:
                print("{0}并不是一个正确的输入!".format(choice))

    def show_lists(self):
        pass

    def search_lists(self):
        pass
    def new_lists(self):
        pass
    def modify_lists(self):
        pass
    def quit(self):
        pass

if __name__ == '__main__':
    Menu().run()
```
