import unittest


class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = TodoList()

    def test_add_task(self):
        self.todo_list.add_task("Buy groceries")
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0].description, "Buy groceries")

    def test_view_tasks(self):
        self.todo_list.add_task("Buy groceries")
        self.todo_list.add_task("Do laundry")
        self.assertEqual(self.todo_list.view_tasks(), ["Buy groceries", "Do laundry"])

    def test_mark_task_as_completed(self):
        self.todo_list.add_task("Buy groceries")
        self.todo_list.add_task("Do laundry")
        self.todo_list.mark_task_as_completed(0)
        self.assertTrue(self.todo_list.tasks[0].completed)


if __name__ == '__main__':
    unittest.main()


class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def view_tasks(self):
        return [task.description for task in self.tasks]

    def mark_task_as_completed(self, index):
        self.tasks[index].completed = True
