# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
num = int(input("Введите шестизначноe число: "))
if num >= 100000 and num <= 999999:
    num1=int(num/1000)
    num2=int(num%1000)
    if int(num1/100)+int(num1/10%10)+int(num1%10) == int(num2/100)+int(num2/10%10)+int(num2%10):
        print(num,'-> yes')
    else: print(num,'-> no')
else: print('Число введено некорректно')