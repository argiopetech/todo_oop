from todo_item import *

def create_TodoItem(taskDescription):
  item = TodoItem(taskDescription)

  return item

def test_create_TodoItem(taskDescription = "Mow lawn"):
  item = create_TodoItem(taskDescription)

  assert(item.description == taskDescription)
  assert(item.complete == False)
  assert(item.creationDate)

def test_save_TodoItem(taskDescription = "Mow lawn"):
  item = create_TodoItem(taskDescription)

  result = item.save()
  assert(result == f"False|{taskDescription}")

#  assert(False)
