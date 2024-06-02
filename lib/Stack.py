ass Stack:
def __init__(self, limit=None):
    self.items = []
    self.limit = limit


def push(self, item):
    if self.limit and len(self.items) >= self.limit:
        raise ValueError("Stack is full")
    self.items.append(item)

def pop(self)
  