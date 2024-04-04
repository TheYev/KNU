import threading
import time

num_philosophers = 5
num_forks = num_philosophers

forks = [threading.Lock() for _ in range(num_forks)]

def philosopher(index):
    left_fork_index = index
    right_fork_index = (index + 1) % num_forks
    
    while True:
        print(f"Philosopher {index} is thinking...")
        time.sleep(2)  

        forks[left_fork_index].acquire()
        forks[right_fork_index].acquire()

        print(f"Philosopher {index} is eating...")
        time.sleep(2)  

        forks[left_fork_index].release()
        forks[right_fork_index].release()

philosopher_threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(num_philosophers)]
for thread in philosopher_threads:
    thread.start()

for thread in philosopher_threads:
    thread.join()
