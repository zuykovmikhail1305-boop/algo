arr1 = [-5, 23, 7, 5, 3, -12, -29, 21, 54, 35, 0]
arr2 = [1,4,1,1,2]

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

    return arr



def choose_sort(arr):

    for i in range(len(arr)):

        min_value = arr[i]
        idx = i

        for j in range(i,len(arr)):

            if arr[j] < min_value:
                min_value = arr[j]
                idx = j


        arr[i], arr[idx] = arr[idx], arr[i]

    return arr



def insert_sort(arr):

    for i in range(1,len(arr)):

        val = arr[i]
        idx = i

        while idx > 0 and arr[idx - 1] > val:

            arr[idx], arr[idx -  1] = arr[idx - 1], arr[idx]
            idx -= 1

    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    low = [i for i in arr if i < pivot]
    mid = [i for i in arr if i == pivot]
    high = [i for i in arr if i > pivot]

    return quick_sort(low) + mid + quick_sort(high)



    




        
    

        


        
        

    


    
        
             

