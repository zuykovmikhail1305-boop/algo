import numpy as np


class Deque_ended():

    def __init__(self, lenght):

        self.lenght = lenght
        self.capacity = 0
        self.arr = np.zeros(lenght)
        self.right = self.lenght//2 + 1
        self.left = self.lenght//2


    def __getitem__(self, key):

        if not isinstance(key, int):
            raise TypeError('Index should be int')

        else:             
            if key < 0:
                key += self.capacity

            
            if key < 0 or key >= self.capacity:
                raise IndexError('Deque index out of range ')
                
            idx = (self.left + 1 + key) % self.lenght
            
            return self.arr[idx]    

        
    def is_full(self):

        return self.lenght == self.capacity


    def is_empty(self):

        if self.capacity <= 0:
            return True
        
        return False


    def add_right(self, value):

        if self.is_full():
            raise OverflowError('Deque is full')
        
        self.arr[self.right % self.lenght] = value
        self.right += 1
        self.capacity += 1

        
    def add_left(self, value):

        if self.is_full():
            raise OverflowError('Deque is full')
        
        self.arr[self.left % self.lenght] = value
        self.left -= 1
        self.capacity += 1


    def pop_right(self):

        if self.is_empty():
            raise ValueError('Deque is empty')

        self.right -= 1
        self.arr[self.right % self.lenght] = 0
        self.capacity -= 1


    def pop_left(self):

        if self.is_empty():
            raise ValueError('Deque is empty')

        self.left += 1
        self.arr[self.left % self.lenght] = 0
        self.capacity -= 1

        
    def pr(self):
        print(self.arr)


