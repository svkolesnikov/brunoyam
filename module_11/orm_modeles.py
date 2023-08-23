from peewee import *


db2 = SqliteDatabase('test2.db')


class BaseModel(Model):
    class Meta:
        database = db2


class Students(BaseModel):
    name = CharField(max_length=100, default='')
    surname = CharField(max_length=100, default='')
    age = IntegerField(default=0)
    city = CharField(max_length=100, default='')

    class Meta:
        db_table = 'students'
        order_by = ('name',)


class Courses(BaseModel):
    name = CharField(max_length=100, null=False)
    time_start = DateField(null=False)
    time_end = DateField(null=False)

    class Meta:
        db_table = 'courses'
        order_by = ('id',)


class Student_courses(BaseModel):
    student_id = IntegerField(null=False)
    course_id = IntegerField(null=False)

    class Meta:
        db_table = 'student_courses'
        order_by = ('id',)
