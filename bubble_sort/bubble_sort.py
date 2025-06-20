def bubble_sort(unsorted_list):

    arr = list(unsorted_list)
    n = len(arr)

    for i in range(n):
        swapped = False 

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break  # No swaps = list already sorted

    return arr

# Example usage
numbers = [4, 5, 3, 4]
print("Sorted:", bubble_sort(numbers))
