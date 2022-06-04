import csv
import tkinter as tk

from entities.Quiz import Quiz
from pages.PageSingleton import PageSingleton


class TrainingsPage(PageSingleton):
    def __init__(self, *args, **kwargs):
        PageSingleton.__init__(self, *args, **kwargs)

        with open('data/trainings.csv', newline='') as csv_file:
            file_data = csv.reader(csv_file, delimiter=',', quotechar='"')

            for row in file_data:
                frame = tk.Frame(self, bg="Gray")
                frame.pack(fill="x", ipady=5)

                quiz = Quiz(row[0])

                print(quiz.get_name())

                label1 = tk.Label(frame, text=row[0], bg="Gray", fg='#FFF')
                label1.pack(side="left", expand=True)
                button1 = tk.Button(frame, text='Take quiz', command=lambda: quiz.take_quiz())
                button1.pack(side="right", ipadx=50)
