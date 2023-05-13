import datetime
import peewee
from orm_modeles import *


def add_student(name: str, surname: str, age: int, city: str, id=None):
    if id:
        try:
            Students.insert(
                id=id,
                name=name,
                surname=surname,
                age=age,
                city=city
            ).execute()
        except:
            print("Запись существует")
    else:
        raw = Students(
            name=name,
            surname=surname,
            age=age,
            city=city
        )
        raw.save()


def add_cource(name, time_start, time_end, id=None):
    if id:
        try:
            Courses.insert(
                id=id,
                name=name,
                time_start=time_start,
                time_end=time_end).execute()
        except:
            print("Запись существует")

    else:
        row = Courses(
            name=name,
            time_start=time_start,
            time_end=time_end
        )
        row.save()


def add_link(student_id, course_id):
    if not Student_courses.select().where(Student_courses.student_id == student_id,
                                          Student_courses.course_id == course_id):
        row = Student_courses(
            student_id=student_id,
            course_id=course_id
        )
        print(row.save())


if __name__ == '__main__':
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

    add_student('Max', 'Brooks', 24, 'Spb', 1)
    add_student('John', 'Stones', 15, 'Spb', 2)
    add_student('Andy', 'Wings', 45, 'Manhester', 3)
    add_student('Kate', 'Brooks', 34, 'Spb', 4)

    add_cource('python', datetime.datetime(2021, 7, 21), datetime.datetime(2021, 8, 21), 1)
    add_cource('java', datetime.datetime(2021, 7, 13), datetime.datetime(2021, 8, 16), 2)

    add_link(1, 1)
    add_link(2, 1)
    add_link(3, 1)
    add_link(4, 2)

    print("* Старше 30 лет *****************************************************************************************")
    for row in Students.select().where(Students.age > 30).dicts():
        print(row)

    print("* Слушают курс по python *********************************************************************************")
    for row in Students.select(Students, Student_courses, Courses.name.alias('course_name')) \
            .join(Student_courses, on=(Students.id == Student_courses.student_id)) \
            .join(Courses, on=(Courses.id == Student_courses.course_id)) \
            .where(Courses.name == 'python') \
            .dicts():
        print(row)

    print("* Слушают курс по питону и живут в Питере ****************************************************************")
    for row in Students.select(Students, Student_courses, Courses.name.alias('course_name')) \
            .join(Student_courses, on=(Students.id == Student_courses.student_id)) \
            .join(Courses, on=(Courses.id == Student_courses.course_id)) \
            .where(Courses.name == 'python', Students.city == 'Spb') \
            .dicts():
        print(row)
