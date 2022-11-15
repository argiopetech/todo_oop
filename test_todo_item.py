from todo_item import *

def test_create_TodoItem(taskDescription = "Mow lawn"):
  item = TodoItem(taskDescription)

  assert(item.description == taskDescription)
  assert(item.complete == False)
  assert(item.creationDate)


def test_save_TodoItem(taskDescription = "Mow lawn"):
  item = TodoItem(taskDescription)

  result = item.save()
  assert(result == f"False|{taskDescription}")

  item.markComplete()
  result = item.save()
  assert(result == f"True|{taskDescription}")


def test_other_tasks():
  taskList = ["Task 1", "Task 2", "Task 3"]

  for task in taskList:
    test_create_TodoItem(task)
    test_save_TodoItem(task)


def test_task_completion(taskDescription = "Mow lawn"):
  item = TodoItem(taskDescription)

  assert(item.complete == False)

  item.markComplete()

  assert(item.complete == True)


def test_empty_todo():
  try:
    TodoItem("")
  except ValueError:
    return

  assert(False)


def test_load_todo():
  def doTest(taskDescription = "Mow lawn"):
    item = TodoItem(taskDescription)

    loadedItem = TodoItem.load(item.save())

    assert(item == loadedItem)

    item.markComplete()

    loadedItem = TodoItem.load(item.save())

    assert(item == loadedItem)

  doTest()
