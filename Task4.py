# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена\
# и записать в файл многочлен степени k.
import  random
polynom = ' '
multyplier = ' '
k = int(input('введите степень многочлена k =  '))
for i in range(k+1):

    a = random.randint(0, 4)
    if a == 0:
        continue
    else:
        multyplier = f'{a} * x^{i} + '
        polynom += multyplier
result = str(f'{polynom[:-2]} = 0')
print(result)
date = open('file1.txt', 'a')
date.write(result)
date.close()


