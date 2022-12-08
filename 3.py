import datetime


class Task:
    def __init__(self, content):
        self.content = content
        time = datetime.datetime.today()
        self.data = f' Создано {str(time.replace(microsecond=0, tzinfo=None))}'

    def __repr__(self):
        return f"{self.content}: {self.data}"

    def __len__(self):
        return len(self.content)

    def __bool__(self):
        if len(self.content) > 0:
            return True
        else:
            return False


# todo_list = []
# todo_list.append(Task('Сделать домашку'))
# todo_list.append(Task('Выпить кофе'))


class TodoList:
    def __init__(self):
        self.tasks = {}

    def __repr__(self):
        return f"{list((self.tasks).values())}"

    def __getitem__(self, item):
        if 0 <= item < len(self.tasks):
            return self.tasks[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        self.tasks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")

        del self.tasks[key]


todo_lst = TodoList()
todo_lst[0] = Task('Сдать домашку')
todo_lst[1] = Task('Выпить кофе')
print(todo_lst)
#[Сдать домашку (создано 2022-12-08 12:34:33), Выпить кофе (создано 2022-12-08 12:34:33)]

print(todo_lst[0])
#Сдать домашку (создано 2022-12-08 12:34:33)

del todo_lst[0]
print(todo_lst)
#[Выпить кофе (создано 2022-12-08 12:34:33)]
