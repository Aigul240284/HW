# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
N=int(input('Введите количество элементов в массиве:'))
data=[]
for i in range(N):
    data.append(int(input('Введите число от 1 до 10: ')))
print(data)
X=int(input('Введите число для поиска самого близкого по величине элемента из массива '))
res=data[0]
dif=abs(data[0]-X)
for i in data:
    if abs(i-X)<dif:
        dif=i-X
        res=i
print(res)
       