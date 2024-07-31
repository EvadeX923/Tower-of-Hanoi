class Linked_List:
    
    class __Node:

        def __init__(self, val): 
            self.next = None
            self.previous = None
            self.value = val

    def __init__(self): 
        self.__size = 0
        self.__header = self.__Node(None)
        self.__trailer = self.__Node(None)
        self.__header.next = self.__trailer 
        self.__header.previous = None
        self.__trailer.next = None
        self.__trailer.previous = self.__header

    def __len__(self):
        return self.__size

    def append_element(self, val):
        newest = self.__Node(val)
        self.__size += 1
        newest.previous = self.__trailer.previous
        self.__trailer.previous.next = newest
        self.__trailer.previous = newest
        newest.next = self.__trailer        

    def insert_element_at(self, val, index):
        newest = self.__Node(val)
        
        #index is not valid or list is empty
        if index >= self.__size or index < 0:
            raise IndexError

        #starts from head 
        elif index <= (self.__size - 1) // 2:
            current = self.__header
            for i in range(0, index):
                current = current.next
            newest.next = current.next
            newest.previous = current
            current.next = newest
            newest.next.previous = newest
            self.__size += 1
        
        #starts from tail
        elif index > (self.__size - 1) // 2:
            current = self.__trailer
            for i in range(index, self.__size):
                current = current.previous
            newest.next = current
            newest.previous = current.previous
            newest.previous.next = newest
            current.previous = newest
            self.__size += 1

    def remove_element_at(self, index):
        if index >= self.__size or index < 0 or self.__size == 0:
            raise IndexError
            
        #starts from head
        elif index <= (self.__size - 1) // 2:
            current = self.__header
            for i in range(0, index):
                current = current.next
            temp = current.next.value
            current.next = current.next.next
            current.next.previous = current
            self.__size -= 1
            return temp
        
        #starts from tail
        elif index > (self.__size - 1) // 2:
            current = self.__trailer
            for i in range(index+1, self.__size):
                current = current.previous
            temp = current.previous.value
            current.previous = current.previous.previous
            current.previous.next = current
            self.__size -= 1
            return temp
            
    def get_element_at(self, index):
        if index >= self.__size or index < 0 or self.__size == 0:
            raise IndexError
        
        #starts from head
        elif index <= (self.__size - 1) / 2:
            current = self.__header
            for i in range(0, index + 1):
                current = current.next
            return current.value
        
        #starts from tail
        elif index > (self.__size - 1) / 2:
            current = self.__trailer
            for i in range(index, self.__size):
                current = current.previous
            return current.value

    def rotate_left(self): 
        if self.__size == 0 or self.__size == 1:
            return
        
        #detach from front
        head = self.__header.next
        self.__header.next = head.next
        head.next.previous = self.__header
        
        #attach to back
        head.previous = self.__trailer.previous
        head.next = self.__trailer
        self.__trailer.previous.next = head
        self.__trailer.previous = head

        
    def __str__(self): 
        #list is empty
        if self.__size == 0:
            return '[ ]'
        
        result = '[ '
        current = self.__header.next
        while current is not self.__trailer:
            result = result + str(current.value) + ', '
            current = current.next
        result = result[:-2] + ' ]'
        return result
            

    def __iter__(self):
        self.current = self.__header
        return self

    def __next__(self):
        if self.current.next is not self.__trailer:
            self.current = self.current.next
            return self.current.value
        else:
            raise StopIteration

    def __reversed__(self):
        reverse = Linked_List()
        current = self.__trailer.previous
        
        while current is not self.__header:
            reverse.append_element(current.value)
            current = current.previous
            
        return reverse