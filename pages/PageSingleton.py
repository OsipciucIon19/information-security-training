import tkinter as tk


class PageSingleton(tk.Frame):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(PageSingleton, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self, *args, **kwargs):
        if self.__initialized: return
        self.__initialized = True
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()
