from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

  def __str__(self):
    return str(self.__list)

  def __len__(self):
    return len(self.__list)
  
  def push_front(self, val):
    if len(self.__list) == 0:
        self.__list.append_element(val)
    else:
        self.__list.insert_element_at(val, 0)
  
  def pop_front(self):
    if len(self.__list) == 0:
        return
    return self.__list.remove_element_at(0)

  def peek_front(self):
    if len(self.__list) == 0:
        return
    return self.__list.get_element_at(0)

  def push_back(self, val):
    self.__list.append_element(val)
  
  def pop_back(self):
    if len(self.__list) == 0:
        return
    return self.__list.remove_element_at(len(self.__list)-1)

  def peek_back(self):
    if len(self.__list) == 0:
        return
    return self.__list.get_element_at(len(self.__list)-1)