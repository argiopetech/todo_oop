from datetime import datetime

class TodoItem:
    def __init__(self, description):
        self.description = description
        self.complete = False

        self.creationDate = datetime.now()
