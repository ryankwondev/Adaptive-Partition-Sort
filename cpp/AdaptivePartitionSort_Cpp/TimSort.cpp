#include "TimSort.h"
#include <iostream>
using namespace std;
#define min(x, y) (x < y ? x : y)
#define MINIMUM 32

inline int TimSort::FindMinRun(int n) {
	register int r = 0;
	while (n >= MINIMUM) {
		r |= n & 1;
		n >>= 1;
	}
	return n + r;
}

inline void TimSort::InsertionSort(int* arr, int low, int high) {
	for (register int i = low + 1; i <= high; ++i) {
		register int e = arr[i];
		register int j = i;
		while (e < arr[--j] && j >= low) arr[j + 1] = arr[j];
		arr[j + 1] = e;
	}
}

inline void TimSort::Merge(int* arr, int low, int mid, int high) {
	register int left = low;
	register int right = mid + 1;
	register int k = -1;
	register int* tmp = new int[high - low + 1];
	while (left <= mid and right <= high) {
		if (arr[left] <= arr[right]) tmp[++k] = arr[left++];
		else tmp[++k] = arr[right++];
	}

	register int i = left - 1;
	while (i < mid) tmp[++k] = arr[++i];
	i = right - 1;
	while (i < high) tmp[++k] = arr[++i];
	i = high + 1;
	k = high - low + 1;
	while (k) arr[--i] = tmp[--k];
	delete[] tmp;
}

void TimSort::Sort(int* arr, unsigned int size) {
	int minrun = FindMinRun(size);
	for (register int start = 0; start < size; start += minrun) {
		InsertionSort(arr, start, min(start + minrun - 1, size - 1));
	}
	int n = minrun;
	--size;
	while (size + 1 > n) {
		register int unit = n << 1;
		for (register int left = 0; left < size; left += unit) {
			register int mid = min(size, left + n - 1);
			register int right = min((left + 2 * n - 1), size);
			Merge(arr, left, mid, right);
		}
		n <<= 1;
	}
}
