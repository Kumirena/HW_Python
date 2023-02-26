'''Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.'''

n = int(input('Введите количество монеток: '))
count_averse = 0
count_reverse = 0
import random
a = [random.randint(0,1) for i in range(n)]
print(a)
for i in range(n):
       if a[i] == 0:
        count_averse += 1
       if a[i] == 1:
        count_reverse += 1
if count_averse < count_reverse:
    print(count_averse)
else:
    print(count_reverse)