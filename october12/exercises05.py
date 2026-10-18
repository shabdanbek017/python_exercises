old = int(input("Введите год рождения:"))
print(f"Вам {2026 - old}")


try:
     c = float(input("Введите температуру в градусах Цельсия:"))
     f = c * 9 / 5 + 32
     print(f"Это {round(f,1)} F")
except ValueError:
    print("Не число")

try:
     x = int(input("Вводите цену:"))
     y = int(input("Вводите количество:"))
     if x * y > 1000:
         print(f"У вас скидка 10%. Итого: {(x * y) * (1 - 10/100)}")
     else:
         print(f"Чек:{x * y}")
except ValueError:
    print("Не число!!!")

name = input("Вводите имя")
old = int(input("Вводите возраст"))
city = input("Вводите город")
print(f"Имя:{name} \n Возраст: {old} \n Город: {city}")


