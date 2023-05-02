import logging
import sys
import datetime

from my_db import BD

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    stream=sys.stdout,
)

logger = logging.getLogger(__name__)

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

