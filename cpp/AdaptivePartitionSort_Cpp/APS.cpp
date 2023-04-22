#include "APS.h"

#define THRESHOLD 0

void inline swap(int& a, int& b) {
	register int t = a;
	a = b;
	b = t;
}

void APS::QuickSort(int* arr, int low, int high) {
	if (low >= high) return;
	
	unsigned int j = high + 1;

	{
		register int mid = (low + high) >> 1;

		if (arr[low] > arr[mid]) swap(arr[low], arr[mid]);
		if (arr[low] > arr[high]) swap(arr[low], arr[high]);
		if (arr[mid] > arr[high]) swap(arr[mid], arr[high]);

		register int pivot = arr[mid];

		register unsigned int i = low - 1;
		while (arr[++i] < pivot);
		while (arr[--j] > pivot);
		while (i < j) {
			swap(arr[i], arr[j]);
			while (arr[++i] < pivot);
			while (arr[--j] > pivot);
		}
	}

	if (j - low < THRESHOLD) MergeSort(arr, low, j);
	else QuickSort(arr, low, j);
	
	if (high - j <= THRESHOLD) MergeSort(arr, j + 1, high);
	else QuickSort(arr, j + 1, high);
}

void APS::MergeSort(int* arr, int low, int high) {
	if (low >= high) return;

	int mid = (low + high) >> 1;
	MergeSort(arr, low, mid);
	MergeSort(arr, mid + 1, high);

	{
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
		i = low - 1;
		k = -1;
		while (i < high) arr[++i] = tmp[++k];
		delete[] tmp;
	}
}

void APS::Sort(int* arr, unsigned int size) {
	QuickSort(arr, 0, size - 1);
}

