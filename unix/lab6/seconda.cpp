#include <iostream>
#include <thread>
#include <mutex>
#include <chrono>

using namespace std;

mutex mtx;

void increment(int& sharedVariable, int iterations) {
    for (int i = 0; i < iterations; ++i) {
        mtx.lock(); 
        ++sharedVariable;
        mtx.unlock(); 
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

    cout << "Result with mutex: " << sharedVariable << endl;
    cout << "Time: " << duration.count() << "seconds" << endl;

    return 0;
}