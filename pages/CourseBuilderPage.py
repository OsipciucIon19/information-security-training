import csv
import tkinter as tk
from pages.PageSingleton import PageSingleton
from CourseBuilder.Director import Director
from CourseBuilder.builder import WebCourseBuilder, ApiCourseBuilder, FrontEndCourseBuilder


class CourseBuilderPage(PageSingleton):
    COURSE_TYPES = ["Web", "Api", "Front-end"]

    def __init__(self, *args, **kwargs):
        PageSingleton.__init__(self, *args, **kwargs)

        def create_course():
            builder = None
            course_type = type_var.get()
            if course_type == 'Web':
                builder = WebCourseBuilder(
                    title_var.get(),
                    content_text.get('1.0', tk.END)
                )
            elif course_type == 'Api':
                builder = ApiCourseBuilder(
                    title_var.get(),
                    content_text.get('1.0', tk.END)
                )
            elif course_type == 'Front-end':
                builder = FrontEndCourseBuilder(
                    title_var.get(),
                    content_text.get('1.0', tk.END)
                )

            director = Director()
            director.set_builder(builder)
            course = director.get_course()
            print(course.get_course())

            with open('data/courses.csv', 'a', newline='') as csv_file:
                spam_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                spam_writer.writerow(course.get_course())

            title_entry.delete(0, tk.END)
            type_var.set(self.COURSE_TYPES[0])
            content_text.delete('1.0', tk.END)

        title_label = tk.Label(self, text="Course Title:", bg="Gray", fg='#FFF')
        title_var = tk.StringVar()
        title_entry = tk.Entry(self, width="50", textvariable=title_var)
        title_label.pack(expand=True)
        title_entry.pack(expand=True)

        type_label = tk.Label(self, text="Type:", bg="Gray", fg='#FFF')
        type_label.pack(expand=True)

        type_var = tk.StringVar()
        type_var.set(self.COURSE_TYPES[0])

        type_dropdown = tk.OptionMenu(self, type_var, *self.COURSE_TYPES)
        type_dropdown.pack(expand=True)

        content_label = tk.Label(self, text="Content:", bg="Gray", fg='#FFF')
        content_label.pack(expand=True)
        content_text = tk.Text(self,width="50", height="25")
        content_text.pack(expand=True)

        create = tk.Button(self, text="Create", command=create_course)
        create.pack(expand=True)
