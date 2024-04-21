# Клас вузла червоно-чорного дерева
import sys

class Node:
    def __init__(self, value, color="RED"):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


# Клас червоно-чорного дерева
class RedBlackTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            node.color = "BLACK"
        else:
            self._insert_helper(node, self.root)
            self._fix_insert(node)

    def _insert_helper(self, node, root):
        if node.value < root.value:
            if root.left is None:
                root.left = node
                node.parent = root
            else:
                self._insert_helper(node, root.left)
        else:
            if root.right is None:
                root.right = node
                node.parent = root
            else:
                self._insert_helper(node, root.right)

    # Метод для виправлення червоно-чорного дерева після вставки нового вузла
    def _fix_insert(self, node):
        while node.parent is not None and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._left_rotate(node.parent.parent)
        self.root.color = "BLACK"

    # Метод для лівого повороту
    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    # Метод для правого повороту
    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child
        left_child.right = node
        node.parent = left_child

    def remove(self, value):
        node = self._search(value)
        if node is not None:
            self._remove_node(node)
            
    def _remove_node(self, node):
        if node.left is not None and node.right is not None:
            successor = self._find_min(node.right)
            node.value = successor.value
            node = successor
        if node.left is None and node.right is None:
            if node.color == "BLACK":
                self._fix_delete(node)
            if node.parent is not None:
                if node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                self.root = None
        elif node.left is not None:
            child = node.left
            self._replace_node(node, child)
        else:
            child = node.right
            self._replace_node(node, child)
        del node

    # Інтерфейс для пошуку вузла в червоно-чорному дереві
    def _search(self, value):
        return self._search_helper(value, self.root)

    # Метод для пошуку вузла в червоно-чорному дереві
    def _search_helper(self, value, node):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_helper(value, node.left)
        else:
            return self._search_helper(value, node.right)


    # Метод для заміни вузла
    def _replace_node(self, node, child):
        if node.parent is not None:
            if node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child
        else:
            self.root = child
        if child is not None:
            child.parent = node.parent
            child.color = "BLACK"

    # Метод для виправлення дерева після видалення вузла
    def _fix_delete(self, node):
        while node != self.root and node.color == "BLACK":
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    node.parent.color = "RED"
                    self._left_rotate(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == "BLACK" and sibling.right.color == "BLACK":
                    sibling.color = "RED"
                    node = node.parent
                else:
                    if sibling.right.color == "BLACK":
                        sibling.left.color = "BLACK"
                        sibling.color = "RED"
                        self._right_rotate(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = "BLACK"
                    sibling.right.color = "BLACK"
                    self._left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    node.parent.color = "RED"
                    self._right_rotate(node.parent)
                    sibling = node.parent.left
                if sibling.right.color == "BLACK" and sibling.left.color == "BLACK":
                    sibling.color = "RED"
                    node = node.parent
                else:
                    if sibling.left.color == "BLACK":
                        sibling.right.color = "BLACK"
                        sibling.color = "RED"
                        self._left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = "BLACK"
                    sibling.left.color = "BLACK"
                    self._right_rotate(node.parent)
                    node = self.root
        node.color = "BLACK"

    # Метод для пошуку мінімального вузла в дереві
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    # Метод для проходу по червоно-чорному дереву
    def _traverse_in_order(self, node):
        if node is not None:
            self._traverse_in_order(node.left)
            print(node.value, end=' ')
            self._traverse_in_order(node.right)

    # Інтерфейс для виведення червоно-чорного дерева
    def print_tree(self):
        self._traverse_in_order(self.root)



# Заданий масив з 20 значень
array = [15, 10, 20, 8, 12, 17, 25, 6, 9, 11, 14, 16, 18, 23, 27, 5, 7, 13, 19, 22]

# Побудова червоно-чорного дерева
rb_tree = RedBlackTree()
for value in array:
    rb_tree.insert(value)

# Виведення побудованого дерева
print("Побудоване червоно-чорне дерево:")
rb_tree.print_tree()

# Додавання нового елемента
new_element = 21
rb_tree.insert(new_element)
print(f"\nДодано новий елемент {new_element}:")
rb_tree.print_tree()

# Видалення елемента
element_to_remove = 14
rb_tree.remove(element_to_remove)
print(f"\nВидалено елемент {element_to_remove}:")
rb_tree.print_tree()