# https://python-scripts.com/peewee
# https://docs.peewee-orm.com/en/latest/peewee/database.html
from peewee import *

db = SqliteDatabase('test.db')


class BaseModel(Model):
    class Meta:
        database = db


class Students(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=100)
    surname = CharField(max_length=100)
    age = IntegerField()
    city = CharField(max_length=100)

    class Meta:
        db_table = 'students'
        order_by = ('name',)


class Courses(BaseModel):
    id = PrimaryKeyField(null=False)
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
