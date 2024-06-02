ass Stack:
def __init__(self, limit=None):
    self.items = []
    self.limit = limit


def push(self, item):
    if self.limit and len(self.items) >= self.limit:
        raise ValueError("Stack is full")
    self.items.append(item)

def pop(self):
    if not self.items:
        raise IndexError ("Stack is empty")
    return self.items [-1]

def peek(self):
    if not self.items:
        raise IndexError("Stack is empty")
    return self.items[-1]

def size(self):
    return len(self.items)

def empty(self):
    return len(self.items) == 0

def full(self):
    return self.limit and len(self.items) >= self.limit

def search(self, value):
    try:
        return len(self.items) - 1 - self.items[::-1].index(value)
    except ValueError :
        return -1
    

  