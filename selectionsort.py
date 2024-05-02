def selection_sort(array):
    n = len(array)
    for i in range(n):
        key = i
        for j in range(i + 1, n):
            if array[j] < array[key]:
                key = j
        array[i], array[key] = array[key], array[i]
    return array
