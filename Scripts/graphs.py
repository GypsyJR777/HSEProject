"""
Функция вызывает окно выбора диаграммы
Получает: -
Возвращает: -
Автор: Матвеев В.Е., Демидов И.Д., Будин А.М.
"""
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
from tkinter import filedialog
import app as m

class Kowalski_analis(tk.Toplevel):
    def __init__(self, parent_):
        '''
        Функция вызывает окно выбора диаграммы
        Получает: -
        Возвращает: -
        Автор: Демидов И.Д., Матвеев В.Е.
        '''
        super().__init__(parent_)
        global parent
        parent = parent_
        self.title('Анализ от Ковальского')
        self.geometry('600x400+400+300')
        self.resizable(False, False)
        self.focus_force()


        def analis_stolb():
            '''
            Функция создает столбчатую диаграмму
            Получает: -
            Возвращает: -
            Автор: Демидов И.Д.
            '''
            fig, ax = plt.subplots()
            ax.bar(list(m.mdf[first_stolb.get()]),
            list(m.mdf[second_stolb.get()]))
            ax.set_facecolor('seashell')
            fig.set_facecolor('floralwhite')
            fig.set_figwidth(12)    #  ширина Figure
            fig.set_figheight(6)
            plt.show()


        def analis_svod():
            '''
            Функция создает сводную таблицу
            Получает: -
            Возвращает: -
            Автор: Матвеев В.Е.
            '''
            data_pt = pd.pivot_table(m.mdf,index=[stolb_1.get(), stolb_2.get()],
            values=stolb_3.get())
            data_pt.columns = [t[0] if t[0] else t[1] for t in data_pt.columns]
            print(data_pt)
            export_file = filedialog.asksaveasfilename(defaultextension='.xlsx')
            data_pt.to_excel(export_file)


        def analis_rasseivanie():
            '''
            Функция создает диаграмму рассеивания
            Получает: -
            Возвращает: -
            Автор: Матвеев В.Е.
            '''
            if stolb_3_rass.get()!='':
                plot_df = m.mdf.groupby([stolb_1_rass.get(), stolb_2_rass.get(),
                stolb_3_rass.get()]).size().reset_index(name='amount')
                plot_df.plot.scatter(x=stolb_1_rass.get(), y=stolb_2_rass.get(),
                s=plot_df[stolb_3_rass.get()], c=stolb_3_rass.get(),
                cmap='inferno')
            else:
                plot_df = m.mdf.groupby([stolb_1_rass.get(), stolb_2_rass.get()]).size().reset_index(name='amount')
                plot_df.plot.scatter(x=stolb_1_rass.get(), y=stolb_2_rass.get(),
                                     s=100*plot_df['amount'], c='amount',
                                     cmap='inferno')
            print(plot_df)
            plt.show()


        def analis_baz():
            '''
            Функция создает базовый анализ
            Получает: -            Возвращает: -
            Автор: Матвеев В.Е.
            '''
            bazstat = m.mdf.describe()
            print(bazstat)
            export_file = filedialog.asksaveasfilename(defaultextension='.xlsx')
            bazstat.to_excel(export_file, index = True, header=True)


        def analis_wix():
            '''
            Функция создает диаграмму Бокса-Вискера
            Получает: -
            Возвращает: -
            Автор: Матвеев В.Е.
            '''
            n = pd.unique(m.mdf[stolb_1_wix.get()]).tolist()
            b=[]
            for item in n:
                b.append(m.mdf[stolb_2_wix.get()][m.mdf[stolb_1_wix.get()] == item])
            plt.boxplot(b)
            plt.show()


        def analis_gis():
            '''
            Функция создает гистодиаграмму
            Получает: -
            Возвращает: -
            Автор: Матвеев В.Е.
            '''
            gis = m.mdf.groupby(stolb_1_gis.get()).size().reset_index(name=stolb_2_gis.get())
            plt.figure(figsize=(16,10), dpi= 80)
            plt.bar(gis[stolb_1_gis.get()], gis[stolb_2_gis.get()], width=.5)
            for i, val in enumerate(gis[stolb_2_gis.get()].values):
                plt.text(i, val, float(val), horizontalalignment='center',
                verticalalignment='bottom',
                fontdict={'fontweight':500, 'size':12})
            plt.gca().set_xticklabels(gis[stolb_1_gis.get()], rotation=60,
            horizontalalignment= 'right')
            plt.ylim(0, 45)
            plt.show()


        label_analis = ttk.Label(self, text='Выберете анализ: ')
        label_analis.grid(row=0, column=0)
        first_stolb = ttk.Entry(self)
        first_stolb.grid(row=1, column=1)
        second_stolb = ttk.Entry(self)
        second_stolb.grid(row=1, column=2)
#Поля сводной таблицы
        stolb_1 = ttk.Combobox(self, values=['Product Code','Manufacturer','Country','Model','OS', 'Storage', 'Diagonal', 'CPU', 'RAM', 'Amount'], width=17)
        stolb_1.grid(row=3, column=1)
        stolb_2 = ttk.Combobox(self, values=['Product Code','Manufacturer','Country','Model','OS', 'Storage', 'Diagonal', 'CPU', 'RAM', 'Amount'], width=17)
        stolb_2.grid(row=3, column=2)
        stolb_3 = ttk.Combobox(self, values=['Storage', 'Diagonal', 'RAM', 'Amount'], width=17)
        stolb_3.grid(row=3, column=3)
#Поля диаграммы рассеивания
        stolb_1_rass = ttk.Combobox(self, values=['Storage', 'Diagonal', 'RAM', 'Amount'], width=17)
        stolb_1_rass.grid(row=2, column=1)
        stolb_2_rass = ttk.Combobox(self, values=['Storage', 'Diagonal', 'RAM', 'Amount'], width=17)
        stolb_2_rass.grid(row=2, column=2)
        stolb_3_rass = ttk.Combobox(self, values=['Storage', 'Diagonal', 'RAM', 'Amount'], width=17)
        stolb_3_rass.grid(row=2, column=3)
        base_stolb = ttk.Button(self, text='Столбчатая Диаграмма', command=analis_stolb)
        base_stolb.grid(row=1, column=0)
        base_svod = ttk.Button(self, text='Сводная таблица', command=analis_svod)
        base_svod.grid(row=3, column=0)
        base_svod = ttk.Button(self, text='Диаграмма рассеивания', command=analis_rasseivanie)
        base_svod.grid(row=2, column=0)
#Поля базовой статистики
        baz_stat = ttk.Button(self, text='Базовая статистка',
        command=analis_baz, width = 90)
        baz_stat.grid(row=4, column=0, columnspan=4)
#Поля диаграммы Бокса-Вискера
        wix_stat = ttk.Button(self, text='Бокса-Вискера', command=analis_wix)
        wix_stat.grid(row=5, column=0)
        stolb_1_wix = ttk.Entry(self)
        stolb_1_wix.grid(row=5, column=1)
        stolb_2_wix = ttk.Entry(self)
        stolb_2_wix.grid(row=5, column=2)
#Поля гистограммы
        gis_stat = ttk.Button(self, text='Гистограмма', command=analis_gis)
        gis_stat.grid(row=6, column=0)
        stolb_1_gis = ttk.Entry(self)
        stolb_1_gis.grid(row=6, column=1)
        stolb_2_gis = ttk.Entry(self)
        stolb_2_gis.grid(row=6, column=2)
