# Бінарна піраміда. Для заданого масиву ключів (більше 10
# значень, задати випадково – цілі числа з множини [0, 100]) побудувати 
# бінарну піраміду, реалізувати операції додавання елемента, видалення 
# мінімального елемента. Вивести побудовані дерева.
# бінарну піраміду nакож відома як min-heap

import heapq
import random

class MinHeap:
    def __init__(self):
        self.heap = []

    def add_element(self, element):
        heapq.heappush(self.heap, element)

    def remove_min(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            return None

    def build_heap(self, array):
        self.heap = array[:]
        heapq.heapify(self.heap)

    def get_heap(self):
        return self.heap

keys = random.sample(range(101), 15)

# Build piramid
heap = MinHeap()
heap.build_heap(keys)

print("Побудована бінарна піраміда:")
print(heap.get_heap())

# Add
new_element = 50
heap.add_element(new_element)
print("\nПісля додавання елемента", new_element, ":")
print(heap.get_heap())

# Delete
removed_element = heap.remove_min()
print("\nВидалений мінімальний елемент:", removed_element)
print("Після видалення мінімального елемента:")
print(heap.get_heap())
