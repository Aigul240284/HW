# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
width = int(input("Введите ширину: "))
length = int(input("Введите длину: "))
num = int(input("Укажите кол-во необходимых долек "))
if (num%width==0 or num%length==0) and num<=width*length:
    print(width,length,num,'-> yes')
else: print(width,length,num,'-> no')