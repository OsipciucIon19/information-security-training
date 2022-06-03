import tkinter as tk
import csv
from pages.PageSingleton import PageSingleton
from pages.CoursePage import CoursePage


class ViewCoursesPage(PageSingleton):
    def __init__(self, *args, **kwargs):
        PageSingleton.__init__(self, *args, **kwargs)

        def open_course(course):
            course_page = CoursePage(course)
            course_page.config(bg="Gray")
            course_page.lift()

        with open('data/courses.csv', newline='') as csv_file:
            file_data = csv.reader(csv_file, delimiter=',', quotechar='"')

            for row in file_data:
                frame = tk.Frame(self, bg="Gray")
                frame.pack(fill="x", ipady=5)

                label1 = tk.Label(frame, text=row[0], bg="Gray", fg='#FFF')
                label1.pack(side="left", expand=True)
                button1 = tk.Button(frame, text='->', command=lambda course=row: open_course(course))
                button1.pack(side="right", ipadx=50)
                label2 = tk.Label(frame, text=f"Course Type: {row[1]}", bg="Gray", fg="#c3c3c3")
                label2.pack(side="right")
