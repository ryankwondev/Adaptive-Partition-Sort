#include "APS.h"

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

	QuickSort(arr, low, j);
	QuickSort(arr, j + 1, high);
}

void APS::Sort(int* arr, unsigned int size) {
	QuickSort(arr, 0, size - 1);
}

