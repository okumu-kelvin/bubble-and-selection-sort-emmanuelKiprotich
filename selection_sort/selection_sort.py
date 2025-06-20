def selection_sort(unsorted_list):
    arr = list(unsorted_list)  
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example usage
numbers = [29, 10, 14, 37, 14]
print("Sorted:", selection_sort(numbers))

