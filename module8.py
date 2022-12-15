# Уровень 1 и 2:

# import sqlite3
#
# conn = sqlite3.connect('db1.sqlite')
#
# cursor = conn.cursor()
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS Students(id int PRIMARY KEY, name Varchar(32), surname Varchar(32),
#                 age int, city Varchar(32))''')
# conn.commit()
# # cursor.executemany('INSERT INTO Students Values (?, ?, ?, ?, ?)',
# #                    [(1, 'Max', 'Brooks', 24, 'Spb'),
# #                     (2, 'John', 'Stones', 15, 'Spb'),
# #                     (3, 'Andy', 'Wings', 45, 'Manchester'),
# #                     (4, 'Kate', 'Brooks', 34, 'Spb')])
# conn.commit()
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS Courses(id int PRIMARY KEY, name Varchar(32), time_start Varchar(32),
#                time_end Varchar(32))''')
# conn.commit()
# # cursor.executemany('INSERT INTO Courses Values (?, ?, ?, ?)',
# #                    [(1, 'python', '21.07.21', '21.08.21'),
# #                     (2, 'java', '13.07.21', '16.08.21')])
# conn.commit()
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS Student_courses(student_id int, course_id int,
#                 FOREIGN KEY(student_id) REFERENCES Students(id),
#                 FOREIGN KEY(course_id) REFERENCES Courses(id))''')
# conn.commit()
# cursor.executemany('INSERT INTO Student_courses Values (?, ?)',
#                    [(1, 1),
#                     (2, 1),
#                     (3, 1),
#                     (4, 2)])
# conn.commit()
#
# print('Студенты, которым больше 30 лет:')
# age_more_30 = cursor.execute('SELECT name, surname FROM Students WHERE age > 30')
# print(age_more_30.fetchall())
#
# print('Студенты, которые изучают язык программирования python:')
# students_take_courses_python = cursor.execute("""SELECT Students.name, Students.surname FROM
#                                                 Students JOIN Student_courses ON
#                                                  Student_courses.student_id = Students.id JOIN Courses
#                                                   ON Student_courses.course_id = Courses.id
#                                                    WHERE Courses.name = 'python'""")
# print(students_take_courses_python.fetchall())
#
# print('Студенты, которые изучают язык программирования python и живут в Санкт-Петербурге:')
# students_take_courses_python_and_SPB = cursor.execute("""SELECT Students.name, Students.surname
#                                                         FROM Students JOIN Student_courses ON
#                                                          Student_courses.student_id = Students.id JOIN Courses ON
#                                                           Student_courses.course_id = Courses.id
#                                                            WHERE Courses.name = 'python' and Students.city = 'Spb'""")
# print(students_take_courses_python_and_SPB.fetchall())
#
# conn.close()



# Уровень 3:
from peewee import *

conn = SqliteDatabase('db2. sqlite')

class Students(Model):
    id = PrimaryKeyField()
    name = CharField()
    surname = CharField()
    age = IntegerField()
    city = CharField()

    class Meta:
        database = conn


class Courses(Model):
    id = PrimaryKeyField()
    name = CharField()
    time_start = CharField()
    time_end = CharField()

    class Meta:
        database = conn


class Student_courses(Model):
    student_id = ForeignKeyField(Students)
    course_id = ForeignKeyField(Courses)

    class Meta:
        database = conn
        indexes = ((('student_id', 'course_id'), True),)


# Students.create_table()
# Courses.create_table()
# Student_courses.create_table()

def data_fill():
    courses_data = [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')]
    students_data = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
				(3, 'Andy', 'Wings', 45, 'Manchester'), (4, 'Kate', 'Brooks', 34, 'Spb')]
    student_courses_data = [(1, 1), (2, 1), (3, 1), (4, 2)]
    try:
        Courses.insert_many(courses_data, fields=[Courses.id, Courses.name, Courses.time_start,
                                                  Courses.time_end]).execute()
    except IntegrityError:
        print('Таблица уже заполнена')
    try:
        Students.insert_many(students_data, fields=[Students.id, Students.name, Students.surname,
                                                    Students.age, Students.city]).execute()
    except IntegrityError:
        print('Таблица уже заполнена')
    try:
        Student_courses.insert_many(student_courses_data, fields=[Student_courses.student_id,
                                                                  Student_courses.course_id]).execute()
    except IntegrityError:
        print('Таблица уже заполнена')


data_fill()


age_more_30 = Students.select().where(Students.age > 30)
print('Студенты, которым больше 30 лет:')
for el in age_more_30:
    print(el.name, el.surname)

students_take_courses_python = Students.select().join(Student_courses).join(Courses).where(Courses.name == 'python')
print('Студенты, которые изучают язык программирования python:')
for el in students_take_courses_python:
    print(el.name, el.surname)

students_take_courses_python_and_SPB = Students.select().join(Student_courses).join(Courses).\
    where((Courses.name == 'python') & (Students.city == 'Spb'))
print('Студенты, которые изучают язык программирования python и живут в Санкт-Петербурге:')
for el in students_take_courses_python_and_SPB:
    print(el.name, el.surname)





