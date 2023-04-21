import random
import tracemalloc

import pandas as pd

from sorting.aps import adaptive_partition_sort
from sorting.introsort import introsort
from sorting.mergesort import merge_sort
from sorting.quicksort import quick_sort
from sorting.timsort import timsort

from testdatas import generate_test_datas


def get_mean(algorithm, datas):
    elapsed_mem = []
    for i in range(len(datas)):
        data = datas[i]
        tracemalloc.start()
        algorithm(data)
        elapsed_mem.append(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()

    best_mem = min(elapsed_mem)
    worst_mem = max(elapsed_mem)
    avg_mem = sum(elapsed_mem) / len(elapsed_mem)

    return best_mem, worst_mem, avg_mem


def run(datas):
    df = pd.DataFrame(
        columns=["Algorithm", "Best Memory", "Worst Memory", "Average Memory"]
    )  # B

    """ print("Running experiments for Quick Sort...")
    quick_sort_best, quick_sort_worst, quick_sort_avg = get_mean(quick_sort, datas)
    print(f"Best memory: {quick_sort_best:.4f} B")
    print(f"Worst memory: {quick_sort_worst:.4f} B")
    print(f"Average memory: {quick_sort_avg:.4f} B\n")
    df.loc[len(df)] = ['Quick Sort', quick_sort_best, quick_sort_worst, quick_sort_avg] """

    print("Running experiments for Merge Sort...")
    merge_sort_best, merge_sort_worst, merge_sort_avg = get_mean(merge_sort, datas)
    print(f"Best memory: {merge_sort_best:.4f} B")
    print(f"Worst memory: {merge_sort_worst:.4f} B")
    print(f"Average memory: {merge_sort_avg:.4f} B\n")
    df.loc[len(df)] = ["Merge Sort", merge_sort_best, merge_sort_worst, merge_sort_avg]

    print("Running experiments for Introsort...")
    introsort_best, introsort_worst, introsort_avg = get_mean(introsort, datas)
    print(f"Best memory: {introsort_best:.4f} B")
    print(f"Worst memory: {introsort_worst:.4f} B")
    print(f"Average memory: {introsort_avg:.4f} B\n")
    df.loc[len(df)] = ["Introsort", introsort_best, introsort_worst, introsort_avg]

    print("Running experiments for Timsort...")
    timsort_best, timsort_worst, timsort_avg = get_mean(timsort, datas)
    print(f"Best memory: {timsort_best:.4f} B")
    print(f"Worst memory: {timsort_worst:.4f} B")
    print(f"Average memory: {timsort_avg:.4f} B\n")
    df.loc[len(df)] = ["Timsort", timsort_best, timsort_worst, timsort_avg]

    print("Running experiments for Adaptive Partition Sort...")
    aps_best, aps_worst, aps_avg = get_mean(
        lambda data: adaptive_partition_sort(data, 0), datas
    )
    print(f"Best memory: {aps_best:.4f} B")
    print(f"Worst memory: {aps_worst:.4f} B")
    print(f"Average memory: {aps_avg:.4f} B\n")
    df.loc[len(df)] = ["APS", aps_best, aps_worst, aps_avg]

    # cut off the last 6 digits of df
    df["Best Memory"] = df["Best Memory"].apply(lambda x: round(x, 6))
    df["Worst Memory"] = df["Worst Memory"].apply(lambda x: round(x, 6))
    df["Average Memory"] = df["Average Memory"].apply(lambda x: round(x, 6))

    # df.to_csv('./results/mem.csv', index=False)
    print(df)


if __name__ == "__main__":
    """print("Running 1M")
    datas = [generate_test_datas.shuffled() for _ in range(4)]
    run(datas)

    print("Running 1M (16)")
    datas = [generate_test_datas.shuffled_16_values() for _ in range(4)]
    run(datas)


    print("Running ASC")
    datas = [generate_test_datas.ascending() for _ in range(4)]
    run(datas)

    print("Running DSC")
    datas = [generate_test_datas.descending() for _ in range(4)]
    run(datas)"""

    print("Running Pipeorgan")
    datas = [generate_test_datas.pipe_organ() for _ in range(4)]
    run(datas)
    # print("Running DSC")
    # print("Running PipeOrgan")
