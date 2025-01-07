import random

def generate_password(ans2, chars):
    password = []
    for _ in range(ans2):
        password.append(random.choice(char))
    
    
    
    
    
    return password




ans1 = int(input('Количество паролей для генерации: ')) #количество паролей которые получит пользователь

ans2 = int(input('Длина одного пароля: ')) #Длина пароля

ans3 = input('Включать ли цифры "0123456789"?: ')#будет ли использование цифр в пароле

ans4 = input('Включать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"?: ')#будут ли в пароли заглавные буквы

ans5 = input('Включать ли строчные буквы "abcdefghijklmnopqrstuvwxyz"?: ')#будут ли строчные буквы в пароле

ans6 = input('Включать ли символы "!#$%&*+-=?@^_?"?: ')#будут ли специальные символы в пароле

ans7 = input('Исключать ли неоднозначные символы "il1Lo0O"?: ')#будут ли использоваться неоднозначные символы

cipfer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Массив с цифрами
bigsymbol = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # Заглавные буквы
smallsymbol = [chr(i) for i in range(ord('a'), ord('z') + 1)]  # Строчные буквы
special = ['!', '#', '$', '%', '&', '*', '+', '-', '=', '?', '@', '^', '_']  # Специальные символы
ambisymbol = ['i', 'l', '1', 'L', 'o', '0', 'O']  # Неоднозначные символы

i = 0

char = []

if ans3.lower() == 'да':
    char += cipfer

if ans4.lower() == 'да':
    char += bigsymbol

if ans5.lower() == 'да':
    char += smallsymbol

if ans6.lower() == 'да':
    char += special

# Исключение неоднозначных символов
if ans7.lower() == 'да':
    char = [c for c in char if c not in ambisymbol]
    
print(generate_password(ans2, char))


