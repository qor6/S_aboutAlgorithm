#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;  

int main(void) {
	
	int N = 0;
	int M = 0;
	
	cin >> N >> M;
	
	int num[N] = {0, };
	for(int z = 0; z < N; z++) {
		num[z] = z + 1;
	}
	
	for(int x = 0; x < M; x++) {
		int i = 0;
		int j = 0;
		
		cin >> i >> j;
		
		reverse(num+(i-1), num + j);

	}
	
	for(int i = 0; i < N; i++) {
		cout << num[i] << " ";
	}
	
}
