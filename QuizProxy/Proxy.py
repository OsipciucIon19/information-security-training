class Proxy:
    def __init__(self, subject):
        self._subject = subject
        self._proxy_state = None
