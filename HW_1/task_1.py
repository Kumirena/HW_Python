'''Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |'''

print('Введите трехзначное число: ')
a = int(input())
n = 0
while a > 0:
    n += a % 10
    a //= 10
print('Сумма цифр', n)