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


d = Deque_ended(10)

r = 1
l = -1
while True:
    print("""====================
    1 - add_right()
    2 - add_left()
    3 - pop_right()
    4 - pop_left()""")

    a = input()
    if a == '1':
        d.add_right(r)
        r += 1
        d.pr()
    elif a == '2':
        d.add_left(l)
        l -= 1
        d.pr()
    elif a == '3':
        d.pop_right()
        r -= 1
        d.pr()
    elif a == '4':
        d.pop_left()
        l += 1
        d.pr()
    else:
        print('Введите индекс')
        print(d[int(input())])


    