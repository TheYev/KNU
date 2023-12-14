#include <iostream>
#include <string>
//w = w1w0w2
using namespace std;

enum State {
	START,
	A,
	AB,
	ABC,
	F,
	EState  
};

bool checkAutomat(State state) {
	if (state == ABC) {
		return 1;
	}
	else if (state == A) {
		return 1;
	}
	else if (state == F) {
		return 1;
	}
	else {
		return 0;
	}
}

State findStateAutomat(const string& input) {
	State currentState = START;
	for (char c : input) {
		switch (currentState) {
		case START:
			if (c == 'a') currentState = A;
			else currentState = EState;
			break;
		case A:
			if (c == 'b') currentState = AB;
			else if (c == 'f') currentState = F;
			else currentState = EState;
			break;
		case AB:
			if (c == 'c') currentState = ABC;
			else currentState = EState;
			break;
		case ABC:
			if (c == 'f') currentState = A;
			else currentState = EState;
			break;
		case EState:
			break;
		}
	}
	return currentState;
}

int main() {
	//string w1 = "abc";
	//string w2 = "abc";
	//string w0 = "abc";


	/*string w1 = "abcf";
	string w2 = "abf";
	string w0 = "abc";*/


	/*string w1 = "abcf";
	string w2 = "abcf";
	string w0 = "af";*/

	/*string w1 = "a3";
	string w2 = "a4";
	string w0 = "a5";*/

	/*string w1 = "a";
	string w2 = "a4";
	string w0 = "a5";*/

	string w1 = "1";
	string w2 = "2";
	string w0 = "3";



	State w1State = findStateAutomat(w1);
	if (checkAutomat(w1State)) {
		State w0State = findStateAutomat(w0);

		if (checkAutomat(w0State)) {
			State w2State = findStateAutomat(w2);

			if (checkAutomat(w2State)) {
				cout << "Line w = w1w0w2 allowed automat." << endl;
			}
			else {
				cout << "Line w2 not allowed automat." << endl;
			}
		}
		else {
			cout << "Line w0 not allowed automat." << endl;
		}
	}
	else {
		cout << "Line w1 not allowed automat." << endl;
	}

	return 0;
}
