import tkinter as tk
import tkinter.ttk as ttk
from bd import Table


def Sorttest_int(sort_parametr, sort_min, sort_max):
    global df, mdf
    dtemp =df[df[sort_parametr] >= sort_min]
    df=dtemp[dtemp[sort_parametr] <= sort_max]


class Child_filter(tk.Toplevel):
    def __init__(self, mdf_, parent_):
        super().__init__()
#        self.init_child()


#    def init_child(self, mdf, parent):
        global df, parent, mdf
        mdf = mdf_
        df = mdf
        parent = parent_

        self.title('Добавление')
        self.geometry('400x400+400+300')
        self.resizable(False, False)
        def filtr_save():
            global mdf, df, parent
            mdf=df
            for widget in parent.winfo_children():
                widget.destroy()
            Table(parent, mdf)
            self.destroy()
            
            
        def filtr_cancel():
            global mdd, df, parent
            df=mdf
            for widget in parent_.winfo_children():
                widget.destroy()
            Table(parent, df)
            self.destroy()
            print(mdf)
        
        
        def filtr():
            global df, parent
            if(filtr_entry_ram.get() !='' and filtr_entry_ram_2.get() !=''):
                Sorttest_int('RAM', int(filtr_entry_ram.get()), int(filtr_entry_ram_2.get()))
            if(filtr_entry_storage.get() !='' and filtr_entry_storage_2.get() !=''):
                Sorttest_int('Storage', int(filtr_entry_storage.get()), int(filtr_entry_storage_2.get()))
            if(filtr_entry_diagonal.get() !='' and filtr_entry_diagonal_2.get() !=''):
                Sorttest_int('Diagonal', float(filtr_entry_diagonal.get()), float(filtr_entry_diagonal_2.get()))
            if(filtr_entry_country.get() !=''):
                df = df[df['Country'] == filtr_entry_country.get()]
            if(filtr_entry_firm.get() !=''):
                df = df[df['Manufacturer'] == filtr_entry_firm.get()]
            if(filtr_entry_model.get() !=''):
                df = df[df['Model'] == filtr_entry_model.get()]
            if(filtr_combobox.get() !=''):
                df = df[df['OS'] == filtr_combobox.get()]
            if(filtr_entry_cpu.get() !=''):
                df = df[df['CPU'] == filtr_entry_cpu.get()]
            if(filtr_entry_amount.get() !='' and filtr_entry_amount_2.get() !=''):
                Sorttest_int('Amount', int(filtr_entry_amount.get()), int(filtr_entry_amount_2.get()))
            print(df)
            for widget in parent.winfo_children():
                widget.destroy()
            Table(parent, df)


        label_description = ttk.Label(self, text='Операционная система')
        label_description.grid(row=1, column =0)

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
        self.mainloop()