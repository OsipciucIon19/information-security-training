from CourseBuilder.Course import Course


class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_course(self):
        course = Course()

        title = self.__builder.get_title()
        course.set_title(title)

        course_type = self.__builder.get_type()
        course.set_type(course_type)

        content = self.__builder.get_content()
        course.set_content(content)

        return course
