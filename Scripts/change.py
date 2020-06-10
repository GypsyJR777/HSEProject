import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

class Change(tk.Toplevel):

    def __init__(self):
        super().__init__(root)
        self.init_child()


    def init_child(self):
        global mdf
        self.title('Изменение данных о смартфоне')
        self.geometry('300x100+400+300')
        self.resizable(False, False)
        label_description = ttk.Label(self, text='Код товара для изменения')
        label_description.grid(row=0, column = 0)
        entry_code = ttk.Entry(self)
        entry_code.grid(row=0, column=1, columnspan=2)
        ok_btn = ttk.Button(self, text='OK')
        ok_btn.grid(row=15, column=0, columnspan=3)
