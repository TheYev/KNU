#include <iostream>
#include <thread>
#include <mutex>
#include <chrono>
#include <string>

int f(int x) {
    std::this_thread::sleep_for(std::chrono::seconds(2));
    x *= 2;

    return x; 
}

int g(int x) {
    std::this_thread::sleep_for(std::chrono::seconds(2));
    x += 3;

    return x; 
}

int main() {
    std::string input;
    
    do {
        int x = 0;
        int result_f = 0;
        int result_g = 0;

        std::cout << "Enter a number or 'exit': ";
        std::cin >> input;

        if (input == "exit") {
            break;
        }

        try {
            x = std::stoi(input);
        } catch (...) {
            std::cerr << "Invalid input. Please enter a valid number." << std::endl;
            continue;
        }

        if(x == 0) {
            return false;
        }

        std::mutex m;

        std::thread thread_f([&]() {
            std::lock_guard<std::mutex> lock(m);
            result_f = f(x);
        });

        std::thread thread_g([&]() {
            std::lock_guard<std::mutex> lock(m);
            result_g = g(x);
        });


        thread_f.join();
        thread_g.join();
        
        std::cout << "Result of f(x): " << result_f << std::endl;
        std::cout << "Result of g(x): " << result_g << std::endl;
        std::cout << "Result of f(x)*g(x): " << result_g * result_f << std::endl;

    } while(true);

    std::cout << "Exit" << std::endl;

    return 0;
}