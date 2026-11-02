import random
import string

length = int(input("Какой длины нужен пароль? (например, 5): "))

characters = string.ascii_letters + string.digits
password = ""

for i in range(length):
    password += random.choice(characters)
    print("Шаг", i, ": добавили символ. Теперь пароль:", password)

print("Готово! Твой надежный пароль:", password)
