from CourseIterator.CourseIterator import CourseIterator


class Progress:
    def __init__(self, courses):
        self.courses = courses

    def add(self, course):
        self.courses.append(course)

    def remove(self):
        return self.courses.pop()

    def iterator(self):
        return CourseIterator(self.courses)
