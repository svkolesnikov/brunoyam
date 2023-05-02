import logging
import sqlite3
import datetime
from sqlite3 import Cursor

logger = logging.getLogger(__name__)


class BD:

    def __init__(self, db_name: str):
        self.db_name = db_name

    def task_1(self):
        """
        Creation tables
        :return:
        """
        connect = None
        cursor = None

        try:
            connect = sqlite3.connect(self.db_name)
        except sqlite3.Error as error:
            logger.error(error)

        if connect:
            try:
                cursor = connect.cursor()
                logger.info('Connected to DB successful')
                query = '''CREATE TABLE Students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        name TEXT NOT NULL DEFAULT '',
                        surname TEXT NOT NULL DEFAULT '',
                        age INTEGER NOT NULL DEFAULT 0,
                        city TEXT NOT NULL DEFAULT '');
                '''
                cursor.execute(query)
                connect.commit()
                logger.info('Table Courses created')
            except sqlite3.Error as error:
                logger.error(error)

            try:
                query = '''CREATE TABLE Courses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        name TEXT NOT NULL DEFAULT '',
                        time_start DATETIME,
                        time_end DATETIME);
                '''
                cursor.execute(query)
                logger.info('Table Courses created')
                connect.commit()
            except sqlite3.Error as error:
                logger.error(error)

            try:
                query = '''CREATE TABLE Student_courses (
                        student_id INTEGER NOT NULL,
                        course_id INTEGER NOT NULL);
                '''
                cursor.execute(query)
                logger.info('Table Student_courses created')
                connect.commit()
            except sqlite3.Error as error:
                logger.error(error)

            if cursor:
                cursor.close()

        if connect:
            connect.close()
            logger.info('Disconnected to DB successful')

    def add_course(self, id: int = None, name="", date_start: datetime = None,
                   date_stop: datetime = None):
        """Adding a cource"""
        connect = None
        cursor = None

        if (len(name) == 0) | (date_start is None) | (date_stop is None):
            return

        try:
            connect = sqlite3.connect(self.db_name)
        except sqlite3.Error as error:
            logger.error(error)

        if connect:
            try:
                cursor = connect.cursor()
                logger.info('Connected to DB successful')
                if id:
                    query = f'''INSERT INTO Courses
                            (id, name, time_start, time_end)
                            VALUES ({id}, '{name}', '{date_start.strftime('%Y-%m-%d')}', '{date_stop.strftime('%Y-%m-%d')}');
                            '''
                else:
                    query = f'''INSERT INTO Courses
                            ( name, time_start, time_end)
                            VALUES ( '{name}', '{date_start.strftime('%Y-%m-%d')}', '{date_stop.strftime('%Y-%m-%d')}');
                            '''

                cursor.execute(query)
                connect.commit()
                logger.info('Record %s added to table Courses', id)
            except sqlite3.Error as error:
                logger.error(error)

                if cursor:
                    cursor.close()
                return

            if connect:
                connect.close()
                logger.info('Disconnected to DB successful')

    def add_student(self, id: int = None, name="", surname="", age: int = 0, city=""):
        """Adding a student"""
        connect = None
        cursor = None

        try:
            connect = sqlite3.connect(self.db_name)
        except sqlite3.Error as error:
            logger.error(error)

        if connect:
            try:
                cursor = connect.cursor()
                logger.info('Connected to DB successful')
                if id:
                    query = f'''INSERT INTO Students
                            (id, name, surname, age, city)
                            VALUES ({id}, '{name}', '{surname}', {age}, '{city}');
                            '''
                else:
                    query = f'''INSERT INTO Students
                            ( name, surname, age, city)
                            VALUES ( '{name}', '{surname}', {age}, '{city}');
                            '''

                cursor.execute(query)
                connect.commit()
                logger.info('Record %s added to table Students', id)
            except sqlite3.Error as error:
                logger.error(error)

                if cursor:
                    cursor.close()
                return

            if connect:
                connect.close()
                logger.info('Disconnected to DB successful')

    def add_link(self, student_id:int, course_id:int):
        """Adding a link"""
        connect = None
        cursor = None

        try:
            connect = sqlite3.connect(self.db_name)
        except sqlite3.Error as error:
            logger.error(error)

        if connect:
            try:
                cursor = connect.cursor()
                logger.info('Connected to DB successful')

                query = f'''INSERT INTO Student_courses
                        (course_id, student_id)
                        VALUES ({course_id}, '{student_id}');
                        '''

                cursor.execute(query)
                connect.commit()
                logger.info('Record %s added to table student_courses')
            except sqlite3.Error as error:
                logger.error(error)

                if cursor:
                    cursor.close()
                return

            if connect:
                connect.close()
                logger.info('Disconnected to DB successful')

    def select_students(self, params):
        connect = None
        cursor = None

        s = list()
        for key, values in params:
            s.append(f"{key} {values['exp']} {values['val']} ")

        exp = s[0]
        query = 'Select * from Students Where ' + exp

        try:
            connect = sqlite3.connect(self.db_name)
        except sqlite3.Error as error:
            logger.error(error)

        if connect:
            try:
                cursor = connect.cursor()
                logger.info('Connected to DB successful')
                cursor.execute(query)
                connect.commit()
                logger.info('Record %s added to table student_courses')
            except sqlite3.Error as error:
                logger.error(error)

                if cursor:
                    cursor.close()
                return

            if connect:
                connect.close()
                logger.info('Disconnected to DB successful')






