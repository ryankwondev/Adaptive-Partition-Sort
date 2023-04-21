import random
import time
import tracemalloc

import matplotlib.pyplot as plt

from sorting.aps import adaptive_partition_sort

t, m = [], []

# time
for i in range(10000):
    rand = [random.randint(0, i) for _ in range(i)]
    start = time.time()
    arr = adaptive_partition_sort(rand)
    end = time.time()
    t.append(end - start)

    if i % 100 == 0:
        print(i)

plt.plot(t)
plt.show()

# memory
for i in range(10000):
    rand = [random.randint(0, i) for _ in range(i)]
    tracemalloc.start()
    arr = adaptive_partition_sort(rand)
    current, peak = tracemalloc.get_traced_memory()
    m.append(peak)
    tracemalloc.stop()

    if i % 100 == 0:
        print(i)

plt.plot(m)
plt.show()
