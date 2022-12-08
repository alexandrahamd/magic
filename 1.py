import datetime


class Task:
    def __init__(self, content):
        self.content = content
        time = datetime.datetime.today()
        self.data = f' Создано {str(time.replace(microsecond=0, tzinfo=None))}'

    def __repr__(self):
        return f"{self.content}: {self.data}"

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.content == other.content
        else:
            NotImplemented

    def __hash__(self):
        return hash(self.content)


todo_list = set()

todo_list.add(Task('Сделать домашку'))
todo_list.add(Task('Выпить кофе'))
todo_list.add(Task('Выйти на пробежку'))
todo_list.add(Task('Сделать домашку'))

for item in todo_list:
    print(item)
