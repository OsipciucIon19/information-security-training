import csv
import tkinter as tk

from CourseIterator.Progress import Progress
from ProgressReports.Report import Report
from ProgressReports.handlers import PDFHandler, GUIHandler
from pages.PageSingleton import PageSingleton


class ProgressPage(PageSingleton):
    def __init__(self, *args, **kwargs):
        PageSingleton.__init__(self, *args, **kwargs)

        def funct():
            gui_handler.nextHandler = pdf_handler
            gui_handler.nextHandler.handle(report)

        with open('data/training-grades.csv', newline='') as csv_file:
            file_data = csv.reader(csv_file, delimiter=',', quotechar='"')

            courses = []
            for row in file_data:
                courses.append(row)

        progress = Progress(courses)
        iterator = progress.iterator()

        while iterator.has_next():
            course = iterator.next()

            frame = tk.Frame(self, bg="Gray")
            frame.pack(fill="x", ipady=5)

            label1 = tk.Label(frame, text=course[0], bg="Gray", fg='#FFF')
            label1.pack(side="left", expand=True)

            label2 = tk.Label(frame, text=f"--> \t\t\t\t {course[1]} %", bg="Gray", fg="#c3c3c3")
            label2.pack(side="right")

        report = Report('gui', courses)
        pdf_handler = PDFHandler()
        gui_handler = GUIHandler()
        avg_grade = gui_handler.handle(report)

        total_label1 = tk.Label(self, text='Overall progress:', bg="Gray", fg='#FFF')
        total_label1.pack(side="left", expand=True)

        total_label2 = tk.Label(self, text=f"--> \t\t\t\t {avg_grade} %", bg="Gray", fg="#c3c3c3")
        total_label2.pack(side="right")

        button = tk.Button(
            self,
            text="Generate PDF Report",
            command=lambda: funct()
        )
        button.place(x=600, y=500)

