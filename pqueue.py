
import collections


class Queue:

  def __init__(self, x=None):
    self.items = collections.deque()
    if x:
      self.push(x)

  def empty(self):
    return not self.items
    
  def size(self):
    return len(self.items)
    
  def last(self):
    return self.items[-1]

  def push(self, x):
    self.items.append(x)

  def pop(self):
    return self.items.pop()

  def popleft(self):
    return self.items.popleft()

  def pushleft(self, x):
    self.items.insert(0, x)
