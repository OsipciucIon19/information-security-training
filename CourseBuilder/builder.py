class Builder:
    def get_title(self): pass

    def get_type(self): pass

    def get_content(self): pass


class WebCourseBuilder(Builder):
    __title = None
    __type = 'Web'
    __content = None

    def __init__(self, title, content):
        self.__title = title
        self.__content = content

    def get_title(self):
        return self.__title

    def get_type(self):
        return self.__type

    def get_content(self):
        return self.__content


class ApiCourseBuilder(Builder):
    __title = None
    __type = 'Api'
    __content = None

    def __init__(self, title, content):
        self.__title = title
        self.__content = content

    def get_title(self):
        return self.__title

    def get_type(self):
        return self.__type

    def get_content(self):
        return self.__content


class FrontEndCourseBuilder(Builder):
    __title = None
    __type = 'Front-end'
    __content = None

    def __init__(self, title, content):
        self.__title = title
        self.__content = content

    def get_title(self):
        return self.__title

    def get_type(self):
        return self.__type

    def get_content(self):
        return self.__content
