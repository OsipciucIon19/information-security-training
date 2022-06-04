import tkinter as tk

from pages.CourseBuilderPage import CourseBuilderPage
from pages.ProgressPage import ProgressPage
from pages.TrainingsPage import TrainingsPage
from pages.ViewCoursesPage import ViewCoursesPage
from pages.CoursePage import CoursePage
from pages.TakeQuizPage import TakeQuizPage


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        view_courses_page = ViewCoursesPage()
        view_courses_page.config(bg="Gray")

        course_page = CoursePage()
        course_page.config(bg="Gray")

        trainings_page = TrainingsPage()
        trainings_page.config(bg="Gray")

        progress_page = ProgressPage()
        progress_page.config(bg="Gray")

        course_builder_page = CourseBuilderPage()
        course_builder_page.config(bg="Gray")

        take_quiz_page = TakeQuizPage(course_name=None)
        take_quiz_page.config(bg="Gray")

        button_bar = tk.Frame(self)
        container = tk.Frame(self)
        button_bar.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        view_courses_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        course_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        trainings_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        progress_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        course_builder_page.place(in_=container,x=0, y=0, relwidth=1, relheight=1)
        take_quiz_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        view_courses_btn = tk.Button(button_bar, text="View Courses", command=view_courses_page.lift)
        trainings_btn = tk.Button(button_bar, text="Trainings", command=trainings_page.lift)
        progress_btn = tk.Button(button_bar, text="Progress", command=progress_page.lift)
        course_builder_btn = tk.Button(button_bar, text="Create a course", command=course_builder_page.lift)

        view_courses_btn.pack(side="left")
        trainings_btn.pack(side="left")
        progress_btn.pack(side="left")
        course_builder_btn.pack(side="left")

        view_courses_page.show()
