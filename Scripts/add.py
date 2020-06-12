import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from bd import Table
import app as m
from tkinter import messagebox as mb


class Child_add(tk.Toplevel):
    def __init__(self, parent_):
        '''
        Функция вызывает окно добавления нового кортежа в таблицу
        Получает: -
        Возвращает: -
        Автор: Будин А.М., Матвеев В.Е.
        '''
        super().__init__(parent_)
        global df, parent
        df = m.mdf
        parent = parent_
        self.title('Добавление')
        self.geometry('260x260+400+300')
        self.resizable(False, False)
        def add():
            '''
            Функция добавляет новый кортеж в таблицу
            Получает: -
            Возвращает: -
            Автор: Будин А.М.
            '''
            global counter, df, parent
            if(entry_firm.get() != '' and entry_country.get() != '' and
               entry_model.get() != '' and entry_storage.get() != '' and
               entry_diagonal.get() != '' and entry_cpu.get() != '' and
               entry_ram.get() != '' and entry_amount.get() != '' and
               combobox.get() != ''):
                if (entry_ram.get().isdigit() == False and
                    entry_storage.get().isdigit() == False and
                    entry_diagonal.get().isdigit() == False and
                    entry_amount.get().isdigit() == False):
                    mb.showerror("Ошибка", """Должны быть введены числа в полях 'Память', 'Оперативная память' и 'Количество'""")
                else:
                    Table_add(entry_firm.get(), entry_country.get(),
                              entry_model.get(), entry_storage.get(),
                              entry_diagonal.get(), entry_cpu.get(), 
                              entry_ram.get(), entry_amount.get(), 
                              combobox.get())
                    self.destroy()
            else:
                mb.showerror("Ошибка", "Введите данные во все поля")


        def Table_add(firm, country, model, storage, diagonal, cpu,
        ram, amount, os):
            '''
            Функция добавляет новый кортеж в таблицу
            Получает: firm - название фирмы производителя,
                country - страна производителя,
                model - модель телефона, storage - объём памяти,
                diagonal - диагональ экрана, cpu - модель процессора,
                ram - объём оперативной памяти, amount - количество (штук),
                os - операционная система
            Возвращает: -
            Автор: Матвеев В.Е.
            '''
            global count, parent
            try:
                counter = m.mdf.loc[len(m.mdf)-1]["Product Code"]
            except(KeyError):
                counter = 0
            m.mdf.loc[len(m.mdf)] = [int(counter) + 1, firm, country,
                      str(model), os, int(storage), float(diagonal),
                      cpu, int(ram), int(amount)]
            for widget in parent.winfo_children():
                widget.destroy()
            Table(parent, m.mdf)


        label_description = ttk.Label(self, text='Операционная система')
        label_description.grid(row=10, column = 0)
        label_description = ttk.Label(self, text='Производитель')
        label_description.grid(row=2, column =0)
        label_description = ttk.Label(self, text='Страна')
        label_description.grid(row=3, column =0)
        label_description = ttk.Label(self, text='Модель')
        label_description.grid(row=4, column =0)
        label_description = ttk.Label(self, text='Память')
        label_description.grid(row=5, column =0)
        label_description = ttk.Label(self, text='Диагональ')
        label_description.grid(row=6, column =0)
        label_description = ttk.Label(self, text='Процессор')
        label_description.grid(row=7, column =0)
        label_description = ttk.Label(self, text='Оперативная память')
        label_description.grid(row=8, column =0)
        label_description = ttk.Label(self, text='Количество')
        label_description.grid(row=9, column =0)
        entry_firm = ttk.Entry(self)
        entry_firm.grid(row=2, column=1)
        entry_country = ttk.Entry(self)
        entry_country.grid(row=3, column=1)
        entry_model = ttk.Entry(self)
        entry_model.grid(row=4, column=1)
        entry_storage = ttk.Entry(self)
        entry_storage.grid(row=5, column=1)
        entry_diagonal = ttk.Entry(self)
        entry_diagonal.grid(row=6, column=1)
        entry_cpu = ttk.Entry(self)
        entry_cpu.grid(row=7, column=1)
        entry_ram = ttk.Entry(self)
        entry_ram.grid(row=8, column=1)
        entry_amount = ttk.Entry(self)
        entry_amount.grid(row=9, column=1)
        combobox = ttk.Combobox(self, values=[u'Android',u'IOS', u'BlackBerry'],
        width=17)
        combobox.grid(row=10, column=1)
        btn_cancel = ttk.Button(self, text='Отмена', command=self.destroy)
        btn_cancel.grid(row=13, column=0, columnspan=2)
        btn_add = ttk.Button(self, text='Добавить', command=add)
        btn_add.grid(row=12, column=0, columnspan=2)
        btn_add.bind('<Button-1>')
        self.grab_set()
        self.focus_set()
