# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


a = int(input('Введите число А: '))
b = int(input('Введите число B: '))

def raising_a_num(num_1, num_2):
    return 1 if num_2 == 0 else num_1 * (raising_a_num(num_1, num_2 - 1))

print(raising_a_num(a,b))