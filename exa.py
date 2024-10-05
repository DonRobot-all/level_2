things = {
    'зажигалка': 20, 'компас': 100, 'фрукты': 500, 'рубашка': 300,
    'термос': 1000, 'аптечка': 200, 'куртка': 600, 'бинокль': 400, 'удочка': 1200,
    'салфетки': 40, 'бутерброды': 820, 'палатка': 5500, 'спальный мешок': 2250, 
    'жвачка': 10
    }

def k(element):
    return element[1]

things = dict(sorted(things.items(), key=k))
print(things)


# things = sorted(things.values())
# print(things)