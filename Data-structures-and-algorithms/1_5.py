# Бінарне дерево пошуку. Для заданого масиву ключів (більше 10
# значень, задати випадково – цілі числа з множини [0, 100]) побудувати 
# бінарне дерево пошуку, реалізувати всі варіанти обходів (прямий, обернений, 
# симетричний). Вивести побудоване дерево і результати обходів.

import random

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

# Build binar tree
def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def print_tree(root, level=0):
    if root is not None:
        print_tree(root.right, level + 1)
        print(' ' * 4 * level + '->', root.val)
        print_tree(root.left, level + 1)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")

keys = random.sample(range(101), 15)

# Build binar tree
root = None
for key in keys:
    root = insert(root, key)

print("Побудоване бінарне дерево пошуку:")
print_tree(root)

print("\nПрямий обхід:")
preorder_traversal(root)
print("\nОбернений обхід:")
postorder_traversal(root)
print("\nСиметричний обхід:")
inorder_traversal(root)
