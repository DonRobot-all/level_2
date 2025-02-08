import pytz

{'America/Argentina/Cordoba', 'America/Chihuahua', 'GMT+0', 'America/Edmonton', 'Africa/Nouakchott', 'Pacific/Auckland', 'Pacific/Bougainville', 'Asia/Amman', 'America/Noronha', 'Africa/Lome', 'America/Monterrey', 'Etc/GMT-14', 'Africa/Ouagadougou', 'Pacific/Fiji', 'Portugal', 'Pacific/Norfolk', 'Australia/Darwin', 'Etc/GMT+5', 'Europe/Belgrade', 'Antarctica/DumontDUrville', 'Brazil/East', 'Europe/Warsaw', 'Indian/Reunion', 'America/Indiana/Vevay', 'Europe/Kyiv', 'Asia/Pontianak', 'Asia/Almaty', 'Etc/GMT+10', 'Asia/Qatar', 'America/Araguaina', 'Pacific/Midway', 'America/Ojinaga', 'Etc/GMT+6', 'America/Pangnirtung', 'America/Detroit', 'Etc/GMT-11', 'Asia/Jakarta', 'Africa/Luanda', 'WET', 'Pacific/Guadalcanal', 'America/Rosario', 'Pacific/Pohnpei', 'US/Mountain', 'Etc/UCT', 'America/Port_of_Spain', 'Asia/Ulaanbaatar', 'Pacific/Galapagos', 'Pacific/Nauru', 'US/East-Indiana', 'Etc/GMT-5', 'NZ', 'America/Havana', 'America/Nome', 'Antarctica/Palmer', 'Asia/Colombo', 'Asia/Karachi', 'Europe/Nicosia', 'America/Buenos_Aires', 'Europe/Minsk', 'America/Belem', 'America/Cancun', 'America/Chicago', 'Asia/Novosibirsk', 'America/Kentucky/Louisville', 'Pacific/Samoa', 'America/Coral_Harbour', 'America/Sao_Paulo', 'Europe/Brussels', 'America/Mendoza', 'Asia/Harbin', 'Asia/Vientiane', 'Asia/Riyadh', 'America/Bogota', 'Pacific/Kwajalein', 'America/Mazatlan', 'Asia/Muscat', 'Antarctica/Rothera', 'Australia/ACT', 'Europe/Bratislava', 'America/St_Vincent', 'America/Tortola', 'America/Lima', 'Africa/Lusaka', 'Egypt', 'Europe/Riga', 'Europe/Saratov', 'Africa/Sao_Tome', 'Asia/Dubai', 'America/Metlakatla', 'Africa/Ceuta', 'Pacific/Guam', 'America/North_Dakota/Beulah', 'MST', 'America/Indiana/Knox', 'Asia/Tehran', 'Asia/Aqtau', 'Australia/Brisbane', 'Pacific/Funafuti', 'Asia/Shanghai', 'Asia/Anadyr', 'Asia/Hebron', 'America/Argentina/Rio_Gallegos', 'Europe/Istanbul', 'Europe/Kirov', 'Africa/Bamako', 'Asia/Gaza', 'Etc/GMT-6', 'America/New_York', 'Asia/Hong_Kong', 'Africa/Bujumbura', 'Canada/Mountain', 'Etc/GMT0', 'Brazil/Acre', 'America/Nassau', 'Europe/Athens', 'Indian/Comoro', 'Europe/Paris', 'Mexico/General', 'America/Kentucky/Monticello', 'Asia/Urumqi', 'Europe/Ljubljana', 
'Asia/Bahrain', 'Antarctica/South_Pole', 'America/Curacao', 'GB', 'America/Fort_Nelson', 'US/Hawaii', 'Pacific/Honolulu', 
'Atlantic/Madeira', 'Pacific/Pitcairn', 'Etc/Universal', 'Indian/Mayotte', 'US/Indiana-Starke', 'Asia/Thimphu', 'Asia/Oral', 'America/Whitehorse', 'Asia/Singapore', 'US/Arizona', 'Asia/Sakhalin', 'America/Guatemala', 'America/St_Thomas', 'Asia/Calcutta', 'Africa/Dar_es_Salaam', 'EST5EDT', 'Africa/Bissau', 'Asia/Kolkata', 'Etc/GMT-13', 'Pacific/Chuuk', 'GMT', 'Atlantic/Faroe', 'Asia/Kuwait', 'Asia/Dili', 'Africa/Johannesburg', 'America/Fort_Wayne', 'Europe/Busingen', 'Asia/Kashgar', 'Europe/Luxembourg', 'Mexico/BajaNorte', 'America/Danmarkshavn', 'Atlantic/Faeroe', 'Europe/Rome', 'Australia/Lord_Howe', 'America/Nipigon', 'Australia/Sydney', 'Asia/Thimbu', 'Asia/Ho_Chi_Minh', 'Indian/Antananarivo', 'Asia/Ust-Nera', 'Pacific/Efate', 'Etc/GMT+0', 'America/Adak', 'Europe/Zaporozhye', 'America/Inuvik', 'America/Indiana/Vincennes', 'Africa/Maseru', 
'Atlantic/Reykjavik', 'America/Argentina/Jujuy', 'America/Argentina/Salta', 'Pacific/Tarawa', 'Canada/Eastern', 'Europe/Lisbon', 'America/La_Paz', 'Africa/Mbabane', 'Indian/Cocos', 'Asia/Manila', 'Asia/Istanbul', 'Asia/Hovd', 'Africa/Ndjamena', 'Jamaica', 'America/Nuuk', 'Europe/Monaco', 'America/Santo_Domingo', 'Indian/Maldives', 'America/Toronto', 'Canada/Atlantic', 'Asia/Chita', 'Indian/Christmas', 'Africa/Blantyre', 'America/Indiana/Winamac', 'Africa/Harare', 'Mexico/BajaSur', 'America/Jujuy', 'Europe/Copenhagen', 'America/Bahia_Banderas', 'HST', 'Indian/Mauritius', 'Europe/Guernsey', 'America/Anchorage', 'America/Merida', 'Antarctica/Casey', 'US/Pacific', 'America/Boa_Vista', 'America/Cuiaba', 'Europe/Samara', 'Etc/GMT-8', 'Etc/GMT+9', 'Atlantic/St_Helena', 'Europe/Volgograd', 'Cuba', 'Asia/Jayapura', 'Etc/GMT+1', 'America/Belize', 'Asia/Baku', 'Africa/Asmara', 'Africa/Tripoli', 'Africa/Addis_Ababa', 'America/Cambridge_Bay', 'Asia/Bangkok', 'Poland', 'America/Atka', 'Etc/Zulu', 'Africa/Dakar', 'Europe/Sofia', 'Australia/Eucla', 'Europe/Andorra', 'Africa/El_Aaiun', 'Brazil/West', 'Europe/Tallinn', 'Pacific/Pago_Pago', 'PRC', 'America/Mexico_City', 'Asia/Ashgabat', 'Antarctica/McMurdo', 'Singapore', 'America/Recife', 'America/Santiago', 'Europe/Tirane', 'America/Ensenada', 'Asia/Atyrau', 'Etc/GMT+12', 'Africa/Maputo', 'Africa/Monrovia', 'Asia/Magadan', 'America/Catamarca', 'America/Thunder_Bay', 'Pacific/Johnston', 'Etc/GMT+4', 'Indian/Chagos', 'GMT0', 'America/Bahia', 'Africa/Djibouti', 'Pacific/Kanton', 'Europe/Uzhgorod', 'Australia/Yancowinna', 'Pacific/Tahiti', 'America/Denver', 'Australia/Adelaide', 'US/Michigan', 'Africa/Bangui', 'Asia/Dhaka', 'Europe/Budapest', 'US/Samoa', 'Africa/Juba', 'America/Puerto_Rico', 'Africa/Mogadishu', 'UTC', 'Africa/Accra', 'America/Miquelon', 'Africa/Nairobi', 'Asia/Irkutsk', 'America/Caracas', 'America/Santarem', 'Europe/Chisinau', 'America/Panama', 'America/Resolute', 'GB-Eire', 'Europe/London', 'America/Grand_Turk', 'America/Dawson_Creek', 'Asia/Qostanay', 'America/Lower_Princes', 'Asia/Bishkek', 'America/Iqaluit', 'Australia/Hobart', 'America/Moncton', 'Europe/Vatican', 'Africa/Brazzaville', 'America/Argentina/San_Juan', 'Africa/Freetown', 'Asia/Phnom_Penh', 'Etc/Greenwich', 'Asia/Brunei', 'America/Antigua', 'Asia/Tokyo', 'Africa/Cairo', 'Europe/Vaduz', 'Africa/Lagos', 'Asia/Choibalsan', 'ROC', 'Europe/Simferopol', 'Antarctica/Macquarie', 'Pacific/Chatham', 'Atlantic/Jan_Mayen', 'Asia/Khandyga', 'Pacific/Noumea', 'Europe/Vienna', 'America/Grenada', 'Pacific/Ponape', 'America/Louisville', 'Israel', 'America/Cayman', 'Pacific/Port_Moresby', 'Africa/Kinshasa', 'America/Costa_Rica', 'Pacific/Rarotonga', 'Australia/Queensland', 'Canada/Pacific', 'Australia/Tasmania', 'Europe/Mariehamn', 'America/Paramaribo', 'Asia/Kuching', 'Etc/GMT+7', 'Libya', 'America/Swift_Current', 'Africa/Kampala', 'America/Shiprock', 'Europe/Zurich', 'America/Barbados', 'Europe/Kaliningrad', 'Asia/Kabul', 'Europe/Zagreb', 'Pacific/Palau', 'Antarctica/Syowa', 'Europe/Tiraspol', 'America/Ciudad_Juarez', 'Africa/Porto-Novo', 'Greenwich', 'Australia/NSW', 'Africa/Timbuktu', 'America/Indiana/Tell_City', 'Asia/Chungking', 'Turkey', 'Asia/Makassar', 'Europe/Ulyanovsk', 'Asia/Chongqing', 'Asia/Katmandu', 'America/Halifax', 'Etc/GMT+8', 'America/Yakutat', 'EET', 'Etc/GMT-2', 'Atlantic/Stanley', 'Etc/UTC', 'Europe/Isle_of_Man', 'US/Alaska', 'Iran', 'Africa/Khartoum', 'America/Indiana/Petersburg', 'America/Montevideo', 'Asia/Tbilisi', 'Pacific/Apia', 'Asia/Kathmandu', 'Asia/Yangon', 'Pacific/Wake', 'America/Manaus', 'America/Marigot', 'Asia/Macao', 'Atlantic/Canary', 'America/Argentina/ComodRivadavia', 'America/Eirunepe', 'Asia/Novokuznetsk', 'America/Martinique', 'Arctic/Longyearbyen', 'Pacific/Saipan', 'America/Guadeloupe', 'Asia/Yekaterinburg', 'Etc/GMT+11', 'America/Anguilla', 'America/Phoenix', 'America/Argentina/Mendoza', 'Asia/Barnaul', 'Australia/Currie', 'Europe/Vilnius', 'Africa/Abidjan', 'America/Godthab', 'America/Montserrat', 'America/Boise', 'Asia/Jerusalem', 'America/Montreal', 'Chile/EasterIsland', 'America/Indiana/Marengo', 'Australia/Perth', 'America/Jamaica', 'Asia/Kuala_Lumpur', 'Asia/Dushanbe', 'Africa/Casablanca', 'America/Kralendijk', 'PST8PDT', 'Asia/Aden', 'UCT', 'America/Managua', 'Etc/GMT', 'Indian/Kerguelen', 'Europe/Madrid', 'W-SU', 'US/Aleutian', 'Antarctica/Mawson', 'Asia/Qyzylorda', 'Asia/Saigon', 'CST6CDT', 'Europe/Dublin', 'America/North_Dakota/Center', 'America/Los_Angeles', 'Africa/Kigali', 'Etc/GMT-9', 'Asia/Beirut', 'Australia/West', 'EST', 'US/Eastern', 'Africa/Niamey', 'Pacific/Tongatapu', 'Asia/Kamchatka', 'Europe/Amsterdam', 'Asia/Omsk', 'Navajo', 'Asia/Tashkent', 'Asia/Seoul', 'Etc/GMT+3', 'Antarctica/Davis', 'Kwajalein', 'America/Rankin_Inlet', 'Africa/Lubumbashi', 'America/Porto_Acre', 'Asia/Macau', 'Zulu', 'America/El_Salvador', 'America/Dominica', 'Australia/South', 'America/Virgin', 'America/Goose_Bay', 'Asia/Tel_Aviv', 'Hongkong', 'Asia/Ulan_Bator', 'Pacific/Marquesas', 'Eire', 'Canada/Newfoundland', 'Pacific/Truk', 'Africa/Gaborone', 'Canada/Central', 'America/Dawson', 'America/St_Johns', 'Asia/Pyongyang', 'America/Knox_IN', 'America/Aruba', 'Asia/Samarkand', 'Europe/Moscow', 'Asia/Damascus', 'America/Rainy_River', 'Etc/GMT-7', 'Africa/Banjul', 'America/Argentina/La_Rioja', 'Africa/Malabo', 'Pacific/Kiritimati', 'Antarctica/Vostok', 'Brazil/DeNoronha', 'Africa/Tunis', 'America/Sitka', 'America/Tijuana', 'Africa/Douala', 'America/Tegucigalpa', 'Asia/Krasnoyarsk', 'Etc/GMT-0', 'America/Creston', 'Asia/Nicosia', 'Europe/Stockholm', 'Europe/Gibraltar', 'America/Regina', 'Australia/Melbourne', 'NZ-CHAT', 'Africa/Algiers', 'US/Central', 'Chile/Continental', 'Europe/Prague', 'Pacific/Gambier', 'America/Matamoros', 'America/Juneau', 'Australia/Broken_Hill', 'Europe/Bucharest', 'Pacific/Kosrae', 'Canada/Saskatchewan', 'America/Guyana', 'ROK', 'America/Atikokan', 'Pacific/Easter', 'America/Rio_Branco', 'Asia/Aqtobe', 'Pacific/Niue', 'America/Porto_Velho', 'Europe/Astrakhan', 'America/Cayenne', 'Iceland', 'Asia/Ashkhabad', 'Universal', 'Asia/Famagusta', 'Pacific/Enderbury', 'America/Santa_Isabel', 'Africa/Conakry', 'Asia/Ujung_Pandang', 'America/Argentina/Tucuman', 
'Europe/San_Marino', 'Asia/Taipei', 'America/Fortaleza', 'America/Maceio', 'GMT-0', 'Asia/Tomsk', 'Etc/GMT+2', 'Japan', 'America/Winnipeg', 'Pacific/Yap', 'Asia/Dacca', 'Pacific/Fakaofo', 'Etc/GMT-12', 'Europe/Oslo', 'Etc/GMT-1', 'America/Thule', 'America/Campo_Grande', 'America/Glace_Bay', 'Asia/Rangoon', 'Asia/Vladivostok', 'America/Cordoba', 'Asia/Yakutsk', 'Australia/Victoria', 'Atlantic/Bermuda', 'Europe/Podgorica', 'Europe/Helsinki', 'Atlantic/Azores', 'Australia/Lindeman', 'America/Argentina/Catamarca', 'America/Vancouver', 'Europe/Sarajevo', 'MET', 'Atlantic/South_Georgia', 'America/Argentina/San_Luis', 'Asia/Yerevan', 'Etc/GMT-3', 'America/Guayaquil', 'Pacific/Majuro', 'Canada/Yukon', 'Australia/Canberra', 'CET', 
'Asia/Baghdad', 'Pacific/Wallis', 'Australia/LHI', 'America/St_Lucia', 'Africa/Windhoek', 'America/Port-au-Prince', 'America/Argentina/Buenos_Aires', 'America/Menominee', 'America/Yellowknife', 'Asia/Srednekolymsk', 'America/St_Kitts', 'Antarctica/Troll', 'America/Hermosillo', 'Atlantic/Cape_Verde', 'Europe/Jersey', 'MST7MDT', 'Europe/Belfast', 'Indian/Mahe', 'America/North_Dakota/New_Salem', 'Etc/GMT-4', 'Europe/Skopje', 'Europe/Kiev', 'America/Argentina/Ushuaia', 'America/Indiana/Indianapolis', 'Europe/Berlin', 'America/St_Barthelemy', 'Australia/North', 'America/Punta_Arenas', 'Africa/Libreville', 'Africa/Asmera', 'America/Asuncion', 'America/Scoresbysund', 'Etc/GMT-10', 'Europe/Malta', 'America/Indianapolis', 'America/Blanc-Sablon'})



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
# name = set(('andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'))
# things = dict.fromkeys(name, 0)
# print(things)


# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}

# union_set = s_1 | s_2
# # union_set = s_1.union(s_2)
# print(union_set)

# intersection_set = s_1 & s_2
# # intersection_set = s_1.intersection(s_2)
# print(intersection_set)


# differenve_set = s_1 - s_2
# # differenve_set = s_1.difference(s_2)
# print(differenve_set)


# symmetric_difference = s_1 ^ s_2
# # symmetric_difference = s_1.symmetric_difference(s_2)
# print(symmetric_difference)


# s_1 = {1, 2, 3}
# s_2 = {3, 1, 2}
# print(s_1 == s_2)

# s_1 = {1, 2, 3}
# s_2 = {1, 2, 3, 4}
# print(s_1 <= s_2)

# s_1 = {1, 2, 3}
# s_2 = {1, 2, 3, 4}
# print(s_1 >= s_2)

# s = set(['Кирилл', 'Георгий', 'Денис'])
# s.add('Илья')
# print(s.pop())
# print(list(s))
# s.remove('Валерий')
# # set.pop()
# # set.clear()


# Символическая выжимка

# Во многих промышленных задачах требуется понимать, из каких символов состоят данные. Напишите программу, чтобы 
# по введённой строке она определяла, из каких символов та состоит.
# Формат ввода

# Вводится одна строка.
# Формат вывода

# Требуется вывести все символы этой строки без повторений.
# Порядок вывода не имеет значения.

# Ввод
# змееед
# Вывод
# здме

# Ввод
# велосипед
# Вывод
# исолвдеп



# Символическая разница

# А ещё в промышленных задачах часто требуется находить общее среди данных, полученных из разных источников. Напишите программу, 
# которая по двум строкам определяет их общие символы.
# Формат ввода

# Вводится две строки.
# Формат вывода

# Требуется вывести все символы этой строки без повторений.
# Порядок вывода не имеет значения.
# Ввод
# змееед
# велосипед

# Вывод
# ед




# Формат ввода
# В первой строке записано натуральное число N — количество выделенных придорожных местностей.
# В каждой из N последующих строк записано описание придорожной местности.
# Формат вывода
# Вывести все найденные объекты в придорожных местностях.

# Ввод
# 3
# березка елочка зайка волк березка
# сосна зайка сосна елочка зайка медведь
# сосна сосна сосна белочка сосна белочка

# Вывод
# сосна
# березка
# волк
# елочка
# медведь
# белочка
# зайка


# Кашееды

# Каждый воспитанник детского сада любит либо манную, либо овсяную, либо обе каши.
# Давайте создадим программу, которая позволит воспитателю быстро выяснить, сколько детей любят обе каши.
# Формат ввода

# В первых двух строках указывается количество детей, любящих манную и овсяную каши (NN и MM).
# Затем идут NN строк — фамилии детей, которые любят манную кашу, и MM строк с фамилиями детей, любящих овсяную кашу.
# Гарантируется, что в группе нет однофамильцев.
# Формат вывода

# Количество учеников, которые любят обе каши.
# Если таких не окажется, в строке вывода нужно написать «Таких нет».
# Ввод
# 3
# 2
# Васильев
# Петров
# Васечкин
# Иванов
# Михайлов

# Вывод
# Таких нет


# Ввод
# 3
# 3
# Иванов
# Петров
# Васечкин
# Иванов
# Петров
# Васечкин

# Вывод
# 3


# Кашееды — 2

# Изменим задачу и напишем программу, которая поможет быстро выяснить, сколько детей любят только одну кашу.
# Формат ввода

# В первых двух строках указывается количество детей, любящих манную и овсяную каши (N и M).
# Затем идут N+M строк — перемешанные фамилии детей.
# Гарантируется, что в группе нет однофамильцев.
# Формат вывода

# Количество учеников, которые любят только одну кашу.
# Если таких не окажется, в строке вывода нужно написать «Таких нет».

# Ввод
# 3
# 2
# Васильев
# Петров
# Васечкин
# Иванов
# Михайлов

# Вывод
# 5
