#Вычислить число c заданной точностью d
accuracy = input('введите точность в формате 0.00001..')
accuracy_number = len(accuracy) - 2
rounded = input('введите округляемое число')
result_number = ['']
count = 0
for i in rounded:
    if i != '.':
        count += 1
    else:
        result_number = rounded[:count + accuracy_number + 1]
print(f'округленное значение равно {result_number}')


