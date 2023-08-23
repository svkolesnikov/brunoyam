import datetime
import peewee
import unittest

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


def add_course(name, time_start, time_end, id=None):
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
        row.save()

def del_student(id):
    student_del = Students.select().where(Students.id == id).execute()
    if student_del.count > 0:
        Student_courses.delete().where(Student_courses.student_id == id).execute()
        Students.delete().where(Students.id == id).execute()



class TestStudent(unittest.TestCase):

    def test_add_student(self):
        id = 99999999 #Очень большой идентификатор которого нет в таблице
        add_student('Max', 'Brooks', 24, 'Spb', id=id)
        student = Students.select().where(Students.id == id).dicts().get()
        Students.delete().where(Students.id == id).execute()
        self.assertEqual(student['name'], 'Max')


    def add_course(self):
        id = 99999999  # Очень большой идентификатор которого нет в таблице
        add_course('python', datetime.datetime(2021, 7, 21), datetime.datetime(2021, 8, 21), id=id)
        course = Courses.select().where(Courses.id == id).dicts().get()
        Courses.delete().where(Courses.id == id).execute()
        self.assertEqual(course['name'], 'python')

    def test_del_student(self):

        id = 99999999 #Очень большой идентификатор которого нет в таблице
        add_student('Max', 'Brooks', 24, 'Spb', id=id)
        student = Students.select().where(Students.id == id).dicts().get()

        Students.delete().where(Students.id == id).execute()
        student_del = Students.select().where(Students.id == id).execute()
        self.assertEqual(student_del.count, 0)


    def test_del_link(self):
        id = 99999999  # Очень большой идентификатор которого нет в таблице
        add_student('Max', 'Brooks', 24, 'Spb', id=id)
        add_course('python', datetime.datetime(2021, 7, 21), datetime.datetime(2021, 8, 21), id=id)
        add_link(id, id)

        #Проверяем удаление студента
        del_student(id)
        student_del = Students.select().where(Students.id == id).execute()
        self.assertEqual(student_del.count, 0)





if __name__ == '__main__':
    try:
       # db2.connect()
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

    unittest.main()
