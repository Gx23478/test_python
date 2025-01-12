def EncryptedFile(input_file, n):
    # Чтение содержимого файла
    with open(input_file, 'r', encoding='utf-8') as f_in:
        symbol_content = f_in.read()
    
    char = []
    unichar = []  # список для шифрования файла
    decrchar = []  # список для дешифрования файла
    char = ''.join(symbol_content) 

    # Алгоритм шифрования и дешифрования
    for i in range(len(char)):
        unichar.append(chr(ord(char[i]) + n))  # шифруем файл
        decrchar.append(chr(ord(unichar[i]) - n))  # дешифруем файл

    # Запись зашифрованного текста в файл
    with open('encrypted.txt', 'w', encoding='utf-8') as file:
        file.write(''.join(unichar))  # Записываем весь зашифрованный текст в одну строку

    # Запись расшифрованного текста в файл
    with open('decrypted.txt', 'w', encoding='utf-8') as file:
        file.write(''.join(decrchar))  # Записываем весь расшифрованный текст в одну строку

def main():
    input_file = 'input.txt'  # Исходный файл
    n = int(input('Насколько символов нужен сдвиг?: '))  # сдвиг для шифра Цезаря
    EncryptedFile(input_file, n)

if __name__ == '__main__':
    main()

