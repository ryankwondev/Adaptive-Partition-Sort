#include <iostream>
#include <ctime>
#include <algorithm>
#include <vector>
#include "APS.h"
#include "IntroSort.h"
#include "TimSort.h"
#include "Array.h"
using namespace std;

int compare(const void* a, const void* b) {
	const int* x = (int*)a;
	const int* y = (int*)b;

	if (*x > *y) return 1;
	else if (*x < *y) return -1;
	return 0;
}

int main() {
	srand((unsigned)time(NULL));
	
	int size = 1000000;
	int range = 1000000;
	
	Array array;
	array.CreateRandomArray(size, range);

	Array arr;
	int start, end;
	
	start = clock();
	arr = array;
	APS::Sort(arr.GetArr(), arr.GetSize());
	end = clock();
	cout << "ATS : " << end - start << "ms" << endl;
	cout << "Accuracy : " << arr.CheckSorted() << endl << endl;

	arr = array;
	start = clock();
	IntroSort::Sort(arr.GetArr(), arr.GetSize());
	end = clock();
	cout << "Intro Sort : " << end - start << "ms" << endl;
	cout << "Accuracy : " << arr.CheckSorted() << endl << endl;

	arr = array;
	start = clock();
	TimSort::Sort(arr.GetArr(), arr.GetSize());
	end = clock();
	cout << "Tim Sort : " << end - start << "ms" << endl;
	cout << "Accuracy : " << arr.CheckSorted() << endl << endl;

	cout << endl;
	cout << "=== C/C++ Standard Sorting Algorithms ===" << endl << endl;
	arr = array;
	start = clock();
	std::sort(arr.GetVector()->begin(), arr.GetVector()->end());
	end = clock();
	cout << "std::sort : " << end - start << "ms" << endl;
	cout << "Accuracy : " << arr.CheckSorted() << endl << endl;

	arr = array;
	start = clock();
	std::qsort(arr.GetArr(), arr.GetSize(), sizeof(int), compare);
	end = clock();
	cout << "std::qsort : " << end - start << "ms" << endl;
	cout << "Accuracy : " << arr.CheckSorted() << endl << endl;
	return 0;
}