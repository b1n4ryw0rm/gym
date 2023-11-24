#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool isPrime(int value){

    if (value <= 1) {
        return false;
    }
    for (int i = 2; i * i <= value; i++) {
        if (value % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n;
    cin >> n;

    for(int i = 0;i < n;i++){
        int dat;
        cin >> dat;
        if (isPrime(dat) == true){
            cout << "Prime" << endl;
        } else {
            cout << "Not prime" << endl;
        }
    }
      
    return 0;
}

