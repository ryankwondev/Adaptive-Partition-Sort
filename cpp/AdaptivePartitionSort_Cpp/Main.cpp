#include <iostream>
#include <ctime>
#include <algorithm>
#include <vector>
#include "APS.h"
using namespace std;
int* MakeRandomArray(int size, int range) {
	int* arr = new int[size];
	for (int i = 0; i < size; i++) {
		arr[i] = rand() % range;
	}
	return arr;
}
int* CopyArray(int* arr, int size) {
	int* ret = new int[size];
	for (int i = 0; i < size; i++) {
		ret[i] = arr[i];
	}
	return ret;
}
vector<int> CopyArray2Vector(int* arr, int size) {
	vector<int> ret;
	for (int i = 0; i < size; i++) {
		ret.push_back(arr[i]);
	}
	return ret;
}

int compare(const void* a, const void* b) {
	const int* x = (int*)a;
	const int* y = (int*)b;

	if (*x > *y) return 1;
	else if (*x < *y) return -1;
	return 0;
}

bool CheckAccuracy(int* arr, int size) {
	for (int i = 0; i < size - 1; i++)
		if (arr[i] > arr[i + 1]) return false;
	return true;
}

bool CheckAccuracy(vector<int> &data) {
	for (int i = 0; i < data.size() - 1; i++)
		if (data[i] > data[i + 1]) return false;
	return true;
}

int main() {
	srand((unsigned)time(NULL));
	
	int size = 10000000;
	int range = 10000000;
	
	auto arr1 = MakeRandomArray(size, range);
	auto arr2 = CopyArray2Vector(arr1, size);
	auto arr3 = CopyArray(arr1, size);
	
	int start, end;
	
	start = clock();
	APS::Sort(arr1, size);
	end = clock();
	cout << "QUICK APS : " << end - start << "ms" << endl;
	cout << "Accuracy : " << CheckAccuracy(arr1, size) << endl << endl;
	
	start = clock();
	std::sort(arr2.begin(), arr2.end());
	end = clock();
	cout << "std::sort : " << end - start << "ms" << endl;
	cout << "Accuracy : " << CheckAccuracy(arr2) << endl << endl;

	start = clock();
	std::qsort(arr3, size, sizeof(int), compare);
	end = clock();
	cout << "std::qsort : " << end - start << "ms" << endl;
	cout << "Accuracy : " << CheckAccuracy(arr3, size) << endl << endl;

	delete[] arr1, arr3;
	return 0;
}