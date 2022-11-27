# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.


numbers = int(input('Введите количество чисел в списке '))
sum = 0
list = []

for i in range(1, numbers + 1) :
     list.append (round ((1 + 1 / i) ** i, 3))
     sum = sum + list[i - 1]

print ('Последовательность:', list) 
print ('Сумма:', sum)