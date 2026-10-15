arr1 = [-5, 23, 7, 5, 1, 1, 3, -12, -29, 21, 54, 35, 0]


def buble_sort(arr):

    for _ in range(len(arr)):
        for i in range(len(arr) - 1):

            if arr[i] > arr[i + 1]:

                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp

            else:
                continue

    return arr


def hairbrush_sort(arr):

    step = len(arr)

    while step > 1:
        step = max(1, int(step / 1.247))

        for i in range(len(arr) - step):

            if arr[i] > arr[i + step]:
                arr[i], arr[i + step] = arr[i + step], arr[i]

    step = max(1, int(step / 1.247))
    
    for i in range(len(arr) - step):

        if arr[i] > arr[i + step]:
            arr[i], arr[i + step] = arr[i + step], arr[i]


    return arr


def choose_sort(arr):

    for i in range(len(arr)):

        min_value = arr[i]
        idx = i

        for j in range(i, len(arr)):

            if arr[j] < min_value:
                min_value = arr[j]
                idx = j

        arr[i], arr[idx] = arr[idx], arr[i]

    return arr


def insert_sort(arr):

    for i in range(1, len(arr)):

        val = arr[i]
        idx = i

        while idx > 0 and arr[idx - 1] > val:

            arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
            idx -= 1

    return arr



def take_pivot(arr, r):
    return arr[r - 1]


def quick_sort_part(arr, l, r):

    if len(arr[l:r]) == 1:
        return [arr[l]]

    if l >= r or len(arr[l:r]) == 0:
        return []

    if len(arr[l:r]) == 2:
        if arr[l] > arr[l + 1]:
            return [arr[l + 1], arr[l]]
        else:
            return arr[l:r]
        
    if len(arr[l:r]) == 3:
        if arr[l] > arr[l + 1]:
            arr[l], arr[l + 1] = arr[l + 1], arr[l]
        if arr[l + 1] > arr[l + 2]:
            arr[l + 1], arr[l + 2] = arr[l + 2], arr[l + 1]
        if arr[l] > arr[l + 1]:
            arr[l], arr[l + 1] = arr[l + 1], arr[l]

        return arr[l:r]

    pivot = take_pivot(arr, r)
    smaller = l - 1

    for i in range(l, r - 1):

        if arr[i] < pivot:
            smaller += 1
            arr[i], arr[smaller] = arr[smaller], arr[i]

    return quick_sort_part(arr, l, smaller + 1) + [pivot] + quick_sort_part(arr, smaller + 1, r - 1) 


def quick_sort(arr):
    return quick_sort_part(arr, 0, len(arr))

    
            
        

           


