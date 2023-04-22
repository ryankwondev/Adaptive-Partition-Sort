#include "Array.h"

Array::Array() {
	this->arr = nullptr;
	this->vec.clear();
	this->size = 0;
}

Array::Array(Array& arr) {
	this->arr = new int[arr.GetSize()];
	for (int i = 0; i < arr.GetSize(); i++) {
		this->arr[i] = arr.arr[i];
	}
	this->vec = arr.vec;
	this->size = arr.GetSize();
}

Array::~Array() {
	this->Clear();
}

void Array::CreateRandomArray(int size, int range) {
	this->Clear();
	this->arr = new int[size];
	for (int i = 0; i < size; i++) {
		arr[i] = rand() % range;
		this->vec.push_back(arr[i]);
	}
	this->size = size;
}

bool Array::CheckSorted() {
	bool arr_chk = true;
	bool vec_chk = true;
	for (int i = 0; i < this->GetSize() - 1; i++) {
		if (this->arr[i] > this->arr[i + 1]) arr_chk = false;
		if (this->vec[i] > this->vec[i + 1]) vec_chk = false;
	}
	return arr_chk || vec_chk;
}

int Array::GetSize() {
	return this->size;
}

vector<int>* Array::GetVector() {
    return &this->vec;
}

int* Array::GetArr() {
	return this->arr;
}

void Array::operator=(Array& src) {
	this->Clear();
	this->arr = new int[src.GetSize()];
	for (int i = 0; i < src.GetSize(); i++) {
		this->arr[i] = src.arr[i];
	}
	this->vec = src.vec;
	this->size = src.GetSize();
}

void Array::PrintVec() {
	cout << "[ ";
	for (int i = 0; i < this->vec.size(); i++) {
		if (i) cout << ", ";
		cout << vec[i];
	}
	cout << " ]";
}

void Array::PrintArr() {
	cout << "[ ";
	for (int i = 0; i < this->GetSize(); i++) {
		if (i) cout << ", ";
		cout << arr[i];
	}
	cout << " ]" << endl;
}

void Array::Clear() {
	this->vec.clear();
	this->size = 0;
	if (this->arr) delete[] this->arr;
	this->arr = nullptr;
}
