#include <iostream>
#include <algorithm>
#define endl '\n'
using namespace std;

int main()
{
    // 바구니 N개(1~N) M번 뒤집기
    int N, M;

    cin >> N >> M;

    // 바구니 수 만큼 배열 생성
    int* arr = new int[N];

    // 바구니 숫자 부여
    for (int i = 0; i < N; i++) {
        arr[i] = i + 1;
    }

    // from바구니부터 to바구니까지 뒤집기
    int from, to;

    // M번 반복해서 뒤집기
    for (int i = 0; i < M; i++) {
        cin >> from >> to;

        reverse(arr + (from - 1), arr + to);

        // 바구니가 잘 뒤집어지는지 확인용
        /*for (int i = 0; i < N; i++) {
            cout << arr[i];
        }
        cout << endl;*/
    }

    for (int i = 0; i < N; i++) {
        cout << arr[i];
        if (i == N - 1)
            break;
        cout << ' ';
    }

    return 0;
}