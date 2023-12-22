"""
Реализовать алгоритмы построения, обхода и балансировки дерева бинарного поиска. 
На вход алгоритма подается последовательность целых положительных чисел. 
Программа должна строить BST, добавляя узлы в порядке последовательности. 
Реализовать обходы дерева по возрастанию и по убыванию узлов. 
Реализовать алгоритм нахождения k-го минимального ключа в дереве. 
На его основе сбалансировать построенное дерево (ротациями вправо и влево (n/2)-ый минимальный элемент помещается в корень и это повторяется рекурсией в дочерних узлах).
"""

"""
Балансировка дерева способствует обеспечению лучшей производительности для операций работы с деревом (операций поиска, вставки и удаления в бинарном дереве поиска (BST)).
Когда высота дерева становится значительной, время выполнения базовых операций (поиск, вставка, удаление) может увеличиваться до O(N).
Сбалансированное дерево гарантирует, что высота дерева остается логарифмической относительно количества узлов O(logN), что обеспечивает более эффективные операции.
"""

# Класс для представления узла бинарного дерева
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Функция для вставки узла в дерево бинарного поиска (BST)
def insert(root, key):
    if root is None:
        return TreeNode(key)
    
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    
    return root

# Функция для обхода дерева в порядке возрастания
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

# Функция для обхода дерева в порядке убывания
def reverse_inorder_traversal(root):
    if root:
        reverse_inorder_traversal(root.right)
        print(root.key, end=" ")
        reverse_inorder_traversal(root.left)

# Функция для нахождения k-го минимального ключа в дереве
def kth_smallest(root, k, count=None):
    if count is None:
        count = [0]
    if root:
        left = kth_smallest(root.left, k, count)
        count[0] += 1

        if count[0] == k:
            return root.key

        right = kth_smallest(root.right, k, count)

        return left if left is not None else right
    
# Функция для балансировки дерева
def balance_tree(root):
    if root is None:
        return None
    
    # Построение отсортированного списка ключей
    sorted_keys = []
    inorder_traversal_for_balance(root, sorted_keys)
    
    # Построение сбалансированного дерева из списка ключей
    return sorted_keys_to_bst(sorted_keys)

# Вспомогательная функция для обхода дерева и сбора ключей в отсортированный список
def inorder_traversal_for_balance(root, keys):
    if root:
        inorder_traversal_for_balance(root.left, keys)
        keys.append(root.key)
        inorder_traversal_for_balance(root.right, keys)

# Вспомогательная функция для построения сбалансированного дерева из списка отсортированных ключей
def sorted_keys_to_bst(keys):
    if not keys:
        return None
    
    mid = len(keys) // 2
    root = TreeNode(keys[mid])
    
    root.left = sorted_keys_to_bst(keys[:mid])
    root.right = sorted_keys_to_bst(keys[mid+1:])
    
    return root

values = [50, 30, 20, 40, 70, 60, 80]

bst_root = None
for value in values:
    bst_root = insert(bst_root, value)

print("Inorder Traversal:")
inorder_traversal(bst_root)

print("\nReverse Inorder Traversal:")
reverse_inorder_traversal(bst_root)

k = 3
kth_min = kth_smallest(bst_root, k)
print(f"\n{k}-th smallest element: {kth_min}")

balanced_root = balance_tree(bst_root)
print("\nBalanced Inorder Traversal:")
inorder_traversal(balanced_root)
