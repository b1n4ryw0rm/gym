#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    int rDay, rMonth, rYear;
    int dDay, dMonth, dYear;
    int fine = 0;

    cin >> rDay >> rMonth >> rYear;
    cin >> dDay >> dMonth >> dYear;

    if ((rYear - dYear) >= 1){
      fine =  10000;
    }
    else if ((rDay - dDay) >= 1 && rMonth == dMonth && rYear == dYear){
      fine = 15 * (rDay - dDay);
    }
    else if ((rMonth - dMonth) >= 1 && rYear == dYear){
      fine = 500 * (rMonth - dMonth);
    }
    
    cout << fine << endl;
    
    return 0;
}

