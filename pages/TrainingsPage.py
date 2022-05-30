import tkinter as tk
from pages.PageSingleton import PageSingleton


class TrainingsPage(PageSingleton):
    def __init__(self, *args, **kwargs):
        PageSingleton.__init__(self, *args, **kwargs)