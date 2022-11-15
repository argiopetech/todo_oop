from datetime import datetime

class TodoItem:
    def __init__(self, description):
        if description == "": 
            raise ValueError("Empty description")

        self.description = description
        self.complete = False

        self.creationDate = datetime.now()


    def save(self):
        return f"{self.complete}|{self.description}"


    def markComplete(self):
        self.complete = True

    def load(toLoad):
        [completion, descr] = toLoad.split('|', 1)
        item = TodoItem(descr)

        return item

    def __eq__(self, other):
        return self.description == other.description and self.complete == other.complete
