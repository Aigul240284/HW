poem=input("Введите стихотворение: ")
res=list(filter(lambda x: x in "аяуюоеёэиыАЯУЮОЕЁЭИЫ", poem))
print("Парам-пам-пам" if 0<len(res) and len(res)%2==0 else "Пам-парам")


