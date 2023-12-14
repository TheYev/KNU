#include <iostream>

using namespace std;

int f(int a) {
    if(a>=10000){
        return a;
    }
    else {
        return f(a+1);
    }
}

int main() {
    int a = 0;
    int b = f(a);
    cout << b;

    return 0;
}