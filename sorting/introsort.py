import math


def introsort(arr):
    maxdepth = 2 * math.floor(math.log2(len(arr)))
    _introsort(arr, 0, len(arr), maxdepth)


def _introsort(arr, start, end, maxdepth):
    if end - start <= 1:
        return
    if maxdepth == 0:
        heapsort(arr, start, end)
    else:
        pivot = partition(arr, start, end)
        _introsort(arr, start, pivot, maxdepth - 1)
        _introsort(arr, pivot + 1, end, maxdepth - 1)


def heapsort(arr, start, end):
    build_max_heap(arr, start, end)
    for i in range(end - 1, start, -1):
        arr[start], arr[i] = arr[i], arr[start]
        max_heapify(arr, start, i, 0)


def build_max_heap(arr, start, end):
    length = end - start
    for i in range(length // 2 - 1, -1, -1):
        max_heapify(arr, start, end, i)


def max_heapify(arr, start, end, i):
    length = end - start
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < length and arr[start + left] > arr[start + largest]:
        largest = left
    if right < length and arr[start + right] > arr[start + largest]:
        largest = right

    if largest != i:
        arr[start + i], arr[start + largest] = arr[start + largest], arr[start + i]
        max_heapify(arr, start, end, largest)


def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end - 1

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[start], arr[right] = arr[right], arr[start]
    return right


if __name__ == "__main__":
    import random
    import time
    import tracemalloc

    t, m = [], []

    for i in range(64):
        rand = [random.randint(0, 100000) for _ in range(100000)]
        arr = rand.copy()
        start = time.time()
        introsort(arr)
        end = time.time()
        t.append(end - start)
        print("Time Routine:", i, sorted(rand) == arr)

    for i in range(64):
        rand = [random.randint(0, 100000) for _ in range(100000)]
        arr = rand.copy()
        tracemalloc.start()
        introsort(arr)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        m.append(peak)
        print("Memory Routine:", i, sorted(rand) == arr)

    print("[IntroSort]")

    print("Best time(ms): ", min(t) * 1000)
    print("Worst time(ms): ", max(t) * 1000)
    print("Average time(ms): ", sum(t) / len(t) * 1000)

    print("Best space(bytes): ", min(m))
    print("Worst space(bytes): ", max(m))
    print("Average space(bytes): ", sum(m) / len(m))
