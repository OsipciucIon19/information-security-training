from entities import Course
from entities.Quiz import Quiz
from pages.TakeQuizPage import TakeQuizPage


class QuizAdapter(Quiz):
    course: Course

    def __init__(self, course):
        super().__init__(self)
        self.course = course

    def take_quiz(self):
        quiz = TakeQuizPage(self.course.get_course()[0])
        quiz.config(bg="Gray")
        quiz.lift()
