import random
import time
import tracemalloc

import matplotlib.pyplot as plt

from sorting.quick_aps import quick_aps
from sorting.introsort import introsort
from sorting.timsort import timsort
from sorting.quicksort import quick_sort

aps_t, aps_m = [], []
timsort_t, timsort_m = [], []
introsort_t, introsort_m = [], []
quick_sort_t, quick_sort_m = [], []

N = 5000

# time
for i in range(1, N + 1):
    rand = [random.randint(0, i) for _ in range(i)]

    start = time.time()
    arr = quick_aps(rand)
    end = time.time()
    aps_t.append((end - start) * 1000)

    start = time.time()
    arr = timsort(rand)
    end = time.time()
    timsort_t.append((end - start) * 1000)

    start = time.time()
    arr = introsort(rand)
    end = time.time()
    introsort_t.append((end - start) * 1000)

    start = time.time()
    arr = quick_sort(rand)
    end = time.time()
    quick_sort_t.append((end - start) * 1000)

    if i % 100 == 0:
        print(i, aps_t[-1], timsort_t[-1], introsort_t[-1], quick_sort_t[-1])

plt.plot(aps_t)
plt.plot(timsort_t)
plt.plot(introsort_t)
plt.plot(quick_sort_t)
plt.legend(["APS", "Timsort", "Introsort", "Quick_sort"])
plt.title("Time Trends")
plt.tight_layout()
plt.savefig("./images/trends_time.png")
plt.show()

# memory
for i in range(1, N + 1):
    rand = [random.randint(0, i) for _ in range(i)]

    tracemalloc.start()
    arr = quick_aps(rand)
    current, peak = tracemalloc.get_traced_memory()
    aps_m.append(peak)
    tracemalloc.stop()

    tracemalloc.start()
    arr = timsort(rand)
    current, peak = tracemalloc.get_traced_memory()
    timsort_m.append(peak)
    tracemalloc.stop()

    tracemalloc.start()
    arr = introsort(rand)
    current, peak = tracemalloc.get_traced_memory()
    introsort_m.append(peak)
    tracemalloc.stop()

    tracemalloc.start()
    arr = quick_sort(rand)
    current, peak = tracemalloc.get_traced_memory()
    quick_sort_m.append(peak)
    tracemalloc.stop()

    if i % 100 == 0:
        print(i, aps_m[-1], timsort_m[-1], introsort_m[-1], quick_sort_m[-1])

plt.plot(aps_m)
plt.plot(timsort_m)
plt.plot(introsort_m)
plt.plot(quick_sort_m)
plt.legend(["APS", "Timsort", "Introsort", "Quicksort"])
plt.title("Memory Trends")
plt.tight_layout()
plt.savefig("./images/trends_mem.png")
plt.show()
