# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
n = int(input("Введите число: "))
for i in range(0, n): 
    if 2**i>n:
        break
    print(2**i)

