# things = {
#     'зажигалка': 20, 'компас': 100, 'фрукты': 500, 'рубашка': 300,
#     'термос': 1000, 'аптечка': 200, 'куртка': 600, 'бинокль': 400, 'удочка': 1200,
#     'салфетки': 40, 'бутерброды': 820, 'палатка': 5500, 'спальный мешок': 2250, 
#     'жвачка': 10
#     }

# def k(element):
#     return element[1]

# things = dict(sorted(things.items(), key=k))
# print(things)
# things = sorted(things.values())
# print(things)
# new_things = {
#     'аптечка': 400,
#     'вода':300
# }

# things.update(new_things)
# print(things)

# def example(number, number_2):
#     return number + number_2


# assert example(2,4) == 6, example(2,4)
# assert example(0,4) == 4, example(0,4)
# assert example(2,-4) == -2, example(2,-4)
# assert example(-2,-4) == -6, example(-2,-4)

# things = {
#     'зажигалка': 20, 'компас': 100, 'фрукты': 500, 'рубашка': 300,
#     'термос': 1000, 'аптечка': 200, 'куртка': 600, 'бинокль': 400, 'удочка': 1200,
#     'салфетки': 40, 'бутерброды': 820, 'палатка': 5500, 'спальный мешок': 2250, 
#     'жвачка': 10
#     }

# print(things.get('овощи'))
# print(things.setdefault('овощи', 0))
# print(things)

# things['овощи'] = 500
# things.setdefault()
# print(things.popitem())
# things.pop('фрукты')
# print(things)
# """
# Задача 4
# Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), 
# а в качестве значений – количество этих чисел в имеющейся последовательности. 
# """
# name = ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov']
# things = dict.fromkeys(name, 0)
# print(things)


# dict1 = {'яблоки': 100, 'бананы': 333, 'груши': 200,
#          'апельсины': 300, 'ананасы': 45, 'лимоны': 98,
#      	'сливы': 76, 'манго': 34, 'виноград': 90, 'лаймы': 230}
# dict2 = {'яблоки': 300, 'груши': 200, 'бананы': 400,
#      	'малина': 777, 'ананасы': 12, 'лаймы': 123, 'черника': 111, 'арбузы': 666}

# for key, value in dict1.items():
#     if dict2.get(key) == None:
#         dict2.setdefault(key, value)
#     else:
#         dict2[key] = value + dict2.get(key)

# print(dict2)


# dict1 = {'яблоки': 100, 'бананы': 333, 'груши': 200,
#          'апельсины': 300, 'ананасы': 45, 'лимоны': 98,
#      	'сливы': 76, 'манго': 34, 'виноград': 90, 'лаймы': 230}
# dict2 = {'яблоки': 300, 'груши': 200, 'бананы': 400,
#      	'малина': 777, 'ананасы': 12, 'лаймы': 123, 'черника': 111, 'арбузы': 666}

# print(dict2.get('помидоры', 0))
# print(dict2)
# print(dict2.setdefault('помидоры', 0))
# print(dict2)




# dict1.fromkeys
# dict1.popitem
# dict1.setdefault

# dict1.pop('яблоки')
# dict1['помидор'] = 300
# print(dict1.popitem())
# print(dict1)
cats = [('Мартин', 5, 'Алексей', 'Егоров'),
    	('Фродо', 3, 'Анна', 'Самохина'),
    	('Вася', 4, 'Андрей', 'Белов'),
    	('Муся', 7, 'Игорь', 'Бероев'),
    	('Изольда', 2, 'Игорь', 'Бероев'),
    	('Снейп', 1, 'Марина', 'Апраксина'),
    	('Лютик', 4, 'Виталий', 'Соломин'),
    	('Снежок', 3, 'Марина', 'Апраксина'),
    	('Марта', 5, 'Сергей', 'Колесников'),
    	('Буся', 12, 'Алена', 'Федорова'),
    	('Джонни', 10, 'Игорь', 'Андропов'),
    	('Мурзик', 1,'Даниил', 'Невзоров'),
    	('Барсик', 2, 'Виталий', 'Соломин'),
    	('Рыжик', 7, 'Владимир', 'Медведев'),
        ('Матильда', 8, 'Андрей', 'Белов'),
    	('Гарфилд', 3, 'Александр', 'Березуев')]

dict1 = {}
for cat, age, name, second_name in cats:
    full_name = f'{name} {second_name}'
    if full_name in dict1:
        dict1[full_name].extend([cat, age])
    else:
        dict1[full_name] = [cat, age]
print(dict1)


dict1.update