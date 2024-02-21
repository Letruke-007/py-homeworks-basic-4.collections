# Задача 1. Визиты в Россию

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
sorted_geo_logs = []

result = [geo_log for geo_log in geo_logs if "Россия" in next(iter(geo_log.values()))]
print(result)

# Задача 2. Уникальные гео-ID

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

sorted_ids = []

for elm in ids.values():
    sorted_ids += elm

sorted_ids = sorted(set(sorted_ids))

print(sorted_ids)
