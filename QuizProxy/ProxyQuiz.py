from QuizProxy.Proxy import Proxy


class ProxyQuiz(Proxy):
    def take_quiz(self):
        if self._proxy_state is None:
            self._subject.take_quiz()
            self._proxy_state = 1
