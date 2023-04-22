#include "IntroSort.h"
#include <cmath>
#include <iostream>
using namespace std;

void inline swap(int& a, int& b) {
	register int t = a;
	a = b;
	b = t;
}

void IntroSort::Sorting(int* arr, int start, int end, int max_depth) {
	if (end - start <= 1) return;
	if (max_depth) {
		int pivot = Partition(arr, start, end);
		Sorting(arr, start, pivot, --max_depth);
		Sorting(arr, pivot + 1, end, max_depth);
	}
	else HeapSort(arr, start, end);	
}

void IntroSort::HeapSort(int* arr, int start, int end) {
	BuildMaxHeap(arr, start, end);
	for (register int i = end - 1; i >= start; --i) {
		swap(arr[start], arr[i]);
		MaxHeapify(arr, start, i, 0);
	}
}

inline void IntroSort::BuildMaxHeap(int* arr, int start, int end) {
	for (register int i = ((end - start) >> 1) - 1; i >= 0; --i) {
		MaxHeapify(arr, start, end, i);
	}
}

void IntroSort::MaxHeapify(int* arr, int start, int end, int i) {
	int largest = i;
	{
		register int len = end - start;
		register int left = (i << 1) + 1;
		register int right = left + 1;	
		if (left < len && arr[start + left] > arr[start + largest]) largest = left;
		if (right < len && arr[start + right] > arr[start + largest]) largest = right;
	}
	if (largest != i) {
		swap(arr[start + i], arr[start + largest]);
		MaxHeapify(arr, start, end, largest);
	}
}

inline int IntroSort::Partition(int* arr, int start, int end) {
	register int pivot = arr[start];
	register int left = start + 1;
	register int right = end - 1;
	while (true) {
		while (left <= right && arr[left] <= pivot) ++left;
		while (arr[right] >= pivot && right >= left) --right;
		if (right < left) break;
		swap(arr[left], arr[right]);
	}
	swap(arr[start], arr[right]);
	return right;
}

void IntroSort::Sort(int* arr, unsigned int size) {
	Sorting(arr, 0, size, (int)log2(size) << 1);
}
