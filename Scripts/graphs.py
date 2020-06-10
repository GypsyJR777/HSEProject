import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

class Kowalski_analis(tk.Toplevel):

    def __init__(self):
        super().__init__(root)
        self.init_child()


    def init_child(self):
        global mdf
        self.title('Анализ от Ковальского')
        self.geometry('600x400+400+300')
        self.resizable(False, False)
        self.focus_force()


        def analis_stolb():
            fig, ax = plt.subplots()
            ax.bar(list(mdf[first_stolb.get()]), list(mdf[second_stolb.get()]))
            ax.set_facecolor('seashell')
            fig.set_facecolor('floralwhite')
            fig.set_figwidth(12)    #  ширина Figure
            fig.set_figheight(6)
            plt.show()

        #Тут можно добавить еще один индекс в квадратные скобки, поля entry оставил на всякий, эта херня считает среднее значение
        #Пробовал вывести в прогу, ошибка, хотя имеет типа DataFrame. Только в консоль работает
        def analis_svod():
            data_pt = pd.pivot_table(mdf,index=[stolb_1.get(), stolb_2.get()], values=stolb_3.get() )
            print(data_pt)
            writer_svod = pd.ExcelWriter('C:/Result_svod_table.xlsx')
            data_pt.to_excel(writer_svod, 'smartphones1')
            writer_svod.save()
            print('DataFrame is written successfully to Excel Sheet.')




        def analis_rasseivanie():
            plot_df = mdf.groupby([stolb_1_rass.get(), stolb_2_rass.get()]).size().reset_index(name='amount')
            print(plot_df)
            plot_df.plot.scatter(x=stolb_1_rass.get(), y=stolb_2_rass.get(), s= 50*plot_df['amount']*2, c='amount', cmap='inferno')



        def analis_baz():
            bazstat = mdf.describe()
            print(bazstat)
            bazstat.show()


        def analis_wix():
            wix=plt.boxplot(x=stolb_1_wix.get(), y=stolb_2_wix.get(), data=mdf, notch=False)
            wix.show()


        label_analis = ttk.Label(self, text='Выберете анализ: ')
        label_analis.grid(row=0, column=0)

        first_stolb = ttk.Entry(self)
        first_stolb.grid(row=1, column=1)

        second_stolb = ttk.Entry(self)
        second_stolb.grid(row=1, column=2)

#Поля сводной таблицы
        stolb_1 = ttk.Entry(self)
        stolb_1.grid(row=3, column=1)

        stolb_2 = ttk.Entry(self)
        stolb_2.grid(row=3, column=2)

        stolb_3 = ttk.Entry(self)
        stolb_3.grid(row=3, column=3)

#Поля диаграммы рассеивания
        stolb_1_rass = ttk.Entry(self)
        stolb_1_rass.grid(row=2, column=1)

        stolb_2_rass = ttk.Entry(self)
        stolb_2_rass.grid(row=2, column=2)

        stolb_3_rass = ttk.Entry(self)
        stolb_3_rass.grid(row=2, column=3)


        base_stolb = ttk.Button(self, text='Столбчатая Диаграмма', command=analis_stolb)
        base_stolb.grid(row=1, column=0)

        base_svod = ttk.Button(self, text='Сводная таблица', command=analis_svod)
        base_svod.grid(row=3, column=0)

        base_svod = ttk.Button(self, text='Диаграмма рассеивания', command=analis_rasseivanie)
        base_svod.grid(row=2, column=0)

#Поля базовой статистики
        baz_stat = ttk.Button(self, text='Базовая статистка', command=analis_baz, width = 90)
        baz_stat.grid(row=4, column=0, columnspan=4)

#Поля диаграммы Бокса-Вискера
        wix_stat = ttk.Button(self, text='Бокса-Вискера', command=analis_wix)
        wix_stat.grid(row=5, column=0)
        stolb_1_wix = ttk.Entry(self)
        stolb_1_wix.grid(row=5, column=1)
        stolb_2_wix = ttk.Entry(self)
        stolb_2_wix.grid(row=5, column=2)
