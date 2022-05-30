class Course:
    def __init__(self):
        self.__title = None
        self.__type = None
        self.__content = None

    def set_title(self, title):
        self.__title = title

    def set_type(self, course_type):
        self.__type = course_type

    def set_content(self, content):
        self.__content = content

    def get_course(self):
        return [self.__title, self.__type, self.__content]
