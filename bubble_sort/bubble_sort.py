numbers = [5, 2, 4, 6, 1, 3]

def bubble_sort(unsorted_list):
    
    arr = list(unsorted_list)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr