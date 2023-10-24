"""
Задание 2:
- Реализовать гибридный алгоритм, сочетающий Merge и Insertion Sort следующим образом: 
в Merge Sort участки массива длины меньшей некоторого параметра k сортировать вставками, не используя рекурсию сортировки слиянием;
- Подобрать оптимальное k для сортировки R массивов длины N, элементы которых - случайные целые числа в диапазоне от 0 до  M;
- Предусмотреть возможность ввода N, R, M;
"""

"""
Преимуществом Merge Sort является его стабильность (порядок элементов с одинаковыми значениями сохраняется) 
и гарантированная временная сложность O(n log n) в худшем, лучшем и среднем случаях. 
Однако он требует дополнительной памяти для временного хранения подмассивов, что может сделать его менее эффективным 
для больших массивов в сравнении с некоторыми другими алгоритмами сортировки.
"""

import random

def generate_random_array(n, m):
    return [random.randint(0, m) for _ in range(n)]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr, k):
    if len(arr) > k:
        mid = len(arr) // 2 # до тех пор, пока не останется подмассивы с одним элементом или пустой массив (они считаются упорядоченными)
        left = arr[:mid]
        right = arr[mid:]

        # рекурсивно сортируются две половины массива
        merge_sort(left, k) 
        merge_sort(right, k)

        i = j = m = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[m] = left[i]
                i += 1
            else:
                arr[m] = right[j]
                j += 1
            m += 1

        while i < len(left):
            arr[m] = left[i]
            i += 1
            m += 1

        while j < len(right):
            arr[m] = right[j]
            j += 1
            m += 1

def hybrid_merge_insertion_sort(arr, k):
    if len(arr) > k:
        merge_sort(arr, k)
    else:
        insertion_sort(arr)

N = int(input("\nВведите длину массивов (N): "))
R = int(input("Введите количество массивов (R): "))
M = int(input("Введите максимальное значение элементов (M): ")) 

for i in range(R):
    arr = generate_random_array(N, M)
    print(f"\nИсходный массив {i + 1}: {arr}")
    k = N // 10
    hybrid_merge_insertion_sort(arr, k)
    print(f"Отсортированный массив {i + 1}: {arr}")
