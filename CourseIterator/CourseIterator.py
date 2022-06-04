from abc import ABC, abstractmethod


class AbstractIterator(ABC):
    @abstractmethod
    def has_next(self): pass

    @abstractmethod
    def next(self): pass


class CourseIterator(AbstractIterator):
    def __init__(self, courses):
        self.index = 0
        self.course_names = courses

    def has_next(self):
        return True if self.index < len(self.course_names) else False

    def next(self):
        course = self.course_names[self.index]
        self.index += 1
        return course
