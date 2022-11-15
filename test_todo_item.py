from todo_item import *

def test_create_TodoItem():
  taskDescription = "Mow lawn"

  item = TodoItem(taskDescription)

  assert(item.description == taskDescription)
  assert(item.complete == False)
  assert(item.creationDate)
