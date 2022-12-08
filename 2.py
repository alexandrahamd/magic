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


todo_list = []

todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))

non_empty_tasks = [item for item in todo_list if item]
print(non_empty_tasks)
#[Сделать домашку (создано 2022-12-08 12:21:16), Сделать домашку (создано 2022-12-08 12:21:16)]

print(len([item for item in todo_list if not item]))
#2
