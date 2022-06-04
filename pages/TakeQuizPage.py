import tkinter as tk
import csv

from entities.Course import Course
from pages.PageSingleton import PageSingleton


class TakeQuizPage(PageSingleton):
    def __init__(self, course_name, *args, **kwargs):
        PageSingleton.__init__(self, *args, **kwargs)
        self.course_name = course_name

        def verify(ans, exercises, cname):
            global grade

            ans = ans.strip().split(',')
            points = 0
            correct_ans = []

            for ex in exercises:
                correct_ans.append(ex.split(',')[1])
            for i in range(len(ans)):
                if ans[i].strip() == correct_ans[i]:
                    points += 1
            grade = points / len(exercises) * 100
            verify_button.config(state='disabled')

            with open('data/training_grades.csv', 'a', newline='') as file:
                spam_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                spam_writer.writerow([f"{cname}", f"{grade}"])

            self.destroy()

        frame = tk.LabelFrame(self, text=f'{self.course_name} Quiz', bg="Gray")
        frame.place(in_=self, relwidth=1)

        label1 = tk.Label(frame, text="Answer this questions with responses separated by comma", bg="Gray", fg='#FFF')
        label1.pack(side="left", expand=True)

        with open('data/trainings.csv', newline='') as csv_file:
            file_data = csv.reader(csv_file, delimiter=',', quotechar='"')

            for row in file_data:
                if row[0] == self.course_name:
                    quiz_exercises = row[1].splitlines()

                    for exercise in quiz_exercises:
                        exercise = exercise.split(',')

                        title_label = tk.Label(frame, text=exercise[0], bg="Gray", fg='#FFF')
                        title_label.pack(expand=True)

                    grade = 0

                    title_var = tk.StringVar()
                    title_entry = tk.Entry(frame, width="50", textvariable=title_var)
                    title_entry.pack(expand=True)

                    verify_button = tk.Button(
                        frame,
                        text="Submit results",
                        command=lambda: verify(title_var.get(), quiz_exercises, self.course_name)
                    )
                    verify_button.pack(expand=True)

