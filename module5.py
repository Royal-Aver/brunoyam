# Часть 1:
# Уровень 1(в задании нужно изменять строку, но в python строки на изменяются по частям, только полностью
# перезаписываются, либо преобразовывается в список и потом в измененном состоянии собирается в строку. Сделал добавление новых строк):
class StringVar:

    def __init__(self, string):
        self.string = string

    def set(self, new_str_val):
        self.string += f' {new_str_val}'

    def get(self):
        return self.string

str1 = StringVar('Hello World!')
str1.set('NO')
str1.set('Yes')
print(str1.get())

# Уровень 2(вообще непонятное задание, сделал как понял):
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def negative_line_segment(self):
        return -(self.x * self.y)

point = Point(4, 3)
print(point.negative_line_segment())


# Часть 2:
import json

class Model:

    def __init__(self):
        self.title = 'This is the title'
        self.text = 'This is text'
        self.author = 'The author\'s name will appear here'

    def save(self):
        with open('data.json', 'w') as f:
            json.dump(self.__dict__, f)

dict1 = Model()
dict1.save()


