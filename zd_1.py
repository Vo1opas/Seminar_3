# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#     *Пример:*
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12




list = [2, 3, 5, 9, 3]

def select_not_even_index(a):
    not_even = []
    if len(a) >= 2:
        for i in range(1, len(a), 2):
            not_even.append(a[i])
        return not_even
    else:
        print('В списке всего одно значение! ')


def get_sum_item_list(a):
    sum = 0
    for i in a:
        sum += i
    return sum

print(f' На нечётных позициях элементы {select_not_even_index(list)}')
print(f' Сумма нечётных элементов: {get_sum_item_list(select_not_even_index(list))}')