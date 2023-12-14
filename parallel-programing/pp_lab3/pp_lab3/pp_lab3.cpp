#include <iostream>
#include <thread>
#include <mutex>
#include <vector>
#include <queue>
#include <unordered_map>
#include <fstream>

using namespace std;

//our file
ofstream output("results.txt");

// Implementation of function f to perform actions
void f(const string& action, int index) {
	// Output a message before the action is executed
	{
		static mutex printMutex;
		lock_guard<mutex> lock(printMutex);
		output << "From the set " << action << " action performed " << index + 1 << ".\n";
		cout << "From the set " << action << " action performed " << index + 1 << ".\n";
	}

	// Simulation of calculation duration
	this_thread::sleep_for(chrono::seconds(1));// Replace this with the actual compute process
}

// Class to represent the graph
class Graph {
public:
	unordered_map<char, vector<char>> adjacencyList;

	// Adding connections to the graph
	void addEdge(char start, char end) {
		adjacencyList[start].push_back(end);
	}
};

// Function for performing actions based on graph structure and flow management
void performActions(const Graph& graph) {
	queue<char> availableTasks;
	mutex taskQueueMutex;

	// Add the corresponding initial actions to the queue
	availableTasks.push('a');
	availableTasks.push('b');
	availableTasks.push('c');
	availableTasks.push('d');

	// Set the number of threads
	const int threadCount = 7;
	vector<thread> threads(threadCount);

	// Create and run threads
	for (int i = 0; i < threadCount; ++i) {
		threads[i] = thread([&]() {
			while (true) {
				char currentTask;
				{
					lock_guard<mutex> lock(taskQueueMutex);
					if (availableTasks.empty()) {
						break; // Exit if tasks are finished
					}
					currentTask = availableTasks.front();
					availableTasks.pop();
				}

				// Execution of the action
				f(string(1, currentTask), 0);

				// Add the following actions to the queue
				auto it = graph.adjacencyList.find(currentTask);
				if (it != graph.adjacencyList.end()) {
					for (char nextTask : it->second) {
						lock_guard<mutex> lock(taskQueueMutex);
						availableTasks.push(nextTask);
					}
				}
				else {
					output << "Error: Key " << currentTask << " missing in the graph.\n";
					cout << "Error: Key " << currentTask << " missing in the graph.\n";
				}
			}
			});
	}

	// Wait for all threads to finish
	for (auto& thread : threads) {
		thread.join();
	}
}

int main() {
	// Start calculations
	output << "The calculation has started.\n";
	cout << "The calculation has started.\n";

	// Creating a graph structure
	Graph graph;
	graph.addEdge('a', 'b');
	graph.addEdge('a', 'c');
	graph.addEdge('a', 'd');
	graph.addEdge('b', 'l');
	graph.addEdge('c', 'f');
	graph.addEdge('c', 'g');
	graph.addEdge('d', 'h');
	graph.addEdge('l', 'i');
	graph.addEdge('f', 'i');
	graph.addEdge('g', 'j');
	graph.addEdge('h', 'j');

	// Call the function to perform actions depending on the graph structure
	performActions(graph);

	// Completion of calculations
	output << "The calculation is complete..\n";
	cout << "The calculation is complete..\n";

	return 0;
}
