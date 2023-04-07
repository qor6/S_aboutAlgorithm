#include <iostream>
//#include <cmath>
#define endl '\n'
using namespace std;

int main()
{
    // 낮올라감, 밤내려옴, 하루움직임, 나무길이, 달팽이위치, 날짜
    int up;
    int down;
    int day_up;
    int tree;
    int location = 0;
    int day = 0;

    cin >> up >> down >> tree;

    // 한번 나무 길이를 넘어서면 내려오는 것은 고려하지 않음
    /*while (location < tree - up) {
        location += (up - down);
        day++;
    }
    day++;*/

    // 하루동안 움직이는 거리
    day_up = up - down;

    //day = ceil(1.0 * (tree - up) / day_up); // 아래 3줄과 같은 기능
    
    // 날짜 계산
    day = (tree - up) / day_up;
    if ((tree - up) % day_up > 0) // 예) 6 1 12
        day++;
    location = day_up * day;

    location += up;
    day++;

    cout << day;

    return 0;
}
