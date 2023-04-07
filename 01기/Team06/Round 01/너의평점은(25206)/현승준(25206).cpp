#include <iostream>
#define endl '\n'
using namespace std;

float convert_grade(string grade);

int main()
{
    // 과목, 학점, 등급, 등급-과목평점, 전공과목별 (학점 × 과목평점)의 합, 학점의 총합, 전공평점
    string object;
    float credit;
    string grade;
    float grade_n;
    float total = 0;
    float credit_sum = 0;
    float result;

    for (int i = 0; i < 20; i++) {
        // 과목, 학점, 등급 차례로 받기
        cin >> object >> credit >> grade;

        // P를 제외한 학점의 경우
        if (grade != "P") {
            credit_sum += credit;
            grade_n = convert_grade(grade);
            total += (credit * grade_n);
        }
        // P일 경우
        else
            continue;
    }

    // 전공평점 = 전공과목별 (학점 × 과목평점)의 합 / 학점의 총합
    result = total / credit_sum;

    cout << fixed;
    cout.precision(6);
    cout << result;

    return 0;
}

// 등급을 과목평점으로 바꿔주는 함수
float convert_grade(string grade) {
    if (grade == "A+")
        return 4.5;
    else if (grade == "A0")
        return 4.0;
    else if (grade == "B+")
        return 3.5;
    else if (grade == "B0")
        return 3.0;
    else if (grade == "C+")
        return 2.5;
    else if (grade == "C0")
        return 2.0;
    else if (grade == "D+")
        return 1.5;
    else if (grade == "D0")
        return 1.0;
    else if (grade == "F")
        return 0.0;
    else
        return -1;
}
