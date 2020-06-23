"""
Функция вызывает окно удаления кортежа
Получает: -
Возвращает: -
Автор: Матвеев В.Е., Демидов И.Д., Будин А.М.
"""
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import numpy as np
from Library import bd
import app as m
from tkinter import messagebox as mb


class Delete(tk.Toplevel):
    def __init__(self, parent_):
        '''
        Функция вызывает окно удаления кортежа
        Получает: -
        Возвращает: -
        Автор: Демидов И.Д
        '''
        super().__init__(parent_)
        global parent
        parent = parent_
        self.title('Удаление смартфона')
        self.geometry('250x100+400+300')
        self.resizable(False, False)

        def delete_code():
            '''
            Функция удаляет выбранный кортеж
            Получает: -
            Возвращает: -
            Автор: Демидов И.Д
            '''
            global parent
            if(choice.get() == ''):
                mb.showerror("Ошибка", "Введите код продукта")
            elif (m.mdf.loc[len(m.mdf)-1]["Product Code"] < int(choice.get())):
                mb.showerror("Ошибка", "Нет такого продукта")
            else:
                m.mdf = m.mdf.drop(np.where(m.mdf['Product Code'] == int(choice.get()))[0])
                for widget in parent.winfo_children():
                    widget.destroy()
                bd.Table(parent, m.mdf)
                self.destroy()


        label_choice = ttk.Label(self, text='''Введите код товара, который хотите удалить''')
        label_choice.grid(row=0, column=0, columnspan=2)
        choice = ttk.Entry(self)
        choice.grid(row=1, column=0, columnspan=2)
        cancel_but = ttk.Button(self, text='Отмена', command=self.destroy)
        cancel_but.grid(row=2, column=1)
        del_but = ttk.Button(self, text='Удалить', command=delete_code)
        del_but.grid(row=2, column=0)
        del_but.bind('<Button-1>')
