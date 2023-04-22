def medianofthreequick_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    high = len(arr) - 1
    low = 0
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

    pivot = arr[mid]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return medianofthreequick_sort(left) + middle + medianofthreequick_sort(right)


if __name__ == "__main__":
    import random
    import time
    import tracemalloc

    t, m = [], []

    for i in range(64):
        rand = [random.randint(0, 100000) for _ in range(100000)]
        arr = rand.copy()
        start = time.time()
        arr = medianofthreequick_sort(arr)
        end = time.time()
        t.append(end - start)
        print("Time Routine:", i, sorted(rand) == arr)

    for i in range(64):
        rand = [random.randint(0, 100000) for _ in range(100000)]
        arr = rand.copy()
        tracemalloc.start()
        arr = medianofthreequick_sort(arr)
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
