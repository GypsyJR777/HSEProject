import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import numpy as np
from bd import Table
import app as m


class Delete(tk.Toplevel):
    def __init__(self, parent_):
        super().__init__(parent_)
    #    self.init_child()


    #def init_child(self):
        global parent
        parent = parent_
        self.title('Удаление смартфона')
        self.geometry('400x400+400+300')
        self.resizable(False, False)
        def delete_code():
            global parent
            if(choice.get() == ''):
                mb.showerror("Ошибка", "Введите код продукта")
            else:
                m.mdf = m.mdf.drop(np.where(m.mdf['Product Code'] == int(choice.get()))[0])
                for widget in parent.winfo_children():
                    widget.destroy()
                Table(parent, m.mdf)
                self.destroy()

        label_choice = ttk.Label(self, text='Введите код товара, который хотите удалить')
        label_choice.grid(row=0, column=0, columnspan=2)

        choice = ttk.Entry(self)
        choice.grid(row=1, column=0, columnspan=2)

        cancel_but = ttk.Button(self, text='Отмена', command=self.destroy)
        cancel_but.grid(row=2, column=1)

        del_but = ttk.Button(self, text='Удалить', command=delete_code)
        del_but.grid(row=2, column=0)
        del_but.bind('<Button-1>')
