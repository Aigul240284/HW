# Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
print('Задача 12')
s = int(input("Введите сумму загаданных чисел: "))
mult1=int(input("Введите произведение загаданных чисел: "))
if s<=1000 and mult1<=1000:
    for i in range(1,s):
        if s-i==mult1/i:
            print(i,s-i)
            break
    else: print('Указаны неверные значения')
else: print('Указаны неверные значения')