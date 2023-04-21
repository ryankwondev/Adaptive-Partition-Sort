def counting_sort(array):
    counting_array = [0] * (len(array) + 1)

    for i in array:
        counting_array[i] += 1

    for i in range(len(array)):
        counting_array[i + 1] += counting_array[i]

    output_array = [-1] * len(array)

    for i in array:
        output_array[counting_array[i] - 1] = i
        counting_array[i] -= 1
    return output_array


if __name__ == '__main__':
    import random
    import time
    import tracemalloc

    t, m = [], []

    for i in range(64):
        rand = [random.randint(0, 100000) for _ in range(100000)]
        arr = rand.copy()
        start = time.time()
        arr = counting_sort(arr)
        end = time.time()
        t.append(end - start)
        print('Time Routine:', i, sorted(rand) == arr)

    for i in range(64):
        rand = [random.randint(0, 100000) for _ in range(100000)]
        arr = rand.copy()
        tracemalloc.start()
        arr = counting_sort(arr)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        m.append(peak)
        print('Memory Routine:', i, sorted(rand) == arr)

    print('[Counting Sort]')

    print('Best time(ms): ', min(t) * 1000)
    print('Worst time(ms): ', max(t) * 1000)
    print('Average time(ms): ', sum(t) / len(t) * 1000)

    print('Best space(bytes): ', min(m))
    print('Worst space(bytes): ', max(m))
    print('Average space(bytes): ', sum(m) / len(m))
