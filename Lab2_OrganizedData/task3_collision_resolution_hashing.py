import random

"""
Реализовать хэширование умножением с разрешением коллизий цепочками переполнения, линейным зондированием и двойным хэшированием. 
Провести вычислительный эксперимент: подобрать константу для метода умножения, сравнить ее с константой Кнута по наибольшей длине цепочек коллизий (например, проитерировать константу Кнута, уменьшая или увеличивая с очень малым шагом)
"""

class HashTable:
    def __init__(self, size, method='chaining'):
        self.size = size
        self.method = method
        self.table = [None] * size

    def hash_function(self, key, constant):
        # Хэш-функция умножением
        return int(self.size * ((key * constant) % 1))

    def insert_chaining(self, key, value, constant):
        index = self.hash_function(key, constant)

        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))

    def insert_linear_probing(self, key, value, constant):
        index = self.hash_function(key, constant)

        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.size

        self.table[index] = (key, value)

    def insert_double_hashing(self, key, value, constant1, constant2):
        index = self.hash_function(key, constant1)
        step = (int(constant2 * key) % (self.size - 1)) + 1 if constant2 != 0 else 1

        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + step) % self.size

        self.table[index] = (key, value)

    def collision_chain_length(self):
        # Функция для вычисления длины наибольшей цепочки коллизий
        max_collision_length = 0
        for chain in self.table:
            if chain is not None:
                max_collision_length = max(max_collision_length, len(chain))

        return max_collision_length

def experiment(hash_table, constant1_values, keys, constant2_values=None):
    if hash_table.method == 'chaining':
        constant2_values = [None]

    for constant1 in constant1_values:
        if constant2_values is None:
            constant2_iter = [None]
        else:
            constant2_iter = constant2_values

        for constant2 in constant2_iter:
            hash_table.table = [None] * hash_table.size  # Обнуляем таблицу перед каждым экспериментом

        # Вставка в хэш-таблицы
            for key in keys:
                if hash_table.method == 'chaining':
                    hash_table.insert_chaining(key, f"value_{key}", constant1)
                elif hash_table.method == 'linear_probing':
                    hash_table.insert_linear_probing(key, f"value_{key}", constant1)
                elif hash_table.method == 'double_hashing':
                    hash_table.insert_double_hashing(key, f"value_{key}", constant1, constant2)

            max_collision_length = hash_table.collision_chain_length()
            if hash_table.method == 'chaining' or hash_table.method == 'linear_probing':
                print(f"constant={constant1}: Max Collision Length = {max_collision_length}")
            elif hash_table.method == 'double_hashing':
                print(f"constant1={constant1}, constant2={constant2}: Max Collision Length = {max_collision_length}")

table_size = 100
keys = [i for i in range(1, 101)]

constant_values_to_try = [i * 0.01 for i in range(1, 101)]

# Значение константы для хэш-функции умножением
constant1 = 0.6180339887

# Цепочки переполнения
print("Chaining Experiment:")
chaining_table = HashTable(table_size, method='chaining')
experiment(chaining_table, constant_values_to_try, keys)

# Линейное зондирование
print("\nLinear Probing Experiment:")
linear_probing_table = HashTable(table_size, method='linear_probing')
experiment(linear_probing_table, constant_values_to_try, keys)

# Двойное хэширование
print("\nDouble Hashing Experiment:")
double_hashing_table = HashTable(table_size, method='double_hashing')
constant2_values_to_try = [i * 0.01 for i in range(1, 101)]
experiment(double_hashing_table, constant_values_to_try, keys, constant2_values_to_try)
