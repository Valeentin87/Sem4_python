# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
number = int(input('введите натуральное число N = '))
multipliers = [1, ]
for i in range(2, number+1):

    if number % i == 0:
        multipliers.append(i)
    else: continue
print(f'список простых множителей числа {number} равен {multipliers}')
