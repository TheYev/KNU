# Біноміальні піраміди. Для заданого масиву ключів (більше 15 
# значень, задати випадково – цілі числа з множини [0, 100]) побудувати 
# біноміальну піраміду, реалізувати операції додавання елемента, видалення 
# мінімального елемента. Вивести побудовані дерева.

import random

class BinomialHeapNode:
    def __init__(self, value):
        self.value = value
        self.degree = 0
        self.child = None
        self.sibling = None
        self.parent = None

class BinomialHeap:
    def __init__(self):
        self.head = None

    def merge_heaps(self, heap1, heap2):
        if heap1 is None:
            return heap2
        if heap2 is None:
            return heap1

        if heap1.value < heap2.value:
            heap1.sibling = self.merge_heaps(heap1.sibling, heap2)
            heap1.sibling.parent = heap1
            return heap1
        else:
            heap2.sibling = self.merge_heaps(heap1, heap2.sibling)
            heap2.sibling.parent = heap2
            return heap2

    def insert(self, value):
        new_heap = BinomialHeap()
        new_heap.head = BinomialHeapNode(value)
        self.head = self.merge_heaps(self.head, new_heap.head)

    def get_min(self):
        if self.head is None:
            return None

        min_node = self.head
        current = self.head.sibling

        while current is not None:
            if current.value < min_node.value:
                min_node = current
            current = current.sibling

        return min_node.value

    def extract_min(self):
        if self.head is None:
            return None

        min_node = self.head
        prev_node = None
        current = self.head
        min_value = min_node.value

        while current.sibling is not None:
            if current.sibling.value < min_value:
                min_node = current.sibling
                prev_node = current

            current = current.sibling

        if prev_node is None:
            self.head = min_node.sibling
        else:
            prev_node.sibling = min_node.sibling

        if min_node.child is not None:
            new_head = None
            child = min_node.child

            while child is not None:
                next_child = child.sibling
                child.parent = None
                child.sibling = new_head
                new_head = child
                child = next_child

            child_heap = BinomialHeap()
            child_heap.head = new_head
            self.head = self.merge_heaps(self.head, child_heap.head)

        return min_value

    def print_heap(self):
        if self.head is None:
            print("Heap is empty")
            return

        nodes = []
        current = self.head

        while current is not None:
            nodes.append(str(current.value))
            current = current.sibling

        print("Binomial Heap: " + " -> ".join(nodes))

# Приклад використання

keys = random.sample(range(101), 15)
heap = BinomialHeap()

for num in keys:
    heap.insert(num)

print("Побудована біноміальна піраміда:")
heap.print_heap()

print("Мінімальний елемент:", heap.get_min())

min_value = heap.extract_min()
print("Видалений мінімальний елемент:", min_value)

print("Біноміальна піраміда після видалення мінімального елемента:")
heap.print_heap()