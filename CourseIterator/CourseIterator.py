from abc import ABC, abstractmethod


class AbstractIterator(ABC):
    @abstractmethod
    def has_next(self): pass

    @abstractmethod
    def next(self): pass


class CourseIterator(AbstractIterator):
    def __init__(self, courses):
        self.index = 0
        self.courses = courses

    def has_next(self):
        return True if self.index < len(self.courses) else False

    def next(self):
        course = self.courses[self.index]
        self.index += 1
        return course

    def get_length(self):
        return len(self.courses)
