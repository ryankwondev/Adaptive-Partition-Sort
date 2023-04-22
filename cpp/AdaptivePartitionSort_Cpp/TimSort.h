#pragma once
class TimSort {
private:
	static inline int FindMinRun(int n);
	static inline void InsertionSort(int* arr, int low, int high);
	static inline void Merge(int* arr, int low, int mid, int high);

public:
	static void Sort(int* arr, unsigned int size);
};

