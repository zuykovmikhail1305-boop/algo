

class Hash_table:
    def __init__(self, size = 8):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self._occupancy = 0


    def _count_hash(self, key):
        return key % self.size


    def put(self, key, value):
        hash = self._count_hash(key)
        self.table[hash].append((key, value))


    def get(self, key):

        hash = self._count_hash(key)
        for i in self.table[hash]:
            if i[0] == key:
                return i[1]

    def remove(self, key):
        
        hash = self._count_hash(key)
        for i in range(len(self.table[hash])):
            if self.table[hash][i][0] == key:
                self.table[hash].pop(i)

    def p(self):
        print(self.table)



h = Hash_table()
h.p()
h.put(8, 1)
h.put(90, 2)
h.put(9, 3)
h.put(16, 4)
print(h.get(16))
h.remove(16)
h.p()


