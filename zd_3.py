# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
#    максимальным и минимальным значением дробной части элементов.
#     *Пример:*
#     - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]

from typing import List

def sort_fractional_part(a: List):
    for i in range(len(a)):
        if type(a[i]) == float:
            a[i] = round(a[i] - int(a[i]), 2)
    a.sort()
    return a


def get_difference_max_min_fractional(a: List):
    max = 0
    min = 0
    for i in range(- 1, - len(a) + 1, - 1):
        if type(a[i]) == float:
            max = a[i]
            break
    for item in a:
        if type(item) == float:
            min = item
            break
    difference = max - min
    return difference

print(f'{list}\n')
print(f'\
    Разница между максимальным и минимальным значением дробной части элементов => {get_difference_max_min_fractional(sort_fractional_part(list))}')