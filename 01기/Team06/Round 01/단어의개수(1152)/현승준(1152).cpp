#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#define endl '\n'
using namespace std;

int main()
{
    // 문장을 입력하면 한 줄에 다 받아서 str에 저장
    string str;
    getline(cin, str);

    // str을 공백을 기준으로 쪼개서 str2에 저장하기 위함
    istringstream iss(str);
    string stringBuffer;
    vector<string> str2;
    str2.clear();

    while (getline(iss, stringBuffer, ' ')) {
        str2.push_back(stringBuffer);
        // 공백을 기준으로 단어가 잘리는지 확인
        //cout << stringBuffer << ' ';
    }

    // 잘린 단어가 str2에 잘 들어있는지 확인
    /*for (int i = 0; i < str2.size(); i++) {
        cout << str2[i] << endl;
    }*/

    // str 시작이 공백이였으면 str2[0]에 널 값이 저장되어있으므로 1 빼주기
    if (str2[0] == "\0")
        cout << (str2.size() - 1);
    else
        cout << str2.size();

    return 0;
}
