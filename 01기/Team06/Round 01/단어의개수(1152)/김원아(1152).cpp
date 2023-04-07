#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;  

int main(void) {

	string input = "";
	
	getline(cin, input);
	
	int length = input.length();
	int count = 0;
	
	if(input.empty()){
		cout << 0;
		return 0;
	}
	
	for(int i = 0; i < length; i++) {
		if(input[i] == ' ') 
			count++;
	}
	if(input[0] == ' ')
		count--;
	count++;
	cout << count;
	
}
