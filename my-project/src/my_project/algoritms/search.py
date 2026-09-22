from math import log

def binary_search(arr, value):

    l = 0
    r = len(arr)
    n = log(r)

    for i in range(n):

        search = arr[(r-l)//2] 

        if search == value:
            return value

        else:
            if value > search:
                l = (r-l)//2
            else:
                r = (r-l)//2

    return False