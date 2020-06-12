import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import numpy as np
from tkinter import messagebox as mb
import matplotlib as plt
import matplotlib.pyplot as plt


def Table(parent=None, xls=None):
        '''
        Функция создает таблицу и добавляет к ней сколлбары
        Получает: parent-название окна, xls-структура DataFrame
        Возращает: -
        Автор:
        '''
        global counter, tree, df

        df = pd.DataFrame(xls)

        count = len(df)
        headings = ["Product Code", "Manufacturer", "Country", "Model", "OS", "Storage", "Diagonal", "CPU", "RAM", "Amount"]
        tree = ttk.Treeview(root, show="headings", selectmode="browse")
        tree["columns"] = headings
        tree["displaycolumns"] = headings

        for head in headings:
            tree.heading(head, text=head, anchor=tk.CENTER)
            tree.column(head, anchor=tk.CENTER, width=50)

        for i in range(count):
            tree.insert('', i, values=df.iloc[i,:].tolist())

        scrollbar = tk.Scrollbar(tree, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")

        scrollbarx = tk.Scrollbar(tree, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=scrollbarx.set)

        scrollbarx.pack(side="bottom", fill="x")
        tree.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)


def Table_add(firm, country, model, storage, diagonal, cpu, ram, amount, os):
    '''
    Функция добавляет новый кортеж в таблицу
    Получает: firm - название фирмы производителя, country - страна производителя,
        model - модель телефона, storage - объём памяти,
        diagonal - диагональ экрана, cpu - модель процессора,
        ram - объём оперативной памяти, amount - количество (штук),
        os - операционная система
    Возвращает: -
    Автор:
    '''
    global mdf, count
    try:
        counter = mdf.loc[len(mdf)-1]["Product Code"]
    except(KeyError):
        counter=0
    mdf.loc[len(mdf)] = [counter+1, firm, country, str(model), os, int(storage), float(diagonal), cpu, int(ram), int(amount)]
    tree.destroy()
    Table(root, mdf)


def Sorttest_int(sort_parametr, sort_min, sort_max):
    '''
    Функция производит отбор по заданным числовым аргументам
    Получает: sort_parametr - название столбца,
        sort_min - минимальное значение,
        sort_max - максимальное значение
    Возвращает: -
    Автор:
    '''
    global df, mdf
    dtemp = df[df[sort_parametr] >= sort_min]
    df = dtemp[dtemp[sort_parametr] <= sort_max]


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        '''
        Функция создает главное окно программы, задает размер, цвета элементов,
        размещает в нём фреймы с виджетами (таблицу,кнопки)
        Получает: -
        Возвращает: -
        Автор: Будин А.М., Демидов И.Д
        '''
        global mdf
        w, h = root.winfo_screenwidth()-100, root.winfo_screenheight()-100
        root.geometry("%dx%d+0+0" % (w, h))
        frame_toolbox = tk.Frame(root, bd=5, bg="#B0C7E4")
        frame_toolbox.pack(side='top', fill=tk.X)


        #frame with controls
        frame_box2 = tk.Frame(frame_toolbox, bd=5, bg="#B0C7E4")
        frame_box2.pack(side='left', fill=tk.Y, expand=1)

        photo = tk.PhotoImage(file = r"../img.png")
        photo = photo.subsample(25, 25)

        # elemests of toolbox
        button1_box1 = tk.Button(frame_box2, text=u'Добавить', command=self.open_dialog, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button2_box1 = tk.Button(frame_box2, text=u'Правка', command=self.change, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button3_box1 = tk.Button(frame_box2, text=u'Удалить', command=self.delete, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button4_box1 = tk.Button(frame_box2, text=u'Экспорт', command=self.saved, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button1_box2 = tk.Button(frame_box2, text=u'Анализ', command=self.analysis, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button1_box3 = tk.Button(frame_box2, text=u'Фильтр', command=self.sort, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button2_box3 = tk.Button(frame_toolbox, bg="#B0C7E4", image=photo, compound=tk.LEFT, relief="flat")

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
            xls = pd.DataFrame(columns=["Product Code", "Manufacturer", "Country", "Model", "OS", "Storage", "Diagonal", "CPU", "RAM", "Amount"])
        mdf = pd.DataFrame(xls)
        Table(root, mdf)

        root.mainloop()


    def open_dialog(self):
        '''
        Функция вызывает класс Child_add для создания окна добавления нового элемента таблицы
        Получает: -
        Возвращает: -
        Автор:
        '''
        Child_add()

    def sort(self):
        '''
        Функция вызывает класс Child_filter для сортировки таблицы
        Получает: -
        Возвращает: -
        Автор:
        '''
        Child_filter()


    def change(self):
        '''
        Функция вызывает класс Change для редактирования элемента таблицы
        Получает: -
        Возвращает: -
        Автор:
        '''
        Change()


    def delete(self):
        '''
        Функция вызывает класс Delete для удаления элемента таблицы
        Получает: -
        Возвращает: -
        Автор:
        '''
        Delete()


    def analysis(self):
        '''
        Функция вызвывает класс Kowalski_analis для различных методов анализа
        Получает: -
        Возвращает: -
        Автор:
        '''
        Kowalski_analis()


    def saved(self):
        '''
        Функция сохраняет таблицу в формате Excel
        Получает: -
        Возвращает: -
        Автор: Матвеев В.Е.
        '''
        global mdf
        mdf.to_pickle("./Data/smartphones.pkl")
        writer = pd.ExcelWriter('./Output/Result.xlsx')
        mdf.to_excel(writer, 'smartphones')
        writer.save()
        print('DataFrame is written successfully to Excel Sheet.')


class Change(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        '''
        Функция вызывает окно изменения выбранного кортежа
        Получает: -
        Возвращает: -
        Автор: Демидов И.Д
        '''
        global mdf
        self.title('Изменение данных о смартфоне')
        self.geometry('300x100+400+300')
        self.resizable(False, False)
        label_description = ttk.Label(self, text='Код товара для изменения')
        label_description.grid(row=0, column = 0)
        entry_code = ttk.Entry(self)
        entry_code.grid(row=0, column=1, columnspan=2)
        ok_btn = ttk.Button(self, text='OK')
        ok_btn.grid(row=15, column=0, columnspan=3)


#        label_description = ttk.Label(self, text='Операционная система')
#        label_description.grid(row=10, column = 0)

#
#        label_description = ttk.Label(self, text='Производитель')
#        label_description.grid(row=2, column =0)
#
#        label_description = ttk.Label(self, text='Страна')
#        label_description.grid(row=3, column =0)
#
#        label_description = ttk.Label(self, text='Модель')
#        label_description.grid(row=4, column =0)
#
#        label_description = ttk.Label(self, text='Память')
#        label_description.grid(row=5, column =0)
#
#        label_description = ttk.Label(self, text='Диагональ')
#        label_description.grid(row=6, column =0)
#
#        label_description = ttk.Label(self, text='Процессор')
#        label_description.grid(row=7, column =0)
#
#        label_description = ttk.Label(self, text='Оперативная память')
#        label_description.grid(row=8, column =0)
#
#        label_description = ttk.Label(self, text='Количество')
#        label_description.grid(row=9, column =0)
#
#
#        change_entry_firm = ttk.Entry(self)
#        string = mdf.loc[entry_code.get()]["Manufacturer"]
#        change_entry_firm.insert(0, string)
#        change_entry_firm.grid(row=2, column=1, columnspan=2)
#
#        filtr_entry_country = ttk.Entry(self)
#        filtr_entry_country.grid(row=3, column=1, columnspan=2)
#
#        filtr_entry_model = ttk.Entry(self)
#        filtr_entry_model.grid(row=4, column=1, columnspan=2)
#
#        filtr_entry_storage = ttk.Entry(self)
#        filtr_entry_storage.insert(0, )
#        filtr_entry_storage.grid(row=5, column=1)
#
#        filtr_entry_diagonal = ttk.Entry(self)
#        filtr_entry_diagonal.insert(0, 0)
#        filtr_entry_diagonal.grid(row=6, column=1)
#
#        filtr_entry_cpu = ttk.Entry(self)
#        filtr_entry_cpu.grid(row=7, column=1, columnspan=2)
#
#        filtr_entry_ram = ttk.Entry(self)
#        filtr_entry_ram.insert(0, 0)
#        filtr_entry_ram.grid(row=8, column=1)
#
#        filtr_entry_amount = ttk.Entry(self)
#        filtr_entry_amount.insert(0, 0)
#        filtr_entry_amount.grid(row=9, column=1)
#
#        filtr_combobox = ttk.Combobox(self, values=[u'Android',u'IOS', u'BlackBerry'], width=17)
#        filtr_combobox.grid(row=10, column=1, columnspan=2)
#
#        filtr_btn_cancel = ttk.Button(self, text='Отмена')
#        filtr_btn_cancel.grid(row=15, column=0, columnspan=3)
#
#        filtr_btn_filtr = ttk.Button(self, text='Применить')
#        filtr_btn_filtr.grid(row=13, column=0, columnspan=3)
#        filtr_btn_filtr.bind('<Button-1>')
#
#        filtr_btn_filtr_save = ttk.Button(self, text='Сохранить измененения')
#        filtr_btn_filtr_save.grid(row=14, column=0,  columnspan=3)
#        filtr_btn_filtr_save.bind('<Button-1>')
#
#        self.grab_set()
#        self.focus_set()




class Delete(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()


    def init_child(self):
        '''
        Функция вызывает окно удаления кортежа
        Получает: -
        Возвращает: -
        Автор: Демидов И.Д
        '''
        self.title('Удаление смартфона')
        self.geometry('400x400+400+300')
        self.resizable(False, False)


        def delete_code():
            '''
            Функция удаляет выбранный кортеж
            Получает: -
            Возвращает: -
            Автор: Демидов И.Д
            '''
            global mdf
            if(choice.get() == ''):
                mb.showerror("Ошибка", "Введите код продукта")
            else:
                mdf = mdf.drop(np.where(mdf['Product Code'] == int(choice.get()))[0])
                tree.destroy()
                Table(root, mdf)
                self.destroy()


        label_choice = ttk.Label(self, text='Введите код товара, который хотите удалить')
        label_choice.grid(row=0, column=0, columnspan=2)

        choice = ttk.Entry(self)
        choice.grid(row=1, column=0, columnspan=2)

        cancel_but = ttk.Button(self, text='Отмена', command=self.destroy)
        cancel_but.grid(row=2, column=1)

        del_but = ttk.Button(self, text='Удалить', command=delete_code)
        del_but.grid(row=2, column=0)
        del_but.bind('<Button-1>')


class Kowalski_analis(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()


    def init_child(self):
        '''
        Функция вызывает окно выбора диаграммы
        Получает: -
        Возвращает: -
        Автор: Демидов И.Д.
        '''
        global mdf
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
            ax.bar(list(mdf[first_stolb.get()]), list(mdf[second_stolb.get()]))
            ax.set_facecolor('seashell')
            fig.set_facecolor('floralwhite')
            fig.set_figwidth(12)    #  ширина Figure
            fig.set_figheight(6)
            plt.show()

        #Тут можно добавить еще один индекс в квадратные скобки, поля entry оставил на всякий, эта херня считает среднее значение
        #Пробовал вывести в прогу, ошибка, хотя имеет типа DataFrame. Только в консоль работает
        def analis_svod():
            '''
            Функция создает сводчатую таблицу
            Получает: -
            Возвращает: -
            Автор: Матвее В.Е.
            '''
            data_pt = pd.pivot_table(mdf,index=[stolb_1.get(), stolb_2.get()], values=stolb_3.get() )
            print(data_pt)
            writer_svod = pd.ExcelWriter('C:/Result_svod_table.xlsx')
            data_pt.to_excel(writer_svod, 'smartphones1')
            writer_svod.save()
            print('DataFrame is written successfully to Excel Sheet.')
            data_pt.show()



        def analis_rasseivanie():
            '''
            Функция создает диаграмму рассеивания
            Получает: -
            Возвращает: -
            Автор: Матвее В.Е.
            '''
            plt.figure(figsize=(13,10))
            sns.boxplot(x='OS', y='Storage', data=df, notch=False)
            def add_n_obs(df,group_col,y):
                medians_dict = {grp[0]:grp[1][y].median() for grp in df.groupby(group_col)}
                xticklabels = [x.get_text() for x in plt.gca().get_xticklabels()]
                n_obs = df.groupby(group_col)[y].size().values
                for (x, xticklabel), n_ob in zip(enumerate(xticklabels), n_obs):
                    plt.text(x, medians_dict[xticklabel]*1.01, "#obs : "+str(n_ob), horizontalalignment='center', fontdict={'size':14}, color='white')
            add_n_obs(df,group_col='OS',y='Storage')
            plt.show()


        def analis_baz():
            '''
            Функция создает базовый анализ
            Получает: -
            Возвращает: -
            Автор: Матвее В.Е.
            '''
            bazstat = mdf.describe()
            print(bazstat)
            bazstat.show()


        def analis_wix():
            '''
            Функция создает диаграмму Бокса-Вискера
            Получает: -
            Возвращает: -
            Автор: Матвее В.Е.
            '''
            n = pd.unique(df[stolb_1_wix.get()]).tolist()
            b=[]
            for item in n:
                b.append(df[stolb_2_wix.get][df[stolb_1_wix.get()] == item])
            plt.boxplot(b)
            plt.show()


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




# добавление
class Child_add(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        '''
        Функция вызывает окно добавления нового кортежа в таблицу
        Получает: -
        Возвращает: -
        Автор: Матвеев В.Е.
        '''
        self.title('Добавление')
        self.geometry('260x260+400+300')
        self.resizable(False, False)

#self.entry_firm, self.entry_country, self.entry_model, self.entry_storage, self.entry_diagonal, self.entry_cpu, self.entry_ram, self.entry_amount, self.combobox
        def add():
            '''
            Функция добавляет новый кортеж в таблицу
            Получает: -
            Возвращает: -
            Автор:
            '''
            global counter, df
            if(entry_firm.get() != '' and entry_country.get() != '' and
               entry_model.get() != '' and entry_storage.get() != '' and
               entry_diagonal.get() != '' and entry_cpu.get() != '' and
               entry_ram.get() != '' and entry_amount.get() != '' and
               combobox.get() != ''):
                if (entry_ram.get().isdigit() == False and
                    entry_storage.get().isdigit() == False and
                    entry_diagonal.get().isdigit() == False and
                    entry_amount.get().isdigit() == False):
                    mb.showerror("Ошибка", "Должны быть введены числа в полях 'Память', 'Оперативная память' и 'Количество'")
                else:
                    Table_add(entry_firm.get(), entry_country.get(), entry_model.get(), entry_storage.get(), entry_diagonal.get(), entry_cpu.get(), entry_ram.get(), entry_amount.get(), combobox.get())
                    self.destroy()
            else:
                mb.showerror("Ошибка", "Введите данные во все поля")



        label_description = ttk.Label(self, text='Операционная система')
        label_description.grid(row=10, column = 0)

#        label_description = ttk.Label(self, text='Код товара')
#        label_description.grid(row=1, column =0)

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

#        self.entry_cod = ttk.Entry(self)
#        self.entry_cod.grid(row=1, column=1)

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

        combobox = ttk.Combobox(self, values=[u'Android',u'IOS', u'BlackBerry'], width=17)
        combobox.grid(row=10, column=1)

        btn_cancel = ttk.Button(self, text='Отмена', command=self.destroy)
        btn_cancel.grid(row=13, column=0, columnspan=2)

        btn_add = ttk.Button(self, text='Добавить', command=add)
        btn_add.grid(row=12, column=0, columnspan=2)
        btn_add.bind('<Button-1>')

        self.grab_set()
        self.focus_set()


# фильтр
class Child_filter(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child2()


    def init_child2(self):
        '''
        Функция вызывает окно с параметрами для фильтрации
        Получает: -
        Возвращает: -
        Автор: Матвеев В.Е.
        '''
        self.title('Фильтр')
        self.geometry('400x290+1000+500')
        self.resizable(False, False)

#self.entry_firm, self.entry_country, self.entry_model, self.entry_storage, self.entry_diagonal, self.entry_cpu, self.entry_ram, self.entry_amount, self.combobox
        def filtr():
            '''
            Функция производит фильтрацию таблицы по заданным значениям
            Получает: -
            Возвращает: -
            Автор: Матвеев В.Е, Будин А.М.
            '''
            global df, mdf
            df = mdf
            if(filtr_entry_ram.get() != '' and filtr_entry_ram_2.get() != ''):
                Sorttest_int('RAM', int(filtr_entry_ram.get()), int(filtr_entry_ram_2.get()))
            if(filtr_entry_storage.get() != '' and filtr_entry_storage_2.get() != ''):
                Sorttest_int('Storage', int(filtr_entry_storage.get()), int(filtr_entry_storage_2.get()))
            if(filtr_entry_diagonal.get() != '' and filtr_entry_diagonal_2.get() != ''):
                Sorttest_int('Diagonal', float(filtr_entry_diagonal.get()), float(filtr_entry_diagonal_2.get()))
            if(filtr_entry_country.get() != ''):
                df = df[df['Country'] == filtr_entry_country.get()]
            if(filtr_entry_firm.get() != ''):
                df = df[df['Manufacturer'] == filtr_entry_firm.get()]
            if(filtr_entry_model.get() != ''):
                df = df[df['Model'] == filtr_entry_model.get()]
            if(filtr_combobox.get() != ''):
                df = df[df['OS'] == filtr_combobox.get()]
            if(filtr_entry_cpu.get() != ''):
                df = df[df['CPU'] == filtr_entry_cpu.get()]
            if(filtr_entry_amount.get() != '' and filtr_entry_amount_2.get() != ''):
                Sorttest_int('Amount', int(filtr_entry_amount.get()), int(filtr_entry_amount_2.get()))
            print(df)
            tree.destroy()
            Table(root, df)


        def filtr_save():
            '''
            Функция сохраняет изменения произведенные с помощью применения фильтра
            Получает: -
            Возвращает: -
            Автор: Матвеев В.Е.
            '''
            global df
            global mdf
            mdf = df
            tree.destroy()
            Table(root, mdf)


        def filtr_cancel():
            '''
            Функция отменяет изменения произведенные с помощью применения фильтра
            Получает: -
            Возвращает: -
            Автор: Матвеев В.Е.
            '''
            global df
            global mdf
            df = mdf
            tree.destroy()
            Table(root, df)
            self.destroy()


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

        filtr_entry_firm = ttk.Entry(self)
        filtr_entry_firm.grid(row=2, column=1, columnspan=2)

        filtr_entry_country = ttk.Entry(self)
        filtr_entry_country.grid(row=3, column=1, columnspan=2)

        filtr_entry_model = ttk.Entry(self)
        filtr_entry_model.grid(row=4, column=1, columnspan=2)

        filtr_entry_storage = ttk.Entry(self)
        filtr_entry_storage.insert(0, 0)
        filtr_entry_storage.grid(row=5, column=1)

        filtr_entry_diagonal = ttk.Entry(self)
        filtr_entry_diagonal.insert(0, 0)
        filtr_entry_diagonal.grid(row=6, column=1)

        filtr_entry_cpu = ttk.Entry(self)
        filtr_entry_cpu.grid(row=7, column=1, columnspan=2)

        filtr_entry_ram = ttk.Entry(self)
        filtr_entry_ram.insert(0, 0)
        filtr_entry_ram.grid(row=8, column=1)

        filtr_entry_amount = ttk.Entry(self)
        filtr_entry_amount.insert(0, 0)
        filtr_entry_amount.grid(row=9, column=1)

        filtr_entry_storage_2 = ttk.Entry(self)
        filtr_entry_storage_2.insert(0, 2048)
        filtr_entry_storage_2.grid(row=5, column=2)

        filtr_entry_diagonal_2 = ttk.Entry(self)
        filtr_entry_diagonal_2.insert(0, 20)
        filtr_entry_diagonal_2.grid(row=6, column=2)

        filtr_entry_ram_2 = ttk.Entry(self)
        filtr_entry_ram_2.insert(0, 256)
        filtr_entry_ram_2.grid(row=8, column=2)

        filtr_entry_amount_2 = ttk.Entry(self, textvariable=1000000)
        filtr_entry_amount_2.insert(0, 1000000)
        filtr_entry_amount_2.grid(row=9, column=2)

        filtr_combobox = ttk.Combobox(self, values=[u'Android',u'IOS', u'BlackBerry'], width=17)
        filtr_combobox.grid(row=10, column=1, columnspan=2)

        filtr_btn_cancel = ttk.Button(self, text='Отмена', command=filtr_cancel)
        filtr_btn_cancel.grid(row=15, column=0, columnspan=3)

        filtr_btn_filtr = ttk.Button(self, text='Применить', command=filtr)
        filtr_btn_filtr.grid(row=13, column=0, columnspan=3)
        filtr_btn_filtr.bind('<Button-1>')

        filtr_btn_filtr_save = ttk.Button(self, text='Сохранить измененения', command=filtr_save)
        filtr_btn_filtr_save.grid(row=14, column=0,  columnspan=3)
        filtr_btn_filtr_save.bind('<Button-1>')

        self.grab_set()
        self.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    root["bg"] = "#B0C7E4"
    root.state("zoomed")
    app = Main(root)
    app.pack()
    root.title("Программа")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.resizable(False, False)