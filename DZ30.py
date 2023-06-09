a,d,n = (int(input("Первый элемент: ")),int(input("Разность эл-тов: ")),
int(input("Кол-во элементов: ")))
ls=[]
for i in range(n):
    ls.append(a + i * d)
print(ls)