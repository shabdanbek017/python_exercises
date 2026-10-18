#Блок 2. Строки (операции + методы)
#8. Приветствие. Запроси имя, выведи Привет, <имя>! через f-строку.
name = input("Введите имz:")
print(f"Привет {name}!")
print(f"Длина имени {len(name)} буквы")
print("первая и последняя буква имени:",name[0],name[-1])
print(name.upper(), name.lower())
print(name.strip())
print(name.replace('a','o'))
print(name[: : -1])
print(name.isdigit())
print(name.find('a'))


s = "Программирование"
print(s[:4], s[-4:])

