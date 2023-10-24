"""
Задание 3:
- Подсчитать число элементарных операций в реализации сортировки вставками
"""
import random

def insertion_sort(arr):
    comparisons = 0  # счетчик сравнений
    moves = 0        # счетчик перемещений

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1  # увеличиваем счетчик сравнений
            arr[j + 1] = arr[j]
            moves += 1        # увеличиваем счетчик перемещений
            j -= 1
        arr[j + 1] = key
        moves += 1            # увеличиваем счетчик перемещений

    return comparisons, moves

arr = [random.randint(0, 50) for _ in range(25)]
print("\nИсходный массив: ", arr)
comparisons, moves = insertion_sort(arr)
print("Отсортированный массив: ", arr)
print("Число сравнений: ", comparisons)
print("Число перемещений: ", moves)
