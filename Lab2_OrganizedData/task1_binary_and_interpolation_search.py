import random

"""
Реализовать алгоритмы бинарного и интерполяционного поиска числа x в массиве длины N, элементы которого - случайные целые числа в диапазоне от 0 до M. 
Вывести число операций сравнения, выполненных алгоритмом для заданных величин.
"""

def binary_search(arr, x):
    comparisons = 0 # счетчик операций сравнения
    low, high = 0, len(arr) - 1 # начальные границы поиска
    
    while low <= high:
        mid = (low + high) // 2 # середина массива
        comparisons += 1
        
        if arr[mid] == x:
            return comparisons # если элемент найден, возвращаем количество операций
        elif arr[mid] < x:
            low = mid + 1 # если искомый элемент больше, ищем в правой половине (переносим нижнюю границу справа от середины)
        else:
            high = mid - 1 # если искомый элемент меньше, ищем в левой половине (переносим верхнюю границу слева от середины)
    
    return comparisons

def interpolation_search(arr, x):
    comparisons = 0
    low, high = 0, len(arr) - 1
    
    while low <= high and arr[low] <= x <= arr[high]:
        mid = low + (high - low) * (x - arr[low]) // (arr[high] - arr[low]) # формула интерполяции
        comparisons += 1
        
        if arr[mid] == x:
            return comparisons
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return comparisons

N = 100
M = 1000
arr = sorted(random.sample(range(M + 1), N))

x_to_search = random.randint(0, M)

binary_comparisons = binary_search(arr, x_to_search)
interpolation_comparisons = interpolation_search(arr, x_to_search)

print(f"Binary Search: {binary_comparisons} comparisons")
print(f"Interpolation Search: {interpolation_comparisons} comparisons")
