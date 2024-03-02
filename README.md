# Изисквания:

1. Приложението трябва да има възможност за добавяне на задачи.
2. Потребителите трябва да могат да виждат списък с всички добавени задачи.
3. Потребителите трябва да могат да маркират задачите като завършени.

# Какво се променя:

# Създаване на тестове за функционалността за добавяне на задачи:

``` Python
def test_add_task():
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0].description == "Buy groceries"
```

# Създаване на функционалност за добавяне на задачи:

``` Python
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))
```

# Създаване на тестове за функционалността за преглед на списъка със задачи:

``` Python
def test_view_tasks():
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Do laundry")
    assert todo_list.view_tasks() == ["Buy groceries", "Do laundry"]
```
# Създаване на функционалност за преглед на списъка със задачи:

``` Python
class TodoList:
    def view_tasks(self):
        return [task.description for task in self.tasks]

```
# Създаване на тестове за функционалността за маркиране на задача като завършена:
``` Python
def test_mark_task_as_completed():
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Do laundry")
    todo_list.mark_task_as_completed(0)
    assert todo_list.tasks[0].completed == True
```
# Създаване на функционалност за маркиране на задача като завършена:
``` Python
class TodoList:
    def mark_task_as_completed(self, index):
        self.tasks[index].completed = True
```
