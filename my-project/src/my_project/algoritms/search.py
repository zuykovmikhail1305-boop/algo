def binary_search(arr, value):

    arr.sort()

    l = 0
    r = len(arr)

    while l < r:

        mid = (r-l)//2
        search = arr[l +mid] 

        if search == value:
            return value

        else:
            if value > search:
                l = l + mid + 1
            if value < search:
                r = l + mid

    return False