import csv
import tkinter as tk

from CourseIterator.Progress import Progress
from pages.PageSingleton import PageSingleton


class ProgressPage(PageSingleton):
    def __init__(self, *args, **kwargs):
        PageSingleton.__init__(self, *args, **kwargs)

    with open('data/training_grades.csv', newline='') as csv_file:
        file_data = csv.reader(csv_file, delimiter=',', quotechar='"')

        courses = []
        for row in file_data:
            courses.append(row)

        progress = Progress(courses)

        iterator = progress.iterator()

        while iterator.has_next():
            course = iterator.next()
            print(course)
