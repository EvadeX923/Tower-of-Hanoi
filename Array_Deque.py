from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__size = 0
    self.__front = 0
    self.__rear = self.__capacity - 1
    
  def __str__(self):
    if self.__size == 0:
        return '[ ]'
    result = [ ]
    index = self.__front
    for i in range(self.__size):
      result.append(str(self.__contents[index % self.__capacity]))
      result.append(', ')
      index += 1
    return '[ ' + ''.join(result)[:-2] + ' ]'
    
  def __len__(self):
    return self.__size

  def __grow(self):
    old = self.__capacity
    self.__capacity *= 2
    temp = self.__contents
    self.__contents = [None] * self.__capacity
    index = self.__front
    for i in range(self.__size):
        self.__contents[i] = temp[index % old]
        index += 1
    self.__front = 0
    self.__rear = self.__size - 1
    
  def push_front(self, val):
    if self.__size == self.__capacity:
        self.__grow()
    self.__contents[(self.__front-1) % self.__capacity] = val
    self.__front -= 1
    self.__size += 1
    
  def pop_front(self):
    if self.__size == 0:
        return
    temp = self.__contents[self.__front % self.__capacity]
    self.__contents[self.__front % self.__capacity] = None
    self.__front += 1
    self.__size -= 1
    return temp
    
  def peek_front(self):
    return self.__contents[self.__front % self.__capacity]
    
  def push_back(self, val):
    if self.__size == self.__capacity:
        self.__grow() 
    self.__contents[(self.__rear+1) % self.__capacity] = val
    self.__rear += 1
    self.__size += 1
  
  def pop_back(self):
    if self.__size == 0:
        return
    temp = self.__contents[self.__rear % self.__capacity]
    self.__contents[self.__rear % self.__capacity] = None
    self.__rear -= 1
    self.__size -= 1
    return temp

  def peek_back(self):
    return self.__contents[self.__rear % self.__capacity]