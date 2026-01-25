def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + recursive_sum(arr[1:])


def item_count(arr):
    if len(arr) == 0:
        return 0
    return 1 + item_count(arr[1:])


def find_max(arr):
    max = 0
    while arr:
        if arr[0] > max:
            max = arr[0]
        arr = arr[1:]
    return max


test_array = [1, 2, 3]
print(recursive_sum(test_array))
print(item_count(test_array))
print(find_max(test_array))
