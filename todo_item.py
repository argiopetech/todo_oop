from datetime import datetime

class TodoItem:
    def __init__(self, description):
        if description == "": raise ValueError("Empty description")

        self.description = description
        self.complete = False

        self.creationDate = datetime.now()


    def save(self):
        return f"False|{self.description}"

    def markComplete(self):
        self.complete = True
