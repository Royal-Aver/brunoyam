#Модуль 3 часть 1
# Уровень 1
def how_many_years():
    x = int(input('Введите сумму вклада: '))
    y = int(input('Введите сумму которую хотите накопить: '))
    p = int(input('Введите проценты: '))
    proc = p / 100
    count = 0
    while x < y:
        count += 1
        x = round(x + (x * proc))
    return count
print(how_many_years())


# Уровень 2
n = int(input('Введите количество повторений: '))
while n != 0:
    print('for - это частный случай цикла while')
    n -= 1


# Уровень 3
num = int(input('Введите число:'))
sum = 0
i = num
while i != 0:
    sum += i
    i -= 1
print(sum)


#Модуль 3 часть 2:
#Уровень 1:
my_list = [1, 2, 3, 1, 2, "Hello", 'WTF', 4, 'Hello', 4]

set_my_list = set([x for x in my_list if my_list.count(x) > 1])

print(list(set_my_list))


#Уровень 3:
d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}

res = dict(zip(d.values(), d.keys()))
print(res)


#Модуль 3 часть 3:
#Уровень 1:
import cmath

def area(a, b, c):
    semiperimeter = (a + b + c) / 2
    return cmath.sqrt(semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c))

print(area(2, 5, 8))


#Уровень 2:
string = '''октябрь уж наступил — уж роща отряхает
Последние листы с нагих своих ветвей;
Дохнул осенний хлад — дорога промерзает.
Журча еще бежит за мельницу ручей,
Но пруд уже застыл; сосед мой поспешает
В отъезжие поля с охотою своей,
И страждут озими от бешеной забавы,
И будит лай собак уснувшие дубравы...'''

def get_str_len_less_5(string):
    list_words_less_5_char = []
    get_list = string.split()
    for e in get_list:
        if len(e) < 5:
            list_words_less_5_char.append(e)
    return ' '.join(list_words_less_5_char)

print(get_str_len_less_5(string))


#Модуль 3 часть 4:
#Уровень 1, 2, 3:
import json

users_list = {'Matvey': '123456', 'Denis': '098765', 'John': 'password'}
with open('users_list.json', 'w') as f:
    json.dump(users_list, f)

def register(login, passwd):
    login = input('Введите ваш логин: ')
    passwd = input('Введите ваш пароль: ')
    user_data = {'login': login, 'passwd': passwd}
    with open('new_user.txt', 'w') as f:
        json.dump(user_data, f)
        if login in users_list.keys():
            print('Ваш логин принят')
        else:
            print('Пользователь с таким логином уже зарегистрирован, придумайте другой')

register('Введите Ваш логин', 'Введите Ваш пароль')

def login(login, passwd):
    login = input('Введите ваш логин: ')
    passwd = input('Введите ваш пароль: ')
    with open('users_list.json', 'r') as f:
        users_list = json.load(f)
        if not login in users_list.keys():
            print('Такого пользователя не существует')
        elif not passwd in users_list.values():
            print('Введен неправильный пароль')
        else:
            print('Добро пожаловать')

login('Введите Ваш логин', 'Введите Ваш пароль')


