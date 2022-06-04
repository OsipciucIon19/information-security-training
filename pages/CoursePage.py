import tkinter as tk

from QuizAdapter.QuizAdapter import QuizAdapter
from entities.Course import Course
from pages.PageSingleton import PageSingleton
from pages.TakeQuizPage import TakeQuizPage


class CoursePage(PageSingleton):
    def __init__(self, *args, **kwargs):
        PageSingleton.__init__(self, *args, **kwargs)
        self.args = args

        frame = tk.LabelFrame(self, text='Course Title', bg="Gray")
        frame.place(in_=self, relwidth=1)

        if len(args) > 0:
            course = Course()
            course.set_title(args[0][0])
            course.set_type(args[0][1])
            course.set_content(args[0][2])

            label1 = tk.Label(frame, text=course.get_course()[0], bg="Gray", fg='#FFF')
            label1.pack(side="left", expand=True)

            label2 = tk.Text(frame, width="150", height="35", bg="#c3c3c3")
            label2.insert(tk.END, course.get_course()[2])
            label2.pack(side="bottom")

            quiz = QuizAdapter(course)

            button1 = tk.Button(frame, text='Take quiz', command=lambda: quiz.take_quiz())
            button1.pack(side="right", ipadx=50)

