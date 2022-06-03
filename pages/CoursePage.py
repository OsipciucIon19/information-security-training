import tkinter as tk
from pages.PageSingleton import PageSingleton
from pages.TakeQuizPage import TakeQuizPage


class CoursePage(PageSingleton):
    def __init__(self, *args, **kwargs):
        PageSingleton.__init__(self, *args, **kwargs)
        self.args = args

        def take_quiz(course_name):
            quiz = TakeQuizPage(course_name)
            quiz.config(bg="Gray")
            quiz.lift()

        frame = tk.LabelFrame(self, text='Course Title', bg="Gray")
        frame.place(in_=self, relwidth=1)

        if len(args) > 0:
            course = args[0]
            label1 = tk.Label(frame, text=course[0], bg="Gray", fg='#FFF')
            label1.pack(side="left", expand=True)

            label2 = tk.Text(frame, width="150", height="35", bg="#c3c3c3")
            label2.insert(tk.END, course[2])
            label2.pack(side="bottom")
            button1 = tk.Button(frame, text='Take quiz', command=lambda course_name=course[0]:take_quiz(course_name))
            button1.pack(side="right", ipadx=50)

