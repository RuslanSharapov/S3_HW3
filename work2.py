# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

n = int(input('Введите число: '))
my_list, my_list2 = [], []

for i in range(n):
    my_list.append(random.randint(1, 9))

for i in range(len(my_list)):
    while i < len(my_list) / 2 and n > len(my_list) / 2:
        n = n - 1
        a = my_list[i] * my_list[n]
        my_list2.append(a)
        i += 1

print(f'{my_list}\n{my_list2}')
