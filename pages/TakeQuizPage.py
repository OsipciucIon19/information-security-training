import tkinter as tk
import csv
from pages.PageSingleton import PageSingleton


class TakeQuizPage(PageSingleton):
    def __init__(self, course_name, *args, **kwargs):
        PageSingleton.__init__(self, *args, **kwargs)
        self.course_name = course_name

        def verify(cans):
            block.set(1)

            if title_var.get() == cans:
                print(1)
                return 1
            else:
                print(0)
                return 0

        frame = tk.LabelFrame(self, text=f'{course_name} Quiz', bg="Gray")
        frame.place(in_=self, relwidth=1)

        label1 = tk.Label(frame, text=course_name, bg="Gray", fg='#FFF')
        label1.pack(side="left", expand=True)

        with open('data/trainings.csv', newline='') as csv_file:
            file_data = csv.reader(csv_file, delimiter=',', quotechar='"')

            for row in file_data:
                if row[0] == course_name:
                    quiz_exercises = row[1].splitlines()

                    points = 0
                    max_points = len(quiz_exercises)
                    block = tk.IntVar()

                    for exercise in quiz_exercises:
                        exercise = exercise.split(',')
                        print(block.get())

                        title_label = tk.Label(self, text=exercise[0], bg="Gray", fg='#FFF')
                        title_label.pack(expand=True)

                        title_var = tk.StringVar()
                        title_entry = tk.Entry(self, width="50", textvariable=title_var)
                        title_entry.pack(expand=True)

                        create = tk.Button(
                            self,
                            text="Check result",
                            # command=lambda correct_answer=exercise[1]: verify(correct_answer)
                            command= lambda: block.set(1)
                        )
                        create.pack(expand=True)

                        # create.wait_variable(block)


