# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, \
# содержащий сумму многочленов.
first_polynom = open('file_task5_first.txt', 'r')
first_polynom_out = first_polynom.readline()
print(first_polynom_out)
second_polynom = open('file_task5_second.txt', 'r')
second_polynom_out = second_polynom.readline()
print(second_polynom_out)
first_polynom.close()
second_polynom.close()
result_first = first_polynom_out[:-4]
result_second = second_polynom_out[:-4]
result_polynom = result_first + '+' + result_second + ' = 0'
print(result_polynom)
answer = open('final.txt', 'a')
answer.write(result_polynom)
answer.close()