import random
import tracemalloc

import pandas as pd

from sorting.aps import adaptive_partition_sort
from sorting.introsort import introsort
from sorting.mergesort import merge_sort
from sorting.quicksort import quick_imp_wrapper
from sorting.timsort import timsort

rand_dataset = []


def generate_data(size):
    return [random.randint(1, 100000) for _ in range(size)]


def run_experiment(algorithm, sample_size):
    elapsed_mem = []
    for i in range(64):
        # data = generate_data(sample_size)
        data = rand_dataset[i]
        tracemalloc.start()
        algorithm(data)
        elapsed_mem.append(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()

    best_mem = min(elapsed_mem)
    worst_mem = max(elapsed_mem)
    avg_mem = sum(elapsed_mem) / len(elapsed_mem)

    return best_mem, worst_mem, avg_mem


if __name__ == "__main__":
    sample_size = 100000
    random.seed = 42

    for i in range(64):
        rand_dataset.append(generate_data(sample_size))

    df = pd.DataFrame(
        columns=["Algorithm", "Best Memory", "Worst Memory", "Average Memory"]
    )  # B

    print("Running experiments for Quick Sort...")
    quick_sort_best, quick_sort_worst, quick_sort_avg = run_experiment(
        quick_imp_wrapper, sample_size
    )
    print(f"Best memory: {quick_sort_best:.4f} B")
    print(f"Worst memory: {quick_sort_worst:.4f} B")
    print(f"Average memory: {quick_sort_avg:.4f} B\n")
    df.loc[len(df)] = ["Quick Sort", quick_sort_best, quick_sort_worst, quick_sort_avg]

    print("Running experiments for Merge Sort...")
    merge_sort_best, merge_sort_worst, merge_sort_avg = run_experiment(
        merge_sort, sample_size
    )
    print(f"Best memory: {merge_sort_best:.4f} B")
    print(f"Worst memory: {merge_sort_worst:.4f} B")
    print(f"Average memory: {merge_sort_avg:.4f} B\n")
    df.loc[len(df)] = ["Merge Sort", merge_sort_best, merge_sort_worst, merge_sort_avg]

    print("Running experiments for Introsort...")
    introsort_best, introsort_worst, introsort_avg = run_experiment(
        introsort, sample_size
    )
    print(f"Best memory: {introsort_best:.4f} B")
    print(f"Worst memory: {introsort_worst:.4f} B")
    print(f"Average memory: {introsort_avg:.4f} B\n")
    df.loc[len(df)] = ["Introsort", introsort_best, introsort_worst, introsort_avg]

    print("Running experiments for Timsort...")
    timsort_best, timsort_worst, timsort_avg = run_experiment(timsort, sample_size)
    print(f"Best memory: {timsort_best:.4f} B")
    print(f"Worst memory: {timsort_worst:.4f} B")
    print(f"Average memory: {timsort_avg:.4f} B\n")
    df.loc[len(df)] = ["Timsort", timsort_best, timsort_worst, timsort_avg]

    print("Running experiments for Adaptive Partition Sort...")
    aps_best, aps_worst, aps_avg = run_experiment(
        lambda data: adaptive_partition_sort(data, 1000), sample_size
    )
    print(f"Best memory: {aps_best:.4f} B")
    print(f"Worst memory: {aps_worst:.4f} B")
    print(f"Average memory: {aps_avg:.4f} B\n")
    df.loc[len(df)] = ["APS", aps_best, aps_worst, aps_avg]

    # cut off the last 6 digits of df
    df["Best Memory"] = df["Best Memory"].apply(lambda x: round(x, 6))
    df["Worst Memory"] = df["Worst Memory"].apply(lambda x: round(x, 6))
    df["Average Memory"] = df["Average Memory"].apply(lambda x: round(x, 6))

    df.to_csv("./results_mem.csv", index=False)
    print(df)
