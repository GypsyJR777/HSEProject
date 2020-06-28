"""
Функция вызывает окно фильтрации
Получает: -
Возвращает: -
Автор: Матвеев В.Е., Демидов И.Д., Будин А.М.
"""

import tkinter as tk
import tkinter.ttk as ttk
import os, sys
sys.path.insert(0, os.path.abspath("../Library"))
import bd
sys.path.insert(0, os.path.abspath("../Scripts"))
import app as m
import pandas as pd


class Child_filter(tk.Toplevel):
    def __init__(self, parent_):
        '''
        Функция вызывает окно с параметрами для фильтрации
        Получает: -
        Возвращает: -
        Автор: Матвеев В.Е., Демидов И.Д., Будин А.М.
        '''
        super().__init__()
        global df, parent, list_firm, xls1, xls2, xls3
        df = m.mdf
        xls1=m.mxls1
        xls2=m.mxls2
        xls3=m.mxls3
        parent = parent_
        self.title('Фильтры')
        self.geometry('420x300+400+300')
        self.resizable(False, False)


        def new_list_models():
            '''
            Функция создает список полей выбора в комбобоксе Models
            Получает: -
            Возвращает: new_list - новый список полей
            Автор: Демидов И.Д.
            '''
            global df, xls3
            df = m.mdf
            xls3=m.mxls3
            if (filtr_combo_firm.get() == ''):
                new_list = pd.unique(xls3['Model']).tolist()
                return new_list
            else:
                xls3 = xls3[xls3['Manufacturer'] == filtr_combo_firm.get()]
                new_list = pd.unique(xls3["Model"]).tolist()
                return new_list


        def new_list_manufacturer():
            '''
            Функция создает список полей выбора в комбобоксе Manufacturer
            Получает: -
            Возвращает: new_list - новый список полей
            Автор: Демидов И.Д.
            '''
            global df, xls1
            df = m.mdf
            xls1 = m.mxls1
            if (filtr_combo_country.get() == ''):
                new_list = pd.unique(xls1['Manufacturer']).tolist()
                return new_list
            else:
                xls1 = xls1[xls1['Country'] == filtr_combo_country.get()]
                new_list = pd.unique(xls1["Manufacturer"]).tolist()
                return new_list


        def new_list_os():
            '''
            Функция создает список полей выбора в комбобоксе OS
            Получает: -
            Возвращает: new_list - новый список полей
            Автор: Демидов И.Д.
            '''
            global df, xls3
            df = m.mdf
            xls3 = m.mxls3
            if (filtr_combo_firm.get() == ''):
                new_list = pd.unique(xls3['OS']).tolist()
                return new_list
            else:
                xls3 = xls3[xls3['Manufacturer'] == filtr_combo_firm.get()]
                new_list = pd.unique(xls3["OS"]).tolist()
                return new_list


        def models():
            '''
            Функция обновляет данные в комбобоксе Models
            Получает: -
            Возвращает: -
            Автор:Демидов И.Д.
            '''
            filtr_combo_model["values"] = new_list_models()


        def manufacturer():
            '''
            Функция обновляет данные в комбобоксе Manufacturer
            Получает: -
            Возвращает: -
            Автор: Демидов И.Д.
            '''
            filtr_combo_firm["values"] = new_list_manufacturer()


        def os():
            '''
            Функция обновляет данные в комбобоксе OS
            Получает: -
            Возвращает: -
            Автор: Демидов И.Д.
            '''
            filtr_combo_os["values"] = new_list_os()


        def new_list_values(stolb_name):
            '''
            функция создает новые список уникальных значений после применения
            фильтра
            Получает: stolb_name - название столбца
            Возвращает: new_list - обновленный список уникальных значений
            Автор: Будин А.М., Матвеев В.Е.
            '''
            global df
            df = pd.merge(pd.merge(xls2, xls3, on=('Model')).drop_duplicates(subset=['Product Code']), xls1, on=('Manufacturer'))
            new_list = pd.unique(df[stolb_name]).tolist()
            return new_list


        def Sorttest_int(sort_parametr, sort_min, sort_max):
            '''
            Функция производит отбор по заданным числовым аргументам
            Получает: sort_parametr - название столбца,
            sort_min - минимальное значение,
            sort_max - максимальное значение
            Возвращает: -
            Автор: Будин А.М.
            '''
            global df, xls1, xls2, xls3

            index2 = ['Storage','RAM','Amount']

            if sort_parametr in index2:
                dtemp2 = xls2[xls2[sort_parametr] >= sort_min]
                xls2 = dtemp2[dtemp2[sort_parametr] <= sort_max]
            else:
                dtemp3 = xls3[xls3[sort_parametr] >= sort_min]
                xls3 = dtemp3[dtemp3[sort_parametr] <= sort_max]


        def filtr_cancel():
            '''
            Функция отменяет изменения произведенные с помощью применения
            фильтра
            Получает: -
            Возвращает: -
            Автор: Демидов И.Д.
            '''
            global parent
            xls1 = m.mxls1
            xls2 = m.mxls2
            xls3 = m.mxls3
            for widget in parent_.winfo_children():
                widget.destroy()
            bd.Table(parent, xls1, xls2, xls3)
            self.destroy()


        def filtr():
            '''
            Функция производит фильтрацию таблицы по заданным значениям
            Получает: -
            Возвращает: -
            Автор: Матвеев В.Е, Будин А.М.
            '''
            global df, parent, xls1, xls2, xls3
            df = m.mdf
            xls1=m.mxls1
            xls2=m.mxls2
            xls3=m.mxls3
            if (filtr_entry_ram.get() != '' and filtr_entry_ram_2.get() != ''):
                Sorttest_int('RAM', int(filtr_entry_ram.get()),
                             int(filtr_entry_ram_2.get()))
            if (filtr_entry_storage.get() != ''
                and filtr_entry_storage_2.get() != ''):
                Sorttest_int('Storage', int(filtr_entry_storage.get()),
                             int(filtr_entry_storage_2.get()))
            if (filtr_entry_diagonal.get() != ''
                and filtr_entry_diagonal_2.get() != ''):
                b=[]
                c=[]
                diagseries = xls3[xls3['Diagonal'] <= float(filtr_entry_diagonal_2.get())]
                diagseries = diagseries[diagseries['Diagonal'] >= float(filtr_entry_diagonal.get())]
                b.append(diagseries['Model'])
                for item in b:
                    for items in item:
                        c.append(items)
                xls2=xls2[xls2['Model'].isin(c)]

            if (filtr_combo_country.get() !=''):
                xls1 = xls1.loc[xls1['Country'] == filtr_combo_country.get()]
                xls3 = xls3[xls3['Manufacturer'].isin(xls1['Manufacturer'].tolist())]
                xls2 = xls2[xls2['Model'].isin(xls3['Model'].tolist())]

            if (filtr_combo_firm.get() != ''):
                xls3 = xls3.loc[xls3['Manufacturer'] == filtr_combo_firm.get()]
                xls2 = xls2[xls2['Model'].isin(xls3['Model'].tolist())]


            if (filtr_combo_model.get() != ''):
                xls2 = xls2[xls2['Model'] == filtr_combo_model.get()]

            if (filtr_combo_os.get() != ''):
                xls3 = xls3.loc[xls3['OS'] == filtr_combo_os.get()]
                xls2 = xls2[xls2['Model'].isin(xls3['Model'].tolist())]

            if (filtr_combo_cpu.get() != ''):
                xls2 = xls2[xls2['CPU'] == filtr_combo_cpu.get()]
            if (filtr_entry_amount.get() != '' and filtr_entry_amount_2.get() != ''):
                Sorttest_int('Amount', int(filtr_entry_amount.get()),
                             int(filtr_entry_amount_2.get()))
            for widget in parent.winfo_children():
                widget.destroy()
            bd.Table(parent, xls1, xls2, xls3)



        def filtr_save():
            '''
            Функция сохраняет изменения произведенные с помощью применения
            фильтра
            Получает: -
            Возвращает: -
            Автор: Демидов И.Д.
            '''
            global df, parent, xls1, xls2, xls3
            m.mdf = df
            m.mxls2 = xls2
            m.mxls1 = xls1
            m.mxls3 = xls3
            for widget in parent.winfo_children():
                widget.destroy()
            bd.Table(parent, m.mxls1, m.mxls2, m.mxls3)
            self.destroy()


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
        filtr_btn_cancel = ttk.Button(self, text='Отмена', command=filtr_cancel)
        filtr_btn_cancel.grid(row=15, column=1, columnspan=3)
        filtr_btn_filtr = ttk.Button(self, text='Применить', command=filtr)
        filtr_btn_filtr.grid(row=13, column=1, columnspan=3)
        filtr_btn_filtr.bind('<Button-1>')
        filtr_btn_filtr_save = ttk.Button(self, text='Сохранить измененения',
                                          command=filtr_save)
        filtr_btn_filtr_save.grid(row=14, column=1, columnspan=3)
        filtr_btn_filtr_save.bind('<Button-1>')
        self.grab_set()
        self.focus_set()
