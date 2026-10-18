try:
    a = int(input("Введите число:"))
    b = int(input("На сколько нужно делить:"))
    print(f"Результат:{a/b}")
except ZeroDivisionError:
       print("На ноль делить нельзя!")
