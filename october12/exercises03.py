#Блок 3. if / else
try:
    x = int(input("Введите число:"))
    if x % 2 == 0:
        print("Четное")
    else:
        print("Нечетное")
except ValueError:
    print("Это не число!!!")

try:
    x = int(input("Введите число:"))
    if x > 0:
        print("Число положительное")
    elif x < 0:
        print("Число отрицательное")
    else:
        print("ноль")
except ValueError:
    print("Это не число!!!")

try:
    x = int(input("Введите число:"))
    y = int(input("Введите 2 число"))
    if x > y:
        print(f"Максимум из двух{x}")
    elif x < y:
        print(f"Максимум из двух{y}")
    else:
        print("=")
except ValueError:
    print("Не число!!!")

try:
    x = int(input("Введите возраст:"))
    if x >= 18:
        print("Взрослый")
    else:
        print("Ребенок")
except ValueError:
    print("Не число")

try:
    x = int(input("Введите балл"))
    if x >= 90:
        print("Ваша оценка 5")
    elif x >= 75:
        print("Ваша оценка 4")
    elif x >= 50:
        print("Ваша оценка 3")
    else:
        print("Ваша оценка 2")
except ValueError:
    print("Не число!!!")

x = len(input("Введите имя:"))
if x > 5:
    print("Длинное имя")
else:
    print("Короткое имя")

x = input("Введите пароль:")
if x == "Python":
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

x = int(input("Введите число"))
if 0 < x < 20:
    print(f"число {x} в диапазоне 1-19")
else:
    print(f"число {x} не в диапазоне 1-19")

s = input("Введи строку:")
if s.lower().startswith("привет"):
    print("Строка начинается ч Привет")
else:
    print("Не начинается")



