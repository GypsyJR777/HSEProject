"""
Функция вызывает окно изменения выбранного кортежа
Получает: -
Возвращает: -
Автор: Матвеев В.Е., Демидов И.Д., Будин А.М.
"""
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import os, sys
sys.path.insert(0, os.path.abspath("../Library"))
import bd
sys.path.insert(0, os.path.abspath("../Scripts"))
import app as m
import pandas as pd
from tkinter import messagebox as mb

class Change(tk.Toplevel):
    def __init__(self, parent_):
        '''
        Функция вызывает окно изменения выбранного кортежа
        Получает: parent_ - окно родителя
        Возвращает: -
        Автор: Демидов И.Д
        '''
        super().__init__()
        global df, parent
        df = m.mdf
        parent = parent_
        self.title('Изменение данных о смартфоне')
        self.geometry('300x70+400+300')
        self.resizable(False, False)


        def new_list_values(stolb_name):
            '''
            функция создает новые список уникальных значений после применения
            фильтра
            Получает: stolb_name - название столбца
            Возвращает: new_list - обновленный список уникальных значений
            Автор: Будин А.М., Матвеев В.Е.
            '''
            global df
            new_list = pd.unique(df[stolb_name]).tolist()
            return new_list


        def ok():
            '''
            Функция обновляет окно и заполняет данными поля ввода
            Получает: -
            Возвращает: -
            Автор: Демидов И.Д
            '''
            global parent
            string = np.array(m.mdf[m.mdf['Product Code'] == int(entry_code.get())])
            if(len(string)>0):
                self.geometry('300x300+400+300')
                ok_btn.grid_remove()
                label_description = ttk.Label(self, text='Операционная система')
                label_description.grid(row=10, column=0)
                label_description = ttk.Label(self, text='Производитель')
                label_description.grid(row=2, column=0)
                label_description = ttk.Label(self, text='Страна')
                label_description.grid(row=3, column=0)
                label_description = ttk.Label(self, text='Модель')
                label_description.grid(row=4, column=0)
                label_description = ttk.Label(self, text='Память')
                label_description.grid(row=5, column=0)
                label_description = ttk.Label(self, text='Диагональ')
                label_description.grid(row=6, column=0)
                label_description = ttk.Label(self, text='Процессор')
                label_description.grid(row=7, column=0)
                label_description = ttk.Label(self, text='Оперативная память')
                label_description.grid(row=8, column=0)
                label_description = ttk.Label(self, text='Количество')
                label_description.grid(row=9, column=0)
                string = np.array(m.mdf[m.mdf['Product Code'] == int(entry_code.get())])
                change_entry_firm.insert(0, string[0][1])
                change_entry_firm.grid(row=2, column=1, columnspan=2)
                change_entry_country.insert(0, string[0][2])
                change_entry_country.grid(row=3, column=1, columnspan=2)
                change_entry_model.insert(0, string[0][3])
                change_entry_model.grid(row=4, column=1, columnspan=2)
                change_combobox.insert(0, string[0][4])
                change_combobox.grid(row=10, column=1, columnspan=2)
                change_entry_storage.insert(0, string[0][5])
                change_entry_storage.grid(row=5, column=1)
                change_entry_diagonal.insert(0, string[0][6])
                change_entry_diagonal.grid(row=6, column=1)
                change_entry_cpu.insert(0, string[0][7])
                change_entry_cpu.grid(row=7, column=1, columnspan=2)
                change_entry_ram.insert(0, string[0][8])
                change_entry_ram.grid(row=8, column=1)
                change_entry_amount.insert(0, string[0][9])
                change_entry_amount.grid(row=9, column=1)
                change_btn_cancel.grid(row=14, column=0, columnspan=2)
                change_btn.grid(row=13, column=0, columnspan=2)
            else:
                mb.showerror("Ошибка", "Нет такого смартфона")


        def change_df():
            '''
            Функция изменяет данные выбранного кортежа
            Получает: -
            Возвращает: -
            Автор: Демидов И.Д
            '''
            global parent
            try:
                m.mdf.loc[int(entry_code.get())-1] = [entry_code.get(),
                          change_entry_firm.get(), change_entry_country.get(),
                          change_entry_model.get(), change_combobox.get(),
                          int(change_entry_storage.get()),
                          float(change_entry_diagonal.get()),
                          change_entry_cpu.get(), int(change_entry_ram.get()),
                          int(change_entry_amount.get())]
                for widget in parent.winfo_children():
                    widget.destroy()
                bd.Table(parent, m.mdf)
            except(ValueError):
                mb.showerror("Ошибка", "Должны быть введены числа в полях 'Память', 'Оперативная память' и 'Количество'")




        label_description = ttk.Label(self, text='Код товара для изменения')
        label_description.grid(row=0, column = 0)
        list_code = new_list_values("Product Code")
        entry_code = ttk.Combobox(self, values=list_code)
        entry_code.grid(row=0, column=1, columnspan=2)
        ok_btn = ttk.Button(self, text='OK', command=ok)
        ok_btn.grid(row=15, column=0, columnspan=3)
        change_entry_firm = ttk.Entry(self)
        change_entry_country = ttk.Entry(self)
        change_entry_model = ttk.Entry(self)
        change_entry_storage = ttk.Entry(self)
        change_entry_diagonal = ttk.Entry(self)
        change_entry_cpu = ttk.Entry(self)
        change_entry_ram = ttk.Entry(self)
        change_entry_amount = ttk.Entry(self)
        change_combobox = ttk.Combobox(self, values=[u'Android',u'IOS',
        u'BlackBerry'], width=17)
        change_btn_cancel = ttk.Button(self, text='Отмена')
        change_btn = ttk.Button(self, text='Применить', command=change_df)
