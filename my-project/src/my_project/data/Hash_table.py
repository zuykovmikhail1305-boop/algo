from hashlib import md5

class Hash_table:
    def __init__(self, size = 8):
        self.size = size
        self.values = []
        self.table = [None] * self.size
        self._occupancy = 0


    def _count_hash(self, value):
        return value % self.size


    def _new_table(self):   
        self.size = self.size * 2
        self.table = [None] * self.size

        for i in self.values:
            self.table[self._count_hash(i)] = i


    def put(self, value):
        if self._occupancy / self.size > 0.75:
            self._new_table()

        hash = self._count_hash(value)

        if self.table[hash] == value:
            pass
        elif self.table[hash] != None:
            self._new_table()
            self.put(value)
        else:
            self.table[hash] = value
            self.values.append(value)
            self._occupancy += 1

    def get(self, key):
        return self.table[key]

    def remove(self, key):
        self.table[key] = None

    def p(self):
        print(self.table)



h = Hash_table()
h.put(8)
h.put(90)
h.put(9)
h.put(16)
h.p()

