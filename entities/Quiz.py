from pages.TakeQuizPage import TakeQuizPage


class Quiz:
    def __init__(self, quiz_name):
        self.quiz_name = quiz_name

    def take_quiz(self):
        quiz = TakeQuizPage(self.quiz_name)
        quiz.config(bg="Gray")
        quiz.lift()
