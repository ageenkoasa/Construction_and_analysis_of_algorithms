"""
Задание 1:
- Реализовать гибридный алгоритм, сочетающий Quick и Insertion Sort, следующим образом: 
в Quick Sort участки массива длины меньшей некоторого параметра k сортировать вставками, не используя для них рекурсию быстрой сортировки;
- Подобрать оптимальное k для сортировки R массивов длины N, элементы которых - случайные целые числа в диапазоне от 0 до  M;
- Предусмотреть возможность ввода N, R, M;
"""

"""
Алгоритм Quick Sort очень эффективен на практике и часто используется в сортировке больших массивов данных. 
Он имеет среднюю временную сложность O(n log n), где n - количество элементов в массиве, 
но в худшем случае может иметь временную сложность O(n^2) при неудачном выборе опорного элемента.

Insertion Sort эффективен для малых массивов, 
так как его временная сложность в лучшем случае составляет O(n), где n - количество элементов в массиве. 
Однако для больших массивов он менее эффективен, так как его средняя и худшая временные сложности составляют O(n^2).
"""

import random

def generate_random_array(n, m):
    return [random.randint(0, m) for _ in range(n)]

# Функция для сортировки массива вставками по возрастанию
def insertion_sort(arr):
    for i in range(1, len(arr)): # первый элемент (с индексом 0) считается упорядоченным подмассивом
        key = arr[i]
        j = i - 1                # элемент, который будет перемещаться
        while j >= 0 and arr[j] > key: # cравниваем предыдущим элемент c текущим (key)
            arr[j + 1] = arr[j]        # если предыдущий больше, сдвигаем его право
            j -= 1
        arr[j + 1] = key 

"""
! Quick Sort !
Массив разбивается на две части: элементы, меньшие или равные опорному элементу, и элементы, большие опорного элемента. 
Элементы, которые меньше опорного элемента, перемещаются влево, а элементы, большие опорного элемента, перемещаются вправо.
"""
# Функция для разделения массива по опорному элементу (pivot)
def partition(arr, low, high):
    pivot = arr[high] # последний элемент массива
    i = low - 1 # текущий элемент, который меньше или равен pivot (i находится "вне" массива слева от него)

    for j in range(low, high): # j = текущий элемент, который больше pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1 # индекс, на котором находится опорный элемент после разделения

"""
Рекурсивная сортировка подмассивов алгоритмом Quick Sort к левой и правой части массива. 
"""
# Функция для сортировки Quick Sort с использованием вставок для малых подмассивов
def hybrid_quick_sort(arr, low, high, k):
    if low < high:
        if high - low + 1 <= k:
            insertion_sort(arr[low:high+1])
        else:
            pivot_index = partition(arr, low, high)
            # каждая часть разбивается и сортируется независимо:
            hybrid_quick_sort(arr, low, pivot_index - 1, k) # левая часть
            hybrid_quick_sort(arr, pivot_index + 1, high, k) # правая часть

N = int(input("\nВведите длину массивов (N): "))
R = int(input("Введите количество массивов (R): "))
M = int(input("Введите максимальное значение элементов (M): "))

for i in range(R):
    arr = generate_random_array(N, M)
    print(f"\nИсходный массив {i + 1}: {arr}")
    k = N // 10  # выберем k как 10% от N
    hybrid_quick_sort(arr, 0, N - 1, k)
    print(f"Отсортированный массив {i + 1}: {arr}")
