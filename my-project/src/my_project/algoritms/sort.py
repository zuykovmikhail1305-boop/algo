arr1 = [-5, 23, 7, 5, 3, -12, -29, 21, 54, 35, 0]
arr2 = [1,4,1,1,2]

def buble_sort(arr):

    for _ in range(len(arr)):
        for i in range(len(arr) - 1):

            if arr[i] > arr[i + 1]:

                rem = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = rem

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

    return arr


def choose_sort(arr):

    new_arr = []

    for _ in range(len(arr)):
        min_count = float('inf')
        idx = 0

        for i in range(len(arr)):
            if arr[i] < min_count:
                min_count = arr[i]
                idx = i

        new_arr.append(min_count)
        del arr[idx]

    return new_arr

print(choose_sort(arr1))


        
             

