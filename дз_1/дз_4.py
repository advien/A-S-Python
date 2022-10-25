# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

first_let = ord('a')
last_let = ord('z')

f = input("Введите первый символ от 'a' до 'z': ")
s = input("Введите второй символ от 'a' до 'z': ")

code_f = ord(f)
code_s = ord(s)

if (code_f < code_s
        and first_let <= code_s <= last_let
        and first_let <= code_s <= last_let):
    poz_f = code_f - first_let + 1
    poz_s = code_s - first_let + 1
    print(f"Позиция '{f}' = {poz_f}, позиция '{s}' = {poz_s}, букв между ними: {poz_s - poz_f - 1}")
else:
    print("Неверный ввод!")