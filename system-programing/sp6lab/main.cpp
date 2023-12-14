#include <iostream>

using namespace std;

int f(int a) {
    if(a>=100000){
        return a;
    }
    else {
        int b = a+1;
        return f(b);
    }
}

int main() {
    int a = 0;
    int b = f(a);
    cout << b;

    return 0;
}