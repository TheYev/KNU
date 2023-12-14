#include <iostream>
#include <vector>
#include <thread>
#include <algorithm>
#include <chrono>
#include <cstdlib>
#include <fstream>


using namespace std;

bool predicate(int value) {
	// returns true if the value is even
	return value % 2 == 0;
}

// parallel count_if algorithm
int p_count_if(const vector<int>& data, int num_threads, int chunk_size) {
	vector<thread> threads;
	vector<int> partial_results(num_threads, 0);
	int data_size = static_cast<int>(data.size());

	for (int i = 0; i < num_threads; ++i) {
		threads.emplace_back([i, chunk_size, &data, &partial_results, data_size, num_threads]() {
			int start = i * chunk_size;
			int end = (i == num_threads - 1) ? data_size : start + chunk_size;
			partial_results[i] = count_if(data.begin() + start, data.begin() + end, predicate);
			});
	}

	for (auto& thread : threads) {
		thread.join();
	}

	// merge res
	int total_count = 0;
	for (int count : partial_results) {
		total_count += count;
	}

	return total_count;
}


void test_p_count_if(const vector<int>& data, int max_threads, const string& our_file) {
	ofstream write_file(our_file);

	if (!write_file) {
		cerr << "could not open file: " << endl;
		return;
	}

	write_file << "K | Seconds:" << endl;
	cout << "K | Seconds:" << endl;

	for (int k = 1; k <= max_threads; ++k) {
		int chunk_size = static_cast<int>(data.size()) / k;

		auto start_time = chrono::high_resolution_clock::now();
		int count = p_count_if(data, k, chunk_size);
		auto end_time = chrono::high_resolution_clock::now();

		chrono::duration<double> res_time = end_time - start_time;
		write_file << k << " | " << res_time.count() << endl;
		cout << k << " | " << res_time.count() << endl;
	}
	write_file.close();
}

void random_val(vector<int>& data) {

	for (size_t i = 0; i < data.size(); ++i) {
		data[i] = rand() % 1000;
	}
}

int main() {
	vector<int> data(10000);
	// populate the data with random values or according to your experiment

	//random_val(data);
	for (int& element : data) {
		 element = 2;
	 }

	int num_threads = 4;
	//int num_threads = thread::hardware_concurrency();

	auto start_time = chrono::high_resolution_clock::now();
	int chunk_size = static_cast<int>(data.size()) / num_threads;
	int count = p_count_if(data, num_threads, chunk_size);
	auto end_time = chrono::high_resolution_clock::now();

	chrono::duration<double> res_time = end_time - start_time;

	//int max_threads = thread::hardware_concurrency(); // hardware count thread
	int max_threads = num_threads; //variable num_threads
	string our_file = "tets.txt";

	test_p_count_if(data, max_threads, our_file);


	cout << "Parallel count_if with " << num_threads << " threads duration: " << res_time.count() << " seconds\n";
	cout << "Count: " << count << endl;

	return 0;
}
