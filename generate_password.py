import random

def generate_password(ans2):
    for _ in range(ans1):   
        password = []
        for _ in range(ans2):
            rancip = random.randint(0, 9)
            ranbig = random.randint(0, 25)
            ransmall = random.randint(0, 25)
            ranspec = random.randint(0, 12)
            
            if n1 == 1:
                password.append(cipfer[rancip])
            if n2 == 1:
                password.append(bigsymbol[ranbig])
            if n3 == 1:
                password.append(smallsymbol[ransmall])
            if n4 == 1:
                password.append(special[ranspec])
        
        z = len(password) - ans2
        
        for _ in range(z):
            password.pop()
    
        print(''.join(map(str, password)))
    




ans1 = int(input('Количество паролей для генерации: ')) #количество паролей которые получит пользователь

ans2 = int(input('Длина одного пароля: ')) #Длина пароля

ans3 = input('Включать ли цифры "0123456789"?: ')#будет ли использование цифр в пароле

ans4 = input('Включать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"?: ')#будут ли в пароли заглавные буквы

ans5 = input('Включать ли строчные буквы "abcdefghijklmnopqrstuvwxyz"?: ')#будут ли строчные буквы в пароле

ans6 = input('Включать ли символы "!#$%&*+-=?@^_"?: ')#будут ли специальные символы в пароле


cipfer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Массив с цифрами
bigsymbol = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # Заглавные буквы
smallsymbol = [chr(i) for i in range(ord('a'), ord('z') + 1)]  # Строчные буквы
special = ['!', '#', '$', '%', '&', '*', '+', '-', '=', '?', '@', '^', '_']  # Специальные символы

n1 = 0
n2 = 0
n3 = 0
n4 = 0


if ans3.lower() == 'да':
    n1 = 1

if ans4.lower() == 'да':
    n2 = 1

if ans5.lower() == 'да':
    n3 = 1

if ans6.lower() == 'да':
    n4 = 1

generate_password(ans2)


