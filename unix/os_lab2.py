import threading
import time

# Оголошення констант для кількості філософів та виділених вилок
num_philosophers = 5
num_forks = num_philosophers

# Оголошення вилок за допомогою locks
forks = [threading.Lock() for _ in range(num_forks)]

# Оголошення функції-потоку філософа
def philosopher(index):
    left_fork_index = index
    right_fork_index = (index + 1) % num_forks
    
    while True:
        print(f"Philosopher {index} is thinking...")
        time.sleep(2)  # Затримка від 2 секунд

        # Блокуємо доступ до вилок
        forks[left_fork_index].acquire()
        forks[right_fork_index].acquire()

        print(f"Philosopher {index} is eating...")
        time.sleep(2)  # Затримка від 2 секунд

        # Звільняємо вилок
        forks[left_fork_index].release()
        forks[right_fork_index].release()

# Створення потоків для кожного філософа
philosopher_threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(num_philosophers)]
for thread in philosopher_threads:
    thread.start()

# Очікування завершення всіх потоків філософів
for thread in philosopher_threads:
    thread.join()
