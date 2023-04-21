def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


if __name__ == "__main__":
    import random
    import time
    import tracemalloc

    t, m = [], []

    for i in range(64):
        rand = [random.randint(0, 100000) for _ in range(100000)]
        arr = rand.copy()
        start = time.time()
        arr = merge_sort(arr)
        end = time.time()
        t.append(end - start)
        print("Time Routine:", i, sorted(rand) == arr)

    for i in range(64):
        rand = [random.randint(0, 100000) for _ in range(100000)]
        arr = rand.copy()
        tracemalloc.start()
        arr = merge_sort(arr)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        m.append(peak)
        print("Memory Routine:", i, sorted(rand) == arr)

    print("[Merge Sort]")

    print("Best time(ms): ", min(t) * 1000)
    print("Worst time(ms): ", max(t) * 1000)
    print("Average time(ms): ", sum(t) / len(t) * 1000)

    print("Best space(bytes): ", min(m))
    print("Worst space(bytes): ", max(m))
    print("Average space(bytes): ", sum(m) / len(m))
