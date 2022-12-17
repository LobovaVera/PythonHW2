# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# # 0,56 -> 11

num = 0
my_float_string = input("Введите вещественное число: ")
my_float_string = my_float_string.replace('.', '')
my_float_string = my_float_string.replace(',', '')
for el in my_float_string:
    num += int(el)
print(num)
