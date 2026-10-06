import numpy as np

class Core():
    def __init__(self):
        self.core = []
        self.commit = []
        self.kesh = dict()


    def add(self, value):

        if len(self.commit) == 0:
            self.commit.append(value)

        else:    
            self.commit.insert(value, 0)
            for i in range(1, len(self.commit)):

                if self.commit[i - 1] <= self.commit[0] < self.commit[i]:
                    self.commit.insert(self.commit[0], i)
                    del(self.commit[0])


    def _make_range(self):

        tmp_arr = []
        tmp = 0

        flag = False

        for i in range(len(self.commit) - 1):

            if self.commit[i + 1] - self.commit[i] == 1:

                if flag == False:
                    tmp = self.commit[i]
                    flag = True

            else:

                if flag == False:
                    tmp_arr.append(self.commit[i])

                else:
                    tmp_arr.append(self.commit[i])
                    self.kesh[tmp] = self.commit[i]

            return tmp_arr


    def make_commit(self):

        lits_commit = self._make_range()

        for i in lits_commit:

            if i in self.kesh:

                for j in range(i, self.kesh[i] + 1, 1):
                    self.core.append(j)

            else:

                self.core.append(i)

        self.commit = []
        self.kesh = dict()


    def show(self):
        print('core', self.core)
        print('commit', self.commit)


core = Core()

core.add(10)
core.show()
core.add(20)
core.show()
core.add(15)
core.show()
core.add(40)
core.show()
core.add(30)
core.make_commit()
core.show()