MINIMUM = 32


def find_minrun(n):
    r = 0
    while n >= MINIMUM:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        element = array[i]
        j = i - 1
        while element < array[j] and j >= left:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = element
    return array


def merge(array, l, m, r):
    array_length1 = m - l + 1
    array_length2 = r - m
    left = []
    right = []
    for i in range(0, array_length1):
        left.append(array[l + i])
    for i in range(0, array_length2):
        right.append(array[m + 1 + i])

    i = 0
    j = 0
    k = l

    while j < array_length2 and i < array_length1:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1

        else:
            array[k] = right[j]
            j += 1

        k += 1

    while i < array_length1:
        array[k] = left[i]
        k += 1
        i += 1

    while j < array_length2:
        array[k] = right[j]
        k += 1
        j += 1


def timsort(array):
    n = len(array)
    minrun = find_minrun(n)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        insertion_sort(array, start, end)

    size = minrun
    while size < n:

        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            merge(array, left, mid, right)
            print(left, mid, right)
        size = 2 * size


if __name__ == '__main__':
    import random
    import time
    import tracemalloc

    t, m = [], []

    for i in range(64):
        rand = [random.randint(0, 100) for _ in range(100)]
        arr = rand.copy()
        start = time.time()
        timsort(arr)
        end = time.time()
        t.append(end - start)
        print('Time Routine:', i, sorted(rand) == arr)

    for i in range(64):
        rand = [random.randint(0, 100000) for _ in range(100000)]
        arr = rand.copy()
        tracemalloc.start()
        timsort(arr)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        m.append(peak)
        print('Memory Routine:', i, sorted(rand) == arr)

    print('[Timsort]')

    print('Best time(ms): ', min(t) * 1000)
    print('Worst time(ms): ', max(t) * 1000)
    print('Average time(ms): ', sum(t) / len(t) * 1000)

    print('Best space(bytes): ', min(m))
    print('Worst space(bytes): ', max(m))
    print('Average space(bytes): ', sum(m) / len(m))
