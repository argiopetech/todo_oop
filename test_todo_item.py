from todo_item import *

taskDescription = "Mow lawn"

def test_create_TodoItem():

  item = TodoItem(taskDescription)

  assert(item.description == taskDescription)
  assert(item.complete == False)
  assert(item.creationDate)

def test_save_TodoItem(): pass
#  assert(False)
