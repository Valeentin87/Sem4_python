# Задайте последовательность чисел. Напишите программу,\
# которая выведет список неповторяющихся элементов исходной последовательности.
import random
my_list = []
result_list = []
for i in range(0, 5):
    my_list.append(random.randint(0, 10))
print(my_list)
for i in range(len(my_list)):
    if my_list[i] in my_list[i+1:]:
        result_list.append(my_list[i])
result = set(my_list).difference(set(result_list))
print('уникальные элементы в первой последовательности {}'.format(result))