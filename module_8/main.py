import logging
import sys
import datetime
import peewee
from orm_modeles import *

from my_db import BD

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    stream=sys.stdout,
)

logger = logging.getLogger(__name__)


def add_student(id, name, surname, age, city):
    row = Students(
        id=id,
        name=name,
        surname=surname,
        age=age,
        city=city
    )
    row.save()


def add_cource(id, name, time_start, time_end):
    row = Courses(
        id=id,
        name=name,
        time_start=time_start,
        time_end=time_end
    )
    row.save()


def add_link(student_id, course_id):
    row = Student_courses(
        student_id=student_id,
        course_id=course_id
    )
    row.save()


if __name__ == '__main__':
    db = BD("test.db")
    db.task_1()

    # Task 2
    db.add_course(1, 'python', datetime.datetime(2021, 7, 21), datetime.datetime(2021, 8, 21))
    db.add_course(2, 'java', datetime.datetime(2021, 7, 13), datetime.datetime(2021, 8, 16))

    db.add_student(1, 'Max', 'Brooks', 24, 'Spb')
    db.add_student(2, 'John', 'Stones', 15, 'Spb')
    db.add_student(3, 'Andy', 'Wings', 45, 'Manhester')
    db.add_student(4, 'Kate', 'Brooks', 34, 'Spb')

    db.add_link(1, 1)
    db.add_link(2, 1)
    db.add_link(3, 1)
    db.add_link(4, 2)

    # Для отладки SQL https://sqliteonline.com/

    print(f'\nStudents over 30 years old ')
    params = {"age": {'exp': '>', 'val': 30}}
    rows = db.select_students(params)
    for row in rows:
        print(row)

    print(f'\nStudents are studying python')
    params = {"course": {'exp': '=', 'val': 'python'}}
    rows = db.select_students(params)
    for row in rows:
        print(row)

    print(f'\nStudents are studying python from Spb')
    params = {"course": {'exp': '=', 'val': 'python'}, "city": {'exp': '=', 'val': 'Spb'}}
    rows = db.select_students(params)
    for row in rows:
        print(row)

    print("===================================================================================================")
    print("                                              peewee                                               ")
    print("===================================================================================================")

    try:
        db2.connect()
        Students.create_table()
    except peewee.InternalError as px:
        print(str(px))

    try:
        Courses.create_table()
    except peewee.InternalError as px:
        print(str(px))

    try:
        Student_courses.create_table()
    except peewee.InternalError as px:
        print(str(px))

    add_student(1, 'Max', 'Brooks', 24, 'Spb')
    add_student(2, 'John', 'Stones', 15, 'Spb')
    add_student(3, 'Andy', 'Wings', 45, 'Manhester')
    add_student(4, 'Kate', 'Brooks', 34, 'Spb')

    add_cource(1, 'python', datetime.datetime(2021, 7, 21), datetime.datetime(2021, 8, 21))
    add_cource(2, 'java', datetime.datetime(2021, 7, 13), datetime.datetime(2021, 8, 16))

    add_link(1, 1)
    add_link(2, 1)
    add_link(3, 1)
    add_link(4, 2)


    print("!!!")

    for row in Students.select().where(Students.age < 30):
        print(">")