"""
Функция размещает объекты в основном окном программы
Получает: -
Возвращает: -
Автор: Матвеев В.Е., Демидов И.Д., Будин А.М.
"""
import tkinter as tk
import pandas as pd
import bd
from tkinter import messagebox as mb
from filtres import Child_filter
from add import Child_add
from change import Change
from delete import Delete
from graphs import Kowalski_analis
from tkinter import filedialog


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()


    def init_main(self):
        '''
        Функция создает и размещает фреймы с виджетами (таблицу, кнопки) в
        главном окне программы, задает размер, цвета элементов
        Получает: -
        Возвращает: -
        Автор: Будин А.М., Демидов И.Д
        '''
        global mdf, tree
        frame_toolbox = tk.Frame(bd=5, bg="#B0C7E4")
        frame_toolbox.pack(side='top', fill=tk.X)
        frame_table = tk.Frame(bd=5, bg="#B0C7E4")
        tree = frame_table
        # frame with controls
        frame_box2 = tk.Frame(frame_toolbox, bd=5, bg="#B0C7E4")
        frame_box2.pack(side='left', fill=tk.Y, expand=1)
        # photo for button
        photo = tk.PhotoImage(file = r"../img.png")
        photo = photo.subsample(25, 25)
        # elemests of toolbox
        button1_box1 = tk.Button(frame_box2, text=u'Добавить',
        command=self.open_dialog, bg="#5E46E0", fg="white",
        font="TimesNewRoman 16")
        button2_box1 = tk.Button(frame_box2, text=u'Правка',
        command=self.change, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button3_box1 = tk.Button(frame_box2, text=u'Удалить',
        command=self.delete, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button4_box1 = tk.Button(frame_box2, text=u'Экспорт',
        command=self.saved, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button1_box2 = tk.Button(frame_box2, text=u'Анализ',
        command=self.analysis, bg="#5E46E0", fg="white",
        font="TimesNewRoman 16")
        button1_box3 = tk.Button(frame_box2, text=u'Фильтр',
        command=self.sort, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button2_box3 = tk.Button(frame_toolbox, bg="#B0C7E4",
        image=photo, compound=tk.LEFT, relief="flat")
        # pack elemests of toolbox
        button1_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
        button2_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
        button3_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
        button4_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
        button1_box2.pack(side='left', padx=5, ipadx=8, ipady=8)
        button1_box3.pack(side='left', padx=5, ipadx=8, ipady=8)
        button2_box3.pack(side='right')
        try:
            xls = pd.read_pickle("../Data/smartphones.pkl")
        except (FileNotFoundError, EOFError):
            mb.showerror("Ошибка", "Файл smartphones.pkl не удалось открыть")
            xls = pd.DataFrame(columns=["Product Code", "Manufacturer",
            "Country", "Model", "OS", "Storage", "Diagonal",
            "CPU", "RAM", "Amount"])
        mdf = pd.DataFrame(xls)
        bd.Table(frame_table, mdf)


    def open_dialog(self):
        '''
        Функция вызывает класс Child_add для
        создания окна добавления нового элемента таблицы
        Получает: -
        Возвращает: -
        Автор: -
        '''
        global tree
        Child_add(tree)


    def sort(self):
        '''
        Функция вызывает класс Child_filter для сортировки таблицы
        Получает: -
        Возвращает: -
        Автор: -
        '''
        global tree
        Child_filter(tree)


    def change(self):
        '''
        Функция вызывает класс Change для редактирования элемента таблицы
        Получает: -
        Возвращает: -
        Автор: -
        '''
        global tree
        Change(tree)


    def delete(self):
        '''
        Функция вызывает класс Delete для удаления элемента таблицы
        Получает: -
        Возвращает: -
        Автор: -
        '''
        global tree
        Delete(tree)


    def analysis(self):
        '''
        Функция вызвывает класс Kowalski_analis для различных методов анализа
        Получает: -
        Возвращает: -
        Автор: -
        '''
        global tree
        Kowalski_analis(tree)


    def saved(self):
        '''
        Функция сохраняет таблицу в формате Excel
        Получает: -
        Возвращает: -
        Автор: Будин А.М.
        '''
        global mdf
        mdf.to_pickle("../Data/smartphones.pkl")
        #writer = pd.ExcelWriter('../Output/Result.xlsx')
        export_file = filedialog.asksaveasfilename(defaultextension='.xlsx')
        mdf.to_excel(export_file, index = True, header=True)
        #mdf.to_excel(writer, 'smartphones')
        #writer.save()
        print('DataFrame is written successfully to Excel Sheet.')
