def binary_search(array, left, right, goal):
    if left == right and array[left] != goal:
        return 'Value not found'
    middle = left + int(abs(right - left) / 2)
    if array[middle] == goal:
        return middle
    if goal < array[middle]:
        binary_search(array, left, middle - 1, goal)
    else:
        binary_search(array, middle + 1, right, goal)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    binary_search(array, 0, len(array), 9)
