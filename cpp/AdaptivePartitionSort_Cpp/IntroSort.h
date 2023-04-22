#pragma once
class IntroSort {
private:
	static void Sorting(int* arr, int start, int end, int max_depth);
	static void HeapSort(int* arr, int start, int end);
	static inline void BuildMaxHeap(int* arr, int start, int end);
	static void MaxHeapify(int* arr, int start, int end, int i);
	static inline int Partition(int* arr, int start, int end);

public:
	static void Sort(int* arr, unsigned int size);
};

