import random
import time

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
    elapsed_times = []
    for i in range(64):
        # data = generate_data(sample_size)
        data = rand_dataset[i]
        start_time = time.time()
        algorithm(data)
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_times.append(elapsed_time)

    best_time = min(elapsed_times)
    worst_time = max(elapsed_times)
    avg_time = sum(elapsed_times) / len(elapsed_times)

    return best_time, worst_time, avg_time


if __name__ == "__main__":
    sample_size = 100000
    random.seed = 42

    for i in range(64):
        rand_dataset.append(generate_data(sample_size))

    df = pd.DataFrame(
        columns=["Algorithm", "Best Time", "Worst Time", "Average Time"]
    )  # milliseconds

    print("Running experiments for Quick Sort...")
    quick_sort_best, quick_sort_worst, quick_sort_avg = run_experiment(
        quick_imp_wrapper, sample_size
    )
    print(f"Best time: {quick_sort_best * 1000:.4f} milliseconds")
    print(f"Worst time: {quick_sort_worst * 1000:.4f} milliseconds")
    print(f"Average time: {quick_sort_avg * 1000:.4f} milliseconds\n")
    df.loc[len(df)] = [
        "Quick Sort",
        quick_sort_best * 1000,
        quick_sort_worst * 1000,
        quick_sort_avg * 1000,
    ]

    print("Running experiments for Merge Sort...")
    merge_sort_best, merge_sort_worst, merge_sort_avg = run_experiment(
        merge_sort, sample_size
    )
    print(f"Best time: {merge_sort_best * 1000:.4f} milliseconds")
    print(f"Worst time: {merge_sort_worst * 1000:.4f} milliseconds")
    print(f"Average time: {merge_sort_avg * 1000:.4f} milliseconds\n")
    df.loc[len(df)] = [
        "Merge Sort",
        merge_sort_best * 1000,
        merge_sort_worst * 1000,
        merge_sort_avg * 1000,
    ]

    print("Running experiments for Introsort...")
    introsort_best, introsort_worst, introsort_avg = run_experiment(
        introsort, sample_size
    )
    print(f"Best time: {introsort_best * 1000:.4f} milliseconds")
    print(f"Worst time: {introsort_worst * 1000:.4f} milliseconds")
    print(f"Average time: {introsort_avg * 1000:.4f} milliseconds\n")
    df.loc[len(df)] = [
        "Introsort",
        introsort_best * 1000,
        introsort_worst * 1000,
        introsort_avg * 1000,
    ]

    print("Running experiments for Timsort...")
    timsort_best, timsort_worst, timsort_avg = run_experiment(timsort, sample_size)
    print(f"Best time: {timsort_best * 1000:.4f} milliseconds")
    print(f"Worst time: {timsort_worst * 1000:.4f} milliseconds")
    print(f"Average time: {timsort_avg * 1000:.4f} milliseconds\n")
    df.loc[len(df)] = [
        "Timsort",
        timsort_best * 1000,
        timsort_worst * 1000,
        timsort_avg * 1000,
    ]

    print("Running experiments for Adaptive Partition Sort...")
    aps_best, aps_worst, aps_avg = run_experiment(
        lambda data: adaptive_partition_sort(data, 1000), sample_size
    )
    print(f"Best time: {aps_best * 1000:.4f} milliseconds")
    print(f"Worst time: {aps_worst * 1000:.4f} milliseconds")
    print(f"Average time: {aps_avg * 1000:.4f} milliseconds\n")
    df.loc[len(df)] = ["APS", aps_best * 1000, aps_worst * 1000, aps_avg * 1000]

    # cut off the last 6 digits of df
    df["Best Time"] = df["Best Time"].apply(lambda x: round(x, 6))
    df["Worst Time"] = df["Worst Time"].apply(lambda x: round(x, 6))
    df["Average Time"] = df["Average Time"].apply(lambda x: round(x, 6))

    df.to_csv("results_time.csv", index=False)
    print(df)
