"""
Задание 4. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""


my_list = input('Введите целые числа через пробел - ').split()
new_list = []
for i in range(0, len(my_list), 2):
    count = i + 2
    a = my_list[i:count]
    a.reverse()
    new_list.extend(a)
print(new_list) # Как в примере не получается, что бы без скобок было. Мозгов не хватает.



