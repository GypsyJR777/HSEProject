"""
Функция вызывает окно добавления нового кортежа в таблицу
Получает: -
Возвращает: -
Автор: Матвеев В.Е., Демидов И.Д., Будин А.М.
"""
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import numpy as np
import os, sys
sys.path.insert(0, os.path.abspath("../Library"))
import bd
sys.path.insert(0, os.path.abspath("../Scripts"))
import app as m
from tkinter import messagebox as mb
pd.options.mode.chained_assignment = None  # default='warn'

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
        self.geometry('350x260+400+300')
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
                # elif (entry_country.get() != np.array(m.mxls1[m.mxls1['Manufacturer'] == entry_firm.get()])[0][1]):
                #     mb.showerror("Ошибка", "Введенная страна не соответствует введенному производителю")
                # elif ((np.array(m.mxls3[m.mxls3['Model'] == entry_model.get()])[0][1] != entry_diagonal.get()) and (np.array(m.mxls3[m.mxls3['Model'] == entry_model.get()])[0][2] != combobox.get()) and (np.array(m.mxls3[m.mxls3['Model'] == entry_model.get()])[0][3] != entry_firm.get())):
                #     mb.showerror("Ошибка", "Введенный данные(диагональ, OS или производитель) не соответствует введенной модели")
                else:
                    print("yeah1")
                    try:
                        if (entry_country.get() != np.array(m.mxls1[m.mxls1['Manufacturer'] == entry_firm.get()])[0][1]):
                            mb.showerror("Ошибка", "Введенная страна не соответствует введенному производителю")
                        elif ((np.array(m.mxls3[m.mxls3['Model'] == entry_model.get()])[0][1] != entry_diagonal.get()) or (np.array(m.mxls3[m.mxls3['Model'] == entry_model.get()])[0][2] != combobox.get()) or (np.array(m.mxls3[m.mxls3['Model'] == entry_model.get()])[0][3] != entry_firm.get())):
                            mb.showerror("Ошибка", "Введенные данные (диагональ, OS или производитель) не соответствует введенной модели")
                    except(IndexError):
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
                counter = df.loc[len(df)-1]["Product Code"]
            except(KeyError):
                counter = 0

            m.mdf = m.mdf[["Product Code", "Manufacturer", "Country", "Model", "OS", "Storage", "Diagonal", "CPU", "RAM", "Amount"]]
            m.mdf.loc[len(m.mdf)] = [len(m.mdf) + 1, firm, country, str(model), os, int(storage), float(diagonal), cpu, int(ram), int(amount)]

            for widget in parent.winfo_children():
                widget.destroy()
            m.mxls1 = m.mdf[['Manufacturer', 'Country']]
            m.mxls1 = m.mxls1.drop_duplicates(subset='Manufacturer')
            m.mxls2 = m.mdf[["Product Code", "Storage", "CPU", "RAM", "Amount", "Model"]]
            m.mxls2 = m.mxls2.drop_duplicates(subset='Product Code')
            m.mxls3 = m.mdf[["Model", "Diagonal", "OS", "Manufacturer"]]
            m.mxls3 = m.mxls3.drop_duplicates(subset='Model')
            print (m.mdf)
            bd.Table(parent, m.mxls1, m.mxls2, m.mxls3)


        def new_list_country():
            '''
            Функция создает список полей выбора в комбобоксе Country, исходя из выбора
                производителя
            Получает: -
            Возвращает: new_list - новый список полей
            Автор: Будин А.М.
            '''
            global df
            if (entry_firm.get() == ''):
                new_list = pd.unique(df['Country']).tolist()
                return new_list
            else:
                df = df[df['Manufacturer'] == entry_firm.get()]
                new_list = pd.unique(df["Country"]).tolist()
                new_list.sort()
                return new_list


        def country():
            '''
            Функция обновляет данные в комбобоксе Coutry и выводит первое
                значение в списке в поле
            Получает: -
            Возвращает: -
            Автор: Будин А.М.
            '''
            entry_country["values"] = new_list_country()


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
        list_firm = new_list_values('Manufacturer')
        entry_firm = ttk.Combobox(self, values=list_firm, width=30)
        entry_firm.grid(row=2, column=1, columnspan=2)
        list_country = new_list_values('Country')
        entry_country = ttk.Combobox(self, values=list_country, width=30, postcommand=country)
        entry_country.grid(row=3, column=1, columnspan=2)
        entry_model = ttk.Entry(self, width=33)
        entry_model.grid(row=4, column=1, columnspan=2)
        list_storage = new_list_values('Storage')
        list_storage = [int(elem) for elem in list_storage]
        list_storage.sort()
        entry_storage = ttk.Combobox(self, values=list_storage, width=30)
        entry_storage.grid(row=5, column=1, columnspan=2)
        entry_diagonal = ttk.Entry(self, width=33)
        entry_diagonal.grid(row=6, column=1, columnspan=2)
        list_cpu = new_list_values('CPU')
        list_cpu.sort()
        entry_cpu = ttk.Combobox(self, values=list_cpu, width=30)
        entry_cpu.grid(row=7, column=1, columnspan=2)
        list_ram = new_list_values('RAM')
        list_ram = [int(elem) for elem in list_ram]
        list_ram.sort()
        entry_ram = ttk.Combobox(self, values=list_ram, width=30)
        entry_ram.grid(row=8, column=1, columnspan=2)
        entry_amount = tk.Spinbox(self, from_=0, to=1000000,  width=32)
        entry_amount.grid(row=9, column=1, columnspan=2)
        list_os = new_list_values('OS')
        combobox = ttk.Combobox(self, values=list_os, width=30)
        combobox.grid(row=10, column=1, columnspan=2)
        btn_cancel = ttk.Button(self, text='Отмена', command=self.destroy)
        btn_cancel.grid(row=13, column=0, columnspan=3)
        btn_add = ttk.Button(self, text='Добавить', command=add)
        btn_add.grid(row=12, column=0, columnspan=3)
        btn_add.bind('<Button-1>')
        self.grab_set()
        self.focus_set()
