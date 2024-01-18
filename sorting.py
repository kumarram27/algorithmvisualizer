class Array:
    def __init__(self, values):
        self.values = values

    def swap(self, i, j):
        self.values[i], self.values[j] = self.values[j], self.values[i]

    def set(self, index, value):
        self.values[index] = value

    def get_len(self):
        return len(self.values)

    def get(self, index):
        return self.values[index]


def bubble_sort(arr):
    n = arr.get_len()
    for i in range(n):
        for j in range(0, n-i-1):
            if arr.get(j) > arr.get(j+1):
                arr.swap(j, j+1)


def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr.get(left) > arr.get(largest):
        largest = left

    if right < n and arr.get(right) > arr.get(largest):
        largest = right

    if largest != i:
        arr.swap(i, largest)
        heapify(arr, n, largest)


def heap_sort(arr):
    n = arr.get_len()

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr.swap(0, i)
        heapify(arr, i, 0)


def selection_sort(arr):
    n = arr.get_len()
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr.get(j) < arr.get(min_index):
                min_index = j
        arr.swap(i, min_index)


def insertion_sort(arr):
    n = arr.get_len()
    for i in range(1, n):
        key = arr.get(i)
        j = i - 1
        while j >= 0 and key < arr.get(j):
            arr.set(j + 1, arr.get(j))
            j -= 1
        arr.set(j + 1, key)


def quick_sort(arr):
    _quick_sort(arr, 0, arr.get_len() - 1)


def _quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        _quick_sort(arr, low, pi - 1)
        _quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr.get(high)
    i = low - 1
    for j in range(low, high):
        if arr.get(j) <= pivot:
            i += 1
            arr.swap(i, j)
    arr.swap(i + 1, high)
    return i + 1


def merge_sort(arr):
    if len(arr.values) > 1:
        mid = len(arr.values) // 2
        left_half = Array(arr.values[:mid])
        right_half = Array(arr.values[mid:])

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half.values) and j < len(right_half.values):
            if left_half.values[i] < right_half.values[j]:
                arr.values[k] = left_half.values[i]
                i += 1
            else:
                arr.values[k] = right_half.values[j]
                j += 1
            k += 1

        while i < len(left_half.values):
            arr.values[k] = left_half.values[i]
            i += 1
            k += 1

        while j < len(right_half.values):
            arr.values[k] = right_half.values[j]
            j += 1
            k += 1
