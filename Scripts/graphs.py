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
import numpy as np
from tkinter import messagebox as mb

class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 300   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.grid(column=2,row=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()


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


        def analis_stolb(event):
            '''
            Функция создает столбчатую диаграмму
            Получает: -
            Возвращает: -
            Автор: Демидов И.Д.
            '''
            fig, ax = plt.subplots()
            lststolb = [str(item) for item in list(m.mdf[first_stolb.get()])]
            ax.bar(lststolb, list(m.mdf[second_stolb.get()]))
            fig.set_figwidth(12)    #  ширина Figure
            fig.set_figheight(6)
            ax.tick_params(labelrotation = 60)
            plt.show()


        # def stolb_info(event):
        #     mb.showinfo("Описание","Показывает график, представленный прямоугольными зонами, высоты которых пропорциональны величинам, которые они отображают.")



        def analis_svod(event):
            '''
            Функция создает сводчатую таблицу
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


        # def svod_info(event):
        #     mb.showinfo("Описание","Резюмирует данные, представленные в исходной таблице, показывает среднее значение по конечному столбцу.")



        def analis_rasseivanie(event):
            '''
            Функция создает диаграмму рассеяния
            Получает: -
            Возвращает: -
            Автор: Матвеев В.Е.
            '''
            if stolb_3_rass.get()!='Кол-во повторений':
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


        # def rasseivanie_info(event):
        #     mb.showinfo("Описание","Показывает взаимосвязь между двумя или тремя переменными, цвет и размер точек отображают значение третьей переменную. Если введены 2 параметра, вместо третьего используется количество повторений.")


        def analis_baz(event):
            '''
            Функция создает базовый анализ
            Получает: -            Возвращает: -
            Автор: Матвеев В.Е.
            '''
            bazstat = m.mdf.describe()
            print(bazstat)
            export_file = filedialog.asksaveasfilename(defaultextension='.xlsx')
            bazstat.to_excel(export_file, index = True, header=True)


        # def baz_info(event):
        #     mb.showinfo("Описание","Сохраняет таблицу с описательной статистикой(среднее, стандартное отклонение, количество наблюдений, минимальное, максимальное и квартили) числовых столбцов.")


        def analis_wix(event):
            '''
            Функция создает диаграмму Бокса-Вискера
            Получает: -
            Возвращает: -
            Автор: Матвеев В.Е.
            '''
            n = pd.unique(m.mdf[stolb_1_wix.get()]).tolist()
            b=[]
            a=[]
            for i in range(len(n)):
                a.append(i+1)
            for item in n:
                b.append(m.mdf[stolb_2_wix.get()][m.mdf[stolb_1_wix.get()] == item])
            plt.boxplot(b)
            plt.xticks(a, n, rotation=75)
            plt.show()

        # def wix_info(event):
        #     mb.showinfo("Описание","Используются в описательной статистике и позволяют быстро исследовать несколько наборов данных в графическом виде. Показывает верхние и нижние границы, квартили и медиану.")


        def analis_gis(event):
            '''
            Функция создает гистодиаграмму
            Получает: -
            Возвращает: -
            Автор: Матвеев В.Е.
            '''
            dfg = m.mdf[[stolb_2_gis.get(), stolb_1_gis.get()]].groupby(stolb_1_gis.get()).apply(lambda x: x.mean())
            dfg.sort_values(stolb_2_gis.get(), inplace=True)
            dfg.reset_index(inplace=True)
            import matplotlib.patches as patches
            fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
            ax.vlines(x=dfg.index, ymin=0, ymax=dfg[stolb_2_gis.get()], color='firebrick', alpha=0.7, linewidth=20)
            for i, cty in enumerate(dfg[stolb_2_gis.get()]):
                ax.text(i, cty+0.5, round(cty, 1), horizontalalignment='center')

            plt.xticks(dfg.index, dfg[stolb_1_gis.get()].str.upper(), rotation=60, horizontalalignment='right', fontsize=12)

            p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
            p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
            fig.add_artist(p1)
            fig.add_artist(p2)
            plt.show()


        # def gis_info(event):
        #     mb.showinfo("Описание","Упорядоченная гистограмма эффективно передает порядок ранжирования элементов. Выводит столбцы по возрастанию.")

        label_analis = ttk.Label(self, text='Выберите анализ: ')
        label_analis.grid(row=0, column=0)
        # label_info = ttk.Label(self, text='Чтобы посмотреть описание, нажмите на кнопку правой кнопкой мыши')
        # label_info.grid(row=7, column=0, rowspan=3, columnspan=3)
        first_stolb = ttk.Combobox(self, values=['Product Code','Manufacturer','Country','Model','OS', 'Storage', 'Diagonal', 'CPU', 'RAM', 'Amount'], width=17)
        first_stolb.grid(row=1, column=1)
        second_stolb = ttk.Combobox(self, values=['Storage', 'Diagonal', 'RAM', 'Amount'], width=17)
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
        base_stolb = ttk.Button(self, text='Столбчатая Диаграмма')
        base_stolb.grid(row=1, column=0)
        base_stolb.bind('<Button-1>', analis_stolb)
        # base_stolb.bind('<Button-3>', stolb_info)
        base_stolb_ttp = CreateToolTip(base_stolb, 'Показывает график, представленный прямоугольными зонами, высоты которых пропорциональны величинам, которые они отображают.')
        base_svod = ttk.Button(self, text='Сводная таблица')
        base_svod.grid(row=3, column=0)
        base_svod.bind('<Button-1>', analis_svod)
        # base_svod.bind('<Button-3>', svod_info)
        base_svod_ttp = CreateToolTip(base_svod, 'Резюмирует данные, представленные в исходной таблице, показывает среднее значение по конечному столбцу.')
        base_ras = ttk.Button(self, text='Диаграмма рассеяния')
        base_ras.grid(row=2, column=0)
        base_ras.bind('<Button-1>', analis_rasseivanie)
        # base_ras.bind('<Button-3>', rasseivanie_info)
        base_ras_ttp = CreateToolTip(base_ras, 'Показывает взаимосвязь между двумя или тремя переменными, цвет и размер точек отображают значение третьей переменную. Если введены 2 параметра, вместо третьего используется количество повторений.')

#Поля базовой статистики
        baz_stat = ttk.Button(self, text='Базовая статистка', width = 90)
        baz_stat.bind('<Button-1>', analis_baz)
        # baz_stat.bind('<Button-3>', baz_info)
        baz_stat.grid(row=4, column=0, columnspan=4)
        baz_stat_ttp = CreateToolTip(baz_stat, 'Сохраняет таблицу с описательной статистикой(среднее, стандартное отклонение, количество наблюдений, минимальное, максимальное и квартили) числовых столбцов.')
#Поля диаграммы Бокса-Вискера
        wix_stat = ttk.Button(self, text='Бокса-Вискера')
        wix_stat.grid(row=5, column=0)
        wix_stat_ttp = CreateToolTip(wix_stat, 'Используются в описательной статистике и позволяют быстро исследовать несколько наборов данных в графическом виде. Показывает верхние и нижние границы, квартили и медиану.')
        wix_stat.bind('<Button-1>', analis_wix)
        # wix_stat.bind('<Button-3>', wix_info)
        stolb_1_wix = ttk.Combobox(self, values=['Product Code','Manufacturer','Country','Model','OS', 'Storage', 'Diagonal', 'CPU', 'RAM', 'Amount'], width=17)
        stolb_1_wix.grid(row=5, column=1)
        stolb_2_wix = ttk.Combobox(self, values=['Storage', 'Diagonal', 'RAM', 'Amount'], width=17)
        stolb_2_wix.grid(row=5, column=2)
#Поля гистограммы
        gis_stat = ttk.Button(self, text='Гистограмма')
        gis_stat.grid(row=6, column=0)
        gis_stat.bind('<Button-1>', analis_gis)
        # gis_stat.bind('<Button-3>', gis_info)
        gis_stat_ttp = CreateToolTip(gis_stat, 'Упорядоченная гистограмма эффективно передает порядок ранжирования элементов. Выводит столбцы по возрастанию.')
        stolb_1_gis = ttk.Combobox(self, values=['Manufacturer', 'Country', 'Model', 'OS', 'CPU'], width=17)
        stolb_1_gis.grid(row=6, column=1)
        stolb_2_gis = ttk.Combobox(self, values=['Storage', 'Diagonal', 'RAM', 'Amount'], width=17)
        stolb_2_gis.grid(row=6, column=2)
