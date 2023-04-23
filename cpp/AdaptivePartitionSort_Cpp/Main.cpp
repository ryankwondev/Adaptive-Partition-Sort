#include <iostream>
#include <ctime>
#include <algorithm>
#include <vector>
#include "TimePerfTester.h"
#include "APS.h"
#include "IntroSort.h"
#include "TimSort.h"
using namespace std;

int main(int argc, char *argv[]) {
	TimePerfTester tester;
	tester.SetRandomTestcases(10, 1000000, 1000000);
	
	tester.TestAlgorithm(APS::Sort);
	cout << tester.GetResultAsStyledString("Adaptive Partition Sort") << endl;
	
	tester.TestAlgorithm(IntroSort::Sort);
	cout << tester.GetResultAsStyledString("Intro Sort") << endl;
	
	tester.TestAlgorithm(TimSort::Sort);
	cout << tester.GetResultAsStyledString("Tim Sort") << endl;
	return 0;
}