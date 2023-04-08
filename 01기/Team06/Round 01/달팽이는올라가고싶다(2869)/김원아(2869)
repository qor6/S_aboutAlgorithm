#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;  
 
int main(void){
    int A, B, V;
    cin >> A >> B >> V;
 
    int n = 0;
    
    // A가 마지막날 단번에 올라갈 수 있는 거리를 제외한 막대의 길이 % 올라가는 거리와 미끄러지는 거리의 편차가 0이라면,  
    if( (V - A) % (A - B) == 0){  
        n = (V - A) / (A - B) + 1;
    }
    else{
        n = (V - A) / (A - B) + 2;
    }
    cout << n;
    
}
