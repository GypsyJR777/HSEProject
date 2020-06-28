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
from tkinter import filedialog


class Child_report(tk.Toplevel):
    def __init__(self, parent_):
        '''
        Функция вызывает окно с параметрами для фильтрации
        Получает: -
        Возвращает: -
        Автор: Матвеев В.Е., Демидов И.Д., Будин А.М.
        '''
        super().__init__()
        global df, parent, list_firm, col_code, col_manufacturer, col_country, col_model, col_os, col_storage, col_diagolal, col_cpu, col_ram, col_amount
        df = m.mdf
        parent = parent_
        self.title('Фильтры')
        self.geometry('420x350+400+300')
        self.resizable(False, False)


        def new_list_models():
            '''
            Функция создает список полей выбора в комбобоксе Models
            Получает: -
            Возвращает: new_list - новый список полей
            Автор: Демидов И.Д.
            '''
            global df
            df = m.mdf
            if (filtr_combo_firm.get() == ''):
                new_list = pd.unique(df['Model']).tolist()
                return new_list
            else:
                df = df[df['Manufacturer'] == filtr_combo_firm.get()]
                new_list = pd.unique(df["Model"]).tolist()
                return new_list


        def new_list_manufacturer():
            '''
            Функция создает список полей выбора в комбобоксе Manufacturer
            Получает: -
            Возвращает: new_list - новый список полей
            Автор: Демидов И.Д.
            '''
            global df
            df = m.mdf
            if (filtr_combo_country.get() == ''):
                new_list = pd.unique(df['Manufacturer']).tolist()
                return new_list
            else:
                df = df[df['Country'] == filtr_combo_country.get()]
                new_list = pd.unique(df["Manufacturer"]).tolist()
                return new_list


        def new_list_os():
            '''
            Функция создает список полей выбора в комбобоксе OS
            Получает: -
            Возвращает: new_list - новый список полей
            Автор: Демидов И.Д.
            '''
            global df
            df = m.mdf
            if (filtr_combo_firm.get() == ''):
                new_list = pd.unique(df['OS']).tolist()
                return new_list
            else:
                df = df[df['Manufacturer'] == filtr_combo_firm.get()]
                new_list = pd.unique(df["OS"]).tolist()
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
            global df
            dtemp = df[df[sort_parametr] >= sort_min]
            df = dtemp[dtemp[sort_parametr] <= sort_max]


        def cancel():
            '''
            Функция отменяет изменения произведенные с помощью применения
            фильтра
            Получает: -
            Возвращает: -
            Автор: Демидов И.Д.
            '''
            self.destroy()


        def filtr():
            '''
            Функция производит фильтрацию таблицы по заданным значениям
            Получает: -
            Возвращает: -
            Автор: Матвеев В.Е, Будин А.М.
            '''
            global df, parent, xls1, xls2, xls3, list_col, col_code, col_manufacturer, col_country, col_model, col_os, col_storage, col_diagolal, col_cpu, col_ram, col_amount
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

            list_col = []
            if col_code.get() == 1:
                list_col.append("Product Code")
            if col_manufacturer.get() == 1:
                list_col.append("Manufacturer")
            if col_country.get() == 1:
                list_col.append("Country")
            if col_model.get() == 1:
                list_col.append("Model")
            if col_os.get() == 1:
                list_col.append("OS")
            if col_storage.get() == 1:
                list_col.append("Storage")
            if col_diagolal.get() == 1:
                list_col.append("Diagonal")
            if col_cpu.get() == 1:
                list_col.append("CPU")
            if col_ram.get() == 1:
                list_col.append("RAM")
            if col_amount.get() == 1:
                list_col.append("Amount")

        def Table_report(parent=None, xls1=None, xls2=None, xls3=None, list_of_columns=None):
            '''
            Функция создает таблицу и добавляет к ней сколлбары
            Получает: parent-название окна, xls-структура DataFrame,
            list_of_columns-список колонок для вывода
            Возращает: -
            Автор: Демидов И.Д, Матвеев В.Е.
            '''
            df = pd.merge(pd.merge(xls2, xls3, on=('Model')).drop_duplicates(subset=['Product Code']), xls1, on=('Manufacturer'))
            df = df[list_of_columns]
            count = len(df)
            #df = df[["Product Code", "Manufacturer", "Country", "Model", "OS", "Storage", "Diagonal", "CPU", "RAM", "Amount"]]
            headings = df.columns.tolist()
            tree = ttk.Treeview(parent, show="headings", selectmode="browse")
            tree["columns"] = headings
            tree["displaycolumns"] = headings
            for head in headings:
                tree.heading(head, text=head, anchor=tk.CENTER)
                tree.column(head, anchor=tk.CENTER, width=50)
                tree.heading(head, text=head, command=lambda head_=head: treeview_sort_column(tree, head_, False))
            for i in range(count):
                tree.insert('', i, values=df.iloc[i, :].tolist())
            scrollbar = tk.Scrollbar(tree, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)
            scrollbar.pack(side="right", fill="y")
            scrollbarx = tk.Scrollbar(tree, orient="horizontal", command=tree.xview)
            tree.configure(xscrollcommand=scrollbarx.set)
            scrollbarx.pack(side="bottom", fill="x")
            tree.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
            m.mdf = m.mdf.reset_index(drop=True)
            parent.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)

        def create():
            '''
            Функция создает отчет и выводит его на экран
            Получает: -
            Возвращает: -
            Автор: Будин А.М
            '''
            global df, parent, window, xls1, xls2, xls3, list_col
            m.mdf = df
            window = tk.Toplevel()
            window.geometry('710x410+400+300')
            frame_report = tk.Frame(window)
            frame_report.pack(side='top', fill=tk.BOTH)
            Table_report(frame_report, xls1, xls2, xls3, list_col)
            frame_btns = tk.Frame(window)
            frame_btns.pack(side='top', fill=tk.X, ipadx=8, ipady=15)
            frame_btns_in= tk.Frame(frame_btns)
            frame_btns.pack(side='left', fill=tk.Y, expand=1)
            btn_cancel = ttk.Button(frame_btns, text='Отмена', command=cancel_report)
            btn_cancel.pack(side=tk.LEFT, padx=5, ipadx=8, ipady=8)
            btn_save_txt = ttk.Button(frame_btns, text='Сохранить TXT', command=save_txt)
            btn_save_txt.pack(side=tk.LEFT, padx=5, ipadx=8, ipady=8)
            window.grab_set()
            window.focus_set()

        def create_report():
            '''
            Функция обратывает нажатие на кнопку создания
            Получает: -
            Возвращает: -
            Автор: Будин А.М.
            '''
            filtr()
            create()

        def cancel_report():
            '''
            Функция обрабатывает нажатие на кнопку отмены
            Получает: -
            Возвращает: -
            Автор: Будин А.М.
            '''
            window.destroy()

        def save_txt():
            '''
            Функция сохраняет текстовый отчет
            Получает: -
            Возвращает: -
            Автор: Матвеев В.Е
            '''
            global window, xls1, xls2, xls3, list_col
            sdf = pd.merge(pd.merge(xls2, xls3, on=('Model')).drop_duplicates(subset=['Product Code']), xls1, on=('Manufacturer'))
            sdf = sdf[list_of_columns_col]
            export_file_path = filedialog.asksaveasfilename(defaultextension='.txt')
            tfile = open(export_file_path, 'w')
            tfile.write(sdf.to_string(index=False))
            tfile.close()
            window.destroy()


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
        col_code = tk.IntVar()
        col_code.set(1)
        col_manufacturer = tk.IntVar()
        col_manufacturer.set(1)
        col_country = tk.IntVar()
        col_country.set(1)
        col_model = tk.IntVar()
        col_model.set(1)
        col_os = tk.IntVar()
        col_os.set(1)
        col_storage = tk.IntVar()
        col_storage.set(1)
        col_diagolal = tk.IntVar()
        col_diagolal.set(1)
        col_cpu = tk.IntVar()
        col_cpu.set(1)
        col_ram = tk.IntVar()
        col_ram.set(1)
        col_amount = tk.IntVar()
        col_amount.set(1)
        code_check = tk.Checkbutton(self, text='Product Code', variable=col_code, onvalue=1, offvalue=0)
        code_check.grid(row=11, column=0, sticky='w', ipadx=20)
        manufacturer_check = tk.Checkbutton(self, text='Manufacturer', variable=col_manufacturer, onvalue=1, offvalue=0)
        manufacturer_check.grid(row=11, column=1, sticky='w', ipadx=20)
        country_check = tk.Checkbutton(self, text='Country', variable=col_country, onvalue=1, offvalue=0)
        country_check.grid(row=11, column=2, sticky='w', ipadx=20)
        model_check = tk.Checkbutton(self, text='Model', variable=col_model, onvalue=1, offvalue=0)
        model_check.grid(row=12, column=0, sticky='w', ipadx=20)
        os_check = tk.Checkbutton(self, text='OS', variable=col_os, onvalue=1, offvalue=0)
        os_check.grid(row=12, column=1, sticky='w', ipadx=20)
        storage_check = tk.Checkbutton(self, text='Storage', variable=col_storage, onvalue=1, offvalue=0)
        storage_check.grid(row=12, column=2, sticky='w', ipadx=20)
        diagonal_check = tk.Checkbutton(self, text='Diagonal', variable=col_diagolal, onvalue=1, offvalue=0)
        diagonal_check.grid(row=13, column=0, sticky='w', ipadx=20)
        cpu_check = tk.Checkbutton(self, text='CPU', variable=col_cpu, onvalue=1, offvalue=0)
        cpu_check.grid(row=13, column=1, sticky='w', ipadx=20)
        ram_check = tk.Checkbutton(self, text='RAM', variable=col_ram, onvalue=1, offvalue=0)
        ram_check.grid(row=13, column=2, sticky='w', ipadx=20)
        amount_check = tk.Checkbutton(self, text='Amount', variable=col_amount, onvalue=1, offvalue=0)
        amount_check.grid(row=14, column=0, sticky='w', ipadx=20)
        filtr_btn_cancel = ttk.Button(self, text='Отмена', command=cancel)
        filtr_btn_cancel.grid(row=15, column=0, columnspan=2)
        filtr_btn_filtr = ttk.Button(self, text='Создать', command=create_report)
        filtr_btn_filtr.grid(row=15, column=1, columnspan=2)
        filtr_btn_filtr.bind('<Button-1>')
        self.grab_set()
        self.focus_set()
