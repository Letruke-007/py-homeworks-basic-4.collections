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

# Задача 3. Частотность поисковых запросов по количеству слов

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

counter1 = 0
counter2 = 0
counter3 = 0


for i in range(len(queries)):
    words = queries[i].split(' ')
    if len(words) == 1:
        counter1 += 1
    elif len(words) == 2:
        counter2 += 1
    elif len(words) == 3:
        counter3 += 1

res_ = counter1 + counter2 + counter3

if res_ != 0:
    print(f'Поисковых запросов, состоящих из 1 слова, {counter1 / res_ * 100}%')
    print(f'Поисковых запросов, состоящих из 2 слов, {counter2 / res_ * 100}%')
    print(f'Поисковых запросов, состоящих из 3 слов, {counter3 / res_ * 100}%')
else:
    print('Все поисковые запросы не подходят под критерии поиска (1,2 или 3 слова)')

# Задача 4. Возврат значения с максимальные объемом продаж

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

res_ = sorted(stats.items(), key=lambda x: x[1])

print(res_[-1])
