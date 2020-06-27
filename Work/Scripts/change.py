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
        global df, parent, xls1, xls2, xls3
        df = m.mdf
        xls1=m.mxls1
        xls2=m.mxls2
        xls3=m.mxls3
        parent = parent_
        self.title('Изменение данных о смартфоне')
        self.geometry('300x130+400+300')
        self.resizable(False, False)


        def new_list_values(stolb_name):
            '''
            функция создает новые список уникальных значений после применения
            фильтра
            Получает: stolb_name - название столбца
            Возвращает: new_list - обновленный список уникальных значений
            Автор: Будин А.М., Матвеев В.Е.
            '''
            if stolb_name == 'Manufacturer':
                new_list = pd.unique(m.mxls1[stolb_name]).tolist()
            if stolb_name == 'Model':
                new_list = pd.unique(m.mxls3[stolb_name]).tolist()
            if stolb_name == 'Product Code':
                new_list = pd.unique(m.mxls2[stolb_name]).tolist()
            return new_list


        def change_country():
            '''
            Функция изменяет страну производителя
            Получает: -
            Возвращает: -
            Автор: Демидов И.Д
            '''
            global parent
            try:
                m.mxls1['Country'][m.mxls1["Manufacturer"] == change_entry_firm.get()] = change_entry_country.get()
                for widget in parent.winfo_children():
                    widget.destroy()
                bd.Table(parent, m.mxls1, m.mxls2, m.mxls3)
                self.destroy()
            except(ValueError):
                mb.showerror("Ошибка", "Должны быть введены данные во все поля")


        def ok3():
            '''
            Функция обновляет окно, отображает в окне инструменты редактирования
            справочника и заполняет данными поля ввода
            Получает: -
            Возвращает: -
            Автор: Будин А.М.
            '''
            global parent
            self.geometry('250x120+400+300')
            table1_btn.grid_remove()
            table2_btn.grid_remove()
            table3_btn.grid_remove()
            label_description1.grid_remove()
            label_description2.grid_remove()
            label_description3.grid_remove()
            label_description = ttk.Label(self, text='Производитель')
            label_description.grid(row=1, column=0)

            label_description = ttk.Label(self, text='Страна')
            label_description.grid(row=2, column=0)
            change_entry_firm.grid(row=1, column=1, columnspan=1)
            change_entry_country.grid(row=2, column=1, columnspan=1)
            change_btn_cancel = ttk.Button(self, text='Отмена', command=cancel)
            change_btn = ttk.Button(self, text='Применить', command=change_country)
            change_btn_cancel.grid(row=4, column=0, columnspan=2)
            change_btn.grid(row=3, column=0, columnspan=2)


        def change_of_model():
            global parent
            try:
                m.mxls3['Diagonal'][m.mxls3["Model"] == change_entry_model.get()] = float(change_entry_diagonal.get())
                m.mxls3['OS'][m.mxls3["Model"] == change_entry_model.get()] = change_combobox.get()
                m.mxls3['Manufacturer'][m.mxls3["Model"] == change_entry_model.get()] = change_entry_firm.get()
                for widget in parent.winfo_children():
                    widget.destroy()
                bd.Table(parent, m.mxls1, m.mxls2, m.mxls3)
                self.destroy()
            except(ValueError):
                mb.showerror("Ошибка", "Должны быть введены данные во все поля")


        def change_of_code():
            global parent
            try:
                m.mxls2['Storage'][m.mxls2["Product Code"] == int(entry_code.get())] = int(change_entry_storage.get())
                m.mxls2['CPU'][m.mxls2["Product Code"] == int(entry_code.get())] = change_entry_cpu.get()
                m.mxls2['RAM'][m.mxls2["Product Code"] == int(entry_code.get())] = int(change_entry_ram.get())
                m.mxls2['Amount'][m.mxls2["Product Code"] == int(entry_code.get())] = int(change_entry_amount.get())
                m.mxls2['Model'][m.mxls2["Product Code"] == int(entry_code.get())] = change_entry_model.get()
                for widget in parent.winfo_children():
                    widget.destroy()
                bd.Table(parent, m.mxls1, m.mxls2, m.mxls3)
                self.destroy()
            except(ValueError):
                mb.showerror("Ошибка", "Должны быть введены данные во все поля")

        def ok1():
            '''
            Функция обновляет окно, отображает в окне инструменты редактирования
            справочника и заполняет данными поля ввода
            Получает: -
            Возвращает: -
            Автор: Будин А.М.
            '''
            global parent
            string = np.array(m.mdf[m.mdf['Product Code'] == 1])
            # if(len(string)>0):
            if(1):
                self.geometry('270x180+400+300')
                label_description = ttk.Label(self, text='Код для изменения')
                label_description.grid(row=0, column = 0, columnspan=1)

                table1_btn.grid_remove()
                table2_btn.grid_remove()
                table3_btn.grid_remove()
                label_description1.grid_remove()
                label_description2.grid_remove()
                label_description3.grid_remove()

                #нужно условие
                label_description = ttk.Label(self, text='Модель')
                label_description.grid(row=1, column=0)

                label_description = ttk.Label(self, text='Память')
                label_description.grid(row=2, column=0)
                label_description = ttk.Label(self, text='Процессор')
                label_description.grid(row=3, column=0)
                label_description = ttk.Label(self, text='Оперативная память')
                label_description.grid(row=4, column=0)
                label_description = ttk.Label(self, text='Количество')
                label_description.grid(row=5, column=0)
                string = np.array(m.mdf[m.mdf['Product Code'] == 1])
                change_entry_model.grid(row=1, column=1, columnspan=2)
                change_entry_storage.grid(row=2, column=1, columnspan=2)
                change_entry_cpu.grid(row=3, column=1, columnspan=2)
                change_entry_ram.grid(row=4, column=1)
                entry_code.grid(row=0, column=1, columnspan=2)
                change_entry_amount.grid(row=5, column=1)
                change_btn_cancel = ttk.Button(self, text='Отмена', command=cancel)
                change_btn = ttk.Button(self, text='Применить', command=change_of_code)
                change_btn_cancel.grid(row=7, column=0, columnspan=2)
                change_btn.grid(row=6, column=0, columnspan=2)

        def ok2():
            '''
            Функция обновляет окно, отображает в окне инструменты редактирования
            справочника и заполняет данными поля ввода
            Получает: -
            Возвращает: -
            Автор: Будин А.М.
            '''
            global parent
            string = np.array(m.mdf[m.mdf['Product Code'] == 1])
            # if(len(string)>0):
            if(1):
                self.geometry('280x160+400+300')
                table1_btn.grid_remove()
                table2_btn.grid_remove()
                table3_btn.grid_remove()
                label_description1.grid_remove()
                label_description2.grid_remove()
                label_description3.grid_remove()
                label_description = ttk.Label(self, text='Операционная система')
                label_description.grid(row=3, column=0)
                label_description = ttk.Label(self, text='Производитель')
                label_description.grid(row=2, column=0)
                label_description = ttk.Label(self, text='Модель')
                label_description.grid(row=1, column=0)
                label_description = ttk.Label(self, text='Диагональ')
                label_description.grid(row=4, column=0)
                string = np.array(m.mdf[m.mdf['Product Code'] == 1])
                change_entry_firm.grid(row=2, column=1, columnspan=2)
                change_entry_model.grid(row=1, column=1, columnspan=2)
                change_combobox.grid(row=3, column=1, columnspan=2)
                change_entry_diagonal.grid(row=4, column=1)
                change_btn_cancel = ttk.Button(self, text='Отмена', command=cancel)
                change_btn = ttk.Button(self, text='Применить', command=change_of_model)
                change_btn_cancel.grid(row=6, column=0, columnspan=2)
                change_btn.grid(row=5, column=0, columnspan=2)
            else:
                mb.showerror("Ошибка", "Нет такого смартфона")


        def cancel():
            self.destroy()
            Change(parent)


        table1_btn = ttk.Button(self, text='Первая Таблица', command=ok1)
        table1_btn.grid(row=1, column=0)
        label_description1 = ttk.Label(self, text='Storage\nCPU\nRAM\nAmount\nModel')
        label_description1.grid(row=2, column=0)
        table2_btn = ttk.Button(self, text='Вторая Таблица', command=ok2)
        table2_btn.grid(row=1, column=1)
        label_description2 = ttk.Label(self, text='Model\nDiagonal\nOS\nManufacturer')
        label_description2.grid(row=2, column=1)
        table3_btn = ttk.Button(self, text='Третья Таблица', command=ok3)
        table3_btn.grid(row=1, column=2)
        label_description3 = ttk.Label(self, text='Manufacturer\nCountry')
        label_description3.grid(row=2, column=2)
        # ok_btn = ttk.Button(self, text='ОК', command=ok)
        # ok_btn.grid(row=15, column=0, columnspan=3)
        entry_code = ttk.Entry(self)
        list_firm = new_list_values('Manufacturer')
        change_entry_firm = ttk.Combobox(self, values=list_firm, state="readonly")
        change_entry_country = ttk.Entry(self)
        list_model = new_list_values('Model')
        change_entry_model = ttk.Combobox(self, values=list_model, state="readonly")
        change_entry_storage = ttk.Entry(self)
        change_entry_diagonal = ttk.Entry(self)
        change_entry_cpu = ttk.Entry(self)
        change_entry_ram = ttk.Entry(self)
        change_entry_amount = ttk.Entry(self)
        change_combobox = ttk.Combobox(self, values=['Android', 'IOS','Blackberry'])
