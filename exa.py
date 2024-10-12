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
dict1 = {'яблоки': 100, 'бананы': 333, 'груши': 200,
         'апельсины': 300, 'ананасы': 45, 'лимоны': 98,
     	'сливы': 76, 'манго': 34, 'виноград': 90, 'лаймы': 230}
dict2 = {'яблоки': 300, 'груши': 200, 'бананы': 400,
     	'малина': 777, 'ананасы': 12, 'лаймы': 123, 'черника': 111, 'арбузы': 666}

dict3 = {key:dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}
print(dict3)