#pragma once
class APS {
private:
	static void QuickSort(int* arr, int low, int high);
	static void MergeSort(int* arr, int low, int high);

public:
	static void Sort(int* arr, unsigned int size);
};