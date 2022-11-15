from todo_item import *

taskDescription = "Mow lawn"

def create_TodoItem():
  item = TodoItem(taskDescription)

  return item

def test_create_TodoItem():
  item = create_TodoItem()

  assert(item.description == taskDescription)
  assert(item.complete == False)
  assert(item.creationDate)

def test_save_TodoItem():
  item = create_TodoItem()

  result = item.save()
  assert(result == f"False|{taskDescription}")

#  assert(False)
