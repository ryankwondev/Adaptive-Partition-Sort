import random
import time

import pandas as pd

from sorting.aps import adaptive_partition_sort
from sorting.introsort import introsort
from sorting.mergesort import merge_sort
from sorting.quicksort import quick_sort
from sorting.timsort import timsort

from testdatas import generate_test_datas


def get_mean(algorithm, datas):
    elapsed_times = []
    for i in range(len(datas)):
        data = datas[i]
        start_time = time.time()
        algorithm(data)
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_times.append(elapsed_time)

    best_time = min(elapsed_times)
    worst_time = max(elapsed_times)
    avg_time = sum(elapsed_times) / len(elapsed_times)

    return best_time, worst_time, avg_time


def run(datas):
    df = pd.DataFrame(
        columns=["Algorithm", "Best Time", "Worst Time", "Average Time"]
    )  # milliseconds

    quick_sort_best, quick_sort_worst, quick_sort_avg = get_mean(quick_sort, datas)
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
    merge_sort_best, merge_sort_worst, merge_sort_avg = get_mean(merge_sort, datas)
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
    introsort_best, introsort_worst, introsort_avg = get_mean(introsort, datas)
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
    timsort_best, timsort_worst, timsort_avg = get_mean(timsort, datas)
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
    aps_best, aps_worst, aps_avg = get_mean(
        lambda data: adaptive_partition_sort(data, 0), datas
    )
    print(f"Best time: {aps_best * 1000:.4f} milliseconds")
    print(f"Worst time: {aps_worst * 1000:.4f} milliseconds")
    print(f"Average time: {aps_avg * 1000:.4f} milliseconds\n")
    df.loc[len(df)] = ["APS", aps_best * 1000, aps_worst * 1000, aps_avg * 1000]

    # cut off the last 6 digits of df
    df["Best Time"] = df["Best Time"].apply(lambda x: round(x, 6))
    df["Worst Time"] = df["Worst Time"].apply(lambda x: round(x, 6))
    df["Average Time"] = df["Average Time"].apply(lambda x: round(x, 6))

    # df.to_csv('./results/mem.csv', index=False)
    print(df)


if __name__ == "__main__":
    print("Running 1M")
    datas = [generate_test_datas.shuffled() for _ in range(16)]
    run(datas)

    print("Running 1M (16)")
    datas = [generate_test_datas.shuffled_16_values() for _ in range(16)]
    run(datas)

    print("Running ASC")
    datas = [generate_test_datas.ascending() for _ in range(4)]
    run(datas)

    print("Running DSC")
    datas = [generate_test_datas.descending() for _ in range(4)]
    run(datas)

    print("Running Pipeorgan")
    datas = [generate_test_datas.pipe_organ() for _ in range(4)]
    run(datas)
    # print("Running DSC")
    # print("Running PipeOrgan")
