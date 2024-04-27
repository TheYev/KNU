#include <iostream>
#include <thread>
#include <chrono>

using namespace std;

void increment(int& sharedVariable, int iterations) {
    for (int i = 0; i < iterations; ++i) {
        ++sharedVariable;
    }
}

int main() {
    int sharedVariable = 0;
    int iterations = 1000000000; // 10^9, 1000000000

    auto start = chrono::high_resolution_clock::now();

    thread thread1(increment, ref(sharedVariable), iterations);
    thread thread2(increment, ref(sharedVariable), iterations);

    thread1.join();
    thread2.join();

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;

    cout << "Result without mutex: " << sharedVariable << endl;
    cout << "Time: " << duration.count() << "seconds" << endl;

    return 0;
}