# Модуль 1 часть 1:
# Уровень 1:
value = (5 + (7 * 5 / 8)) / 3 ** 5
print(value)


# Уровень 2:
def how_many_kilometers_traveled (v, t):
    len_mkad = 109
    return print(v * t % len_mkad)

how_many_kilometers_traveled(30, 5)


# Уровень 3:
def which_number_is_greater (a, b):
    return print(max(a, b))

which_number_is_greater(124.2, -2)


# Модуль 1 часть 2:
# Уровень 1:
a = 1
b = 2
c = 3

if a == b and a == c and b == c:
    print(3)
elif a == b or b == c or c == a:
    print(2)
else:
    print(0)


# Уровень 2:
x1 = 1
x2 = 2
y1 = 3
y2 = 3
if y1 == y2 or x1 == x2:
    print("YES")
else:
    print('NO')


# Уровень 3:
password = input('Введите пароль: ')
i = 0
val = True

while i < len(password):
    if len(password) < 8:
        val = False
    if not any(char.isupper() for char in password):
        val = False
    i += 1

if val:
    print('Password is valid')
else:
    print('Password is not valid')
