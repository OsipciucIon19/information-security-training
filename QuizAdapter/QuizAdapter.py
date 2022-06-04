from entities import Course
from pages.TakeQuizPage import TakeQuizPage


class QuizAdapter:
    course: Course

    def __init__(self, course):
        self.course = course

    def take_quiz(self):
        quiz = TakeQuizPage(self.course)
        print(quiz)
        quiz.config(bg="Gray")
        quiz.lift()
