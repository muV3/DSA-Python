# selection sort finds the smallest element and adds it to a new list
# this is repeated until the end of array is reached
# O(n^2) time complexity


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


test_array = [3, 7, 5, 9, 6]
print(selectionSort(test_array))
