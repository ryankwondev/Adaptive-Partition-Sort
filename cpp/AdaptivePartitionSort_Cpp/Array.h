#pragma once
#include <iostream>
#include <vector>
using namespace std;

class Array {
public:
	Array();
	Array(const Array& arr);
	~Array();
	void CreateRandomArray(int size, int range);
	bool CheckSorted();
	int GetSize() const;

	vector<int>* GetVector();
	int* GetArr();

	void operator= (Array& src);

	void PrintVec();
	void PrintArr();

private:
	vector<int> vec;
	int* arr;	
	int size;

	void Clear();
};

