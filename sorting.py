def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(array):
    n = len(array)
    for i in range(n):
        key = i
        for j in range(i + 1, n):
            if array[j] < array[key]:
                key = j
        array[i], array[key] = array[key], array[i]
    return array
