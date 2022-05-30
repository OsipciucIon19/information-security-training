import tkinter as tk
from pages.PageSingleton import PageSingleton


class ProgressPage(PageSingleton):
    def __init__(self, *args, **kwargs):
        PageSingleton.__init__(self, *args, **kwargs)

        messages = 'test'

        label = tk.Text(self, width="80", height="35")
        label.insert(tk.END, messages)
        label.pack(expand=True)
