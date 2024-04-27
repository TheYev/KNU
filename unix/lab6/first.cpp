#include <iostream>
#include <vector>
#include <thread>
#include <chrono>

using namespace std;

void multiply(const vector<vector<int>>& A, const vector<vector<int>>& B,
    vector<vector<int>>& result, int row, int col) {
    int sum = 0;
    for (size_t i = 0; i < A[row].size(); ++i) {
        sum += A[row][i] * B[i][col];
    }
    result[row][col] = sum;
}

void printResult(const vector<vector<int>>& result) {
    for (size_t i = 0; i < result.size(); ++i) {
        for (size_t j = 0; j < result[0].size(); ++j) {
            cout << "[" << i << "," << j << "]=" << result[i][j] << " ";
        }
       cout << endl;
    }
}

int main() {
    int n = 3;
    int m = 3;
    int k = 3;

    vector<vector<int>> A(n, vector<int>(m, 1));
    vector<vector<int>> B(m, vector<int>(k, 2));

    vector<vector<int>> result(n, vector<int>(k, 0));

    vector<int> numThreadsList = { 1, 2, 4, 8, 16 };

    for (int numThreads : numThreadsList) {
        auto start = chrono::high_resolution_clock::now();

        vector<thread> threads;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < k; ++j) {
                threads.emplace_back(thread(multiply,ref(A), ref(B), ref(result), i, j));
            }
        }
        printResult(result);
        for (auto& thread : threads) {
            thread.join();
        }

        auto end = chrono::high_resolution_clock::now();

        chrono::duration<double> duration = end - start;
        cout << "Time taken with " << numThreads << " threads: " << duration.count() << " seconds" << endl;
    }

    return 0;
}