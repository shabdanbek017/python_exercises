starting_balance = 1000
history_oper = []
while True:
    print(f"""
Ваш баланс: {starting_balance}
1 — пополнить
2 — снять
3 — история
4 — выход

    """)
    try:
        choice = int(input("Введите номер:"))
    except ValueError:
        print("Ошибка!")
        continue
    if choice == 1:
        starting_balance += 500
        history_oper.append("+500")
        print(f"Пополнение +500 \n Баланс:{starting_balance}")

    elif choice == 2:
        if starting_balance < 500:
            print("Недостаточно средств!")
        else:
            starting_balance -= 500
            history_oper.append("-500")
            print("Снято -500")
    elif choice == 3:
        for i in history_oper:
            print(i)
    elif choice == 4:
        print("Выход!")
        break
    else:
        print("Ошибка!")

print(f"Итоговый баланс:{starting_balance}\n Количество операций:{len(history_oper)}")