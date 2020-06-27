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




        label_description = ttk.Label(self, text='Операционная система')
        label_description.grid(row=4, column=0)
        label_description = ttk.Label(self, text='Производитель')
        label_description.grid(row=3, column=0)
        label_description = ttk.Label(self, text='Страна')
        label_description.grid(row=2, column=0)
        label_description = ttk.Label(self, text='Модель')
        label_description.grid(row=5, column=0)
        label_description = ttk.Label(self, text='Память')
        label_description.grid(row=8, column=0)
        label_description = ttk.Label(self, text='Диагональ')
        label_description.grid(row=7, column=0)
        label_description = ttk.Label(self, text='Процессор')
        label_description.grid(row=6, column=0)
        label_description = ttk.Label(self, text='Оперативная память')
        label_description.grid(row=9, column=0)
        label_description = ttk.Label(self, text='Количество')
        label_description.grid(row=10, column=0)
        list_country = new_list_values('Country')
        filtr_combo_country = ttk.Combobox(self, values=list_country, width=38)
        filtr_combo_country.grid(row=2, column=1, columnspan=2)
        list_firm = new_list_values('Manufacturer')
        filtr_combo_firm = ttk.Combobox(self, values=list_firm, width=38, postcommand=manufacturer)
        filtr_combo_firm.grid(row=3, column=1, columnspan=2)
        list_os = new_list_values('OS')
        filtr_combo_os = ttk.Combobox(self, values=list_os, width=38, postcommand=os)
        filtr_combo_os.grid(row=4, column=1, columnspan=2)
        list_cpu = new_list_values('CPU')
        filtr_combo_cpu = ttk.Combobox(self, values=list_cpu, width=38)
        filtr_combo_cpu.grid(row=6, column=1, columnspan=2)
        list_model = new_list_models()
        filtr_combo_model = ttk.Combobox(self, values=list_model, width=38, postcommand=models)
        filtr_combo_model.grid(row=5, column=1, columnspan=2)
        list_diagonal = new_list_values('Diagonal')
        list_diagonal.sort()
        filtr_entry_diagonal = ttk.Combobox(self, values=list_diagonal, width=17)
        filtr_entry_diagonal.insert(0, 0)
        filtr_entry_diagonal.grid(row=7, column=1)
        list_storage = new_list_values('Storage')
        list_storage.sort()
        filtr_entry_storage = ttk.Combobox(self, values=list_storage, width=17)
        filtr_entry_storage.insert(0, 0)
        filtr_entry_storage.grid(row=8, column=1)
        list_ram = new_list_values('RAM')
        list_ram.sort()
        filtr_entry_ram = ttk.Combobox(self, values=list_ram, width=17)
        filtr_entry_ram.insert(0, 0)
        filtr_entry_ram.grid(row=9, column=1)
        filtr_entry_amount = ttk.Entry(self, width=20)
        filtr_entry_amount.insert(0, 0)
        filtr_entry_amount.grid(row=10, column=1)
        filtr_entry_storage_2 = ttk.Combobox(self, values=list_storage, width=17)
        filtr_entry_storage_2.insert(0, 2048)
        filtr_entry_storage_2.grid(row=8, column=2)
        filtr_entry_diagonal_2 = ttk.Combobox(self, values=list_diagonal, width=17)
        filtr_entry_diagonal_2.insert(0, 20)
        filtr_entry_diagonal_2.grid(row=7, column=2)
        filtr_entry_ram_2 = ttk.Combobox(self, values=list_ram, width=17)
        filtr_entry_ram_2.insert(0, 256)
        filtr_entry_ram_2.grid(row=9, column=2)
        filtr_entry_amount_2 = ttk.Entry(self, width=20)
        filtr_entry_amount_2.insert(0, 1000000)
        filtr_entry_amount_2.grid(row=10, column=2)
        code_check = tk.Checkbutton(self, text='Product Code')
        code_check.grid(row=11, column=0, sticky='w', ipadx=20)
        manufacturer_check = tk.Checkbutton(self, text='Manufacturer')
        manufacturer_check.grid(row=11, column=1, sticky='w', ipadx=20)
        country_check = tk.Checkbutton(self, text='Country')
        country_check.grid(row=11, column=2, sticky='w', ipadx=20)
        model_check = tk.Checkbutton(self, text='Model')
        model_check.grid(row=12, column=0, sticky='w', ipadx=20)
        os_check = tk.Checkbutton(self, text='OS')
        os_check.grid(row=12, column=1, sticky='w', ipadx=20)
        storage_check = tk.Checkbutton(self, text='Storage')
        storage_check.grid(row=12, column=2, sticky='w', ipadx=20)
        diagonal_check = tk.Checkbutton(self, text='Diagonal')
        diagonal_check.grid(row=13, column=0, sticky='w', ipadx=20)
        cpu_check = tk.Checkbutton(self, text='CPU')
        cpu_check.grid(row=13, column=1, sticky='w', ipadx=20)
        ram_check = tk.Checkbutton(self, text='RAM')
        ram_check.grid(row=13, column=2, sticky='w', ipadx=20)
        amount_check = tk.Checkbutton(self, text='Amount')
        amount_check.grid(row=14, column=0, sticky='w', ipadx=20)
        filtr_btn_cancel = ttk.Button(self, text='Отмена', command=filtr_cancel)
        filtr_btn_cancel.grid(row=15, column=0, columnspan=2)
        filtr_btn_filtr = ttk.Button(self, text='Создать', command=filtr)
        filtr_btn_filtr.grid(row=15, column=1, columnspan=2)
        filtr_btn_filtr.bind('<Button-1>')
        self.grab_set()
        self.focus_set()
