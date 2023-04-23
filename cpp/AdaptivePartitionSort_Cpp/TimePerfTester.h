#pragma once
#include "Array.h"
#include <chrono>
using Testcase = vector<Array>;

enum TimeType {MIN, MAX, AVG};

//Algorithm Time Performance Tester Class
class TimePerfTester {
private:
	Testcase testcase;
	double min_time = 0, max_time = 0, avg_time = 0;
	int error_cnt = -1;
	vector<double> time;

public:
	void SetRandomTestcases(int testcase_num, int array_size, int array_range); //Set Testcase as random arrays
	void SetTestcases(Testcase &testcase); //Set Testcase as "testcase"
	
	void TestAlgorithm(void (*Sort)(int*, unsigned int)); //Testring Algorithm (Parameter : Algorithm Function (Function Type : [Name](int* arr, unsigned int size)))
	
	double GetElapsedTime(TimeType type); //Get Min/Max/Avg Elapsed Time
	vector<double> GetElapsedTimeList(); //Get Whole Elapsed Time List
	bool GetAccuracy(); //If Passes All the Testcases : True, Else : False
	int GetErrorCount(); //Get the Number of Testcases that did not pass
	std::string GetResultAsStyledString(string algorithm_name); //Get Result as Styled String
	Testcase GetTestcase(); //Get Current Testcase
};

