# Функция для выполнения побитового сдвига влево
def left_rotate(value, amount):
    return ((value << amount) | (value >> (32 - amount))) & 0xFFFFFFFF

# Функция для вычисления SHA-1 хеша
def sha1(message):
    # Инициализация начальных значений хеша
    hash_values = [
        0x67452301,  # Первое хеш-значение
        0xEFCDAB89,  # Второе хеш-значение
        0x98BADCFE,  # Третье хеш-значение
        0x10325476,  # Четвёртое хеш-значение
        0xC3D2E1F0   # Пятое хеш-значение
    ]

    # Преобразование сообщения в байты
    original_byte_length = len(message)  # Длина сообщения в байтах
    original_bit_length = original_byte_length * 8  # Длина сообщения в битах
    message += b'\x80'  # Добавление бита 1 в конце сообщения
    message += b'\x00' * ((56 - (original_byte_length + 1) % 64) % 64)  # Дополнение до 56 байт
    message += original_bit_length.to_bytes(8, byteorder='big')  # Добавление длины сообщения в битах

    # Основной цикл обработки блоков
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]  # Извлечение текущего блока
        w = list(int.from_bytes(chunk[j:j + 4], byteorder='big') for j in range(0, 64, 4))  # Создание массива w

        # Расширение массива w до 80 элементов
        for j in range(16, 80):
            new_value = w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16]
            w.append(left_rotate(new_value, 1))  # Выполнение побитового сдвига

        # Инициализация временных переменных a, b, c, d, e
        a = hash_values[0]
        b = hash_values[1]
        c = hash_values[2]
        d = hash_values[3]
        e = hash_values[4]

        # Основной цикл обработки
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | (~b & d)  # Функция для первой четверти
                k = 0x5A827999  # Константа для первой четверти
            elif 20 <= j <= 39:
                f = b ^ c ^ d  # Функция для второй четверти
                k = 0x6ED9EBA1  # Константа для второй четверти
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)  # Функция для третьей четверти
                k = 0x8F1BBCDC  # Константа для третьей четверти
            else:
                f = b ^ c ^ d  # Функция для четвёртой четверти
                k = 0xCA62C1D6  # Константа для четвёртой четверти

            # Обновление временной переменной
            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xFFFFFFFF
            e = d  # Обновление e
            d = c  # Обновление d
            c = left_rotate(b, 30)  # Обновление c
            b = a  # Обновление b
            a = temp  # Обновление a
        
        # Обновление значений хеша
        hash_values[0] = (hash_values[0] + a) & 0xFFFFFFFF
        hash_values[1] = (hash_values[1] + b) & 0xFFFFFFFF
        hash_values[2] = (hash_values[2] + c) & 0xFFFFFFFF
        hash_values[3] = (hash_values[3] + d) & 0xFFFFFFFF
        hash_values[4] = (hash_values[4] + e) & 0xFFFFFFFF

    # Возвращение хеша в виде 20-байтовой строки
    return b''.join(x.to_bytes(4, byteorder='big') for x in hash_values)

# Проверка работы алгоритма
if __name__ == "__main__":

    message = b"Hello, World !"
    hash = sha1(message)
    print("\nТекст первичный:\n", message) 
    print("Hash:", hash.hex())  # Хеш в шестнадцатеричном формате

    message = b"Hello, World !"
    hash = sha1(message)
    print("\nТекст первичный (повтор):\n", message) 
    print("Hash:", hash.hex())  # Хеш в шестнадцатеричном формате

    message = b"Hello, World ?"
    hash = sha1(message)
    print("\nТекст первичный (замена ! на ?):\n", message) 
    print("Hash:", hash.hex())  # Хеш в шестнадцатеричном формате
