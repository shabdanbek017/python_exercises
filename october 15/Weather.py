#Задача 3. «Метеостанция»
from encodings import hp_roman8

data = [
    ("Пн", 5, 12),
    ("Вт", 3, 10),
    ("Ср", -2, 8),
    ("Чт", 0, 6),
    ("Пт", 7, 14),
    ("Сб", 10, 18),
    ("Вс", 8, 15),
]
avar = []
mintemp = []

hot_temp = data[0][2]
hot_day = data[0][0]
cold_temp = data[0][1]
cold_day = data[0][0]


for day, min_t, max_t in data:
    print(f"{day}: мин {min_t} макс {max_t} среднее {(min_t + max_t) / 2}")
    avar.append((min_t + max_t)/2)
    if max_t > hot_temp:
           hot_temp = max_t
           hot_day = day

    if min_t < cold_temp:
        cold_temp = min_t
        cold_day = day

    if min_t < 0:
        mintemp.append(day)

avtempweek = sum(avar) / len(avar)
print(f"Средняя темература за неделю: {avtempweek}")
print(f"Самый теплый день:{hot_day,hot_temp} ")
print(f"Самый холодный день:{cold_day,cold_temp} ")
print(mintemp)