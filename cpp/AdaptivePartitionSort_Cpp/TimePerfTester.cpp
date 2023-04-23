#include "TimePerfTester.h"
#include <string>
using namespace std;

void TimePerfTester::SetRandomTestcases(int testcase_num, int array_size, int array_range) {
	this->testcase.clear();
	for (int i = 0; i < testcase_num; i++) {
		this->testcase.push_back(Array());
		this->testcase.back().CreateRandomArray(array_size, array_range);
	}
}

void TimePerfTester::SetTestcases(Testcase& testcase) {
	this->testcase.clear();
	for (int i = 0; i < testcase.size(); i++) {
		this->testcase.push_back(testcase[i]);
	}
}

void TimePerfTester::TestAlgorithm(void(*Sort)(int*, unsigned int)) {
	this->min_time = -1;
	this->max_time = -1;
	this->error_cnt = 0;
	this->time.clear();
	double total = 0;
	for (int i = 0; i < this->testcase.size(); i++) {
		Array a = this->testcase[i];
		
		int* arr = a.GetArr();
		unsigned int size = a.GetSize();

		auto begin_time = chrono::high_resolution_clock::now();
		Sort(arr, size);
		auto end_time = chrono::high_resolution_clock::now();
		
		chrono::duration<double> duration = end_time - begin_time;
		double t = duration.count() * 1000.0;

		if (this->min_time == -1) this->min_time = t;
		else this->min_time = min(t, this->min_time);
		this->max_time = max(t, this->max_time);
		total += t;
		this->time.push_back(t);

		this->error_cnt += !a.CheckSorted();
	}
	this->avg_time = total / (double)this->testcase.size();
}

double TimePerfTester::GetElapsedTime(TimeType type) {
	switch (type) {
	case MIN: return this->min_time;
	case MAX: return this->max_time;
	case AVG: return this->avg_time;
	}
	return -1;
}

vector<double> TimePerfTester::GetElapsedTimeList() {
	return this->time;
}

bool TimePerfTester::GetAccuracy() {
	return !this->error_cnt;
}

int TimePerfTester::GetErrorCount() {
	return this->error_cnt;
}

string TimePerfTester::GetResultAsStyledString(string algorithm_name) {
	string str = "";
	str += "[" + algorithm_name + " Test Result" + "]\n";
	str += "INFO : Testcase Size : " + to_string(this->testcase.size()) + " | ";
	if (!this->testcase.empty()) {
		str += "Array Size : " + to_string(this->testcase.front().GetSize());
	}
	str += "\n";
	str += "> Best Time : " + to_string(this->min_time) + " sec" + "\n";
	str += "> Worst Time : " + to_string(this->max_time) + " sec" + "\n";
	str += "> Average Time : " + to_string(this->avg_time) + " sec" + "\n";
	str += "Sorting ";
	str += (this->GetAccuracy() ? "Succeed" : "Failed");
	str += "\n";
	str += "¤¤Error Count : " + to_string(this->GetErrorCount()) + "\n";
	return str;
}

Testcase TimePerfTester::GetTestcase() {
	return this->testcase;
}
