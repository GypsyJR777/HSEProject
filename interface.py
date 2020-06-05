import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd



def Table(parent=None, xls=None):
        global counter, tree, df

        df = pd.DataFrame(xls)
        df_col = df.columns.values

        tree = ttk.Treeview(root)
        tree["columns"]=(df_col)
        counter = len(df)
        index_col=False
        #generating for loop to create columns and give heading to them through df_col var.
        for x in range(10):
            tree.column(x, width=50)
            tree.heading(x, text=df_col[x])
        #generating for loop to print values of dataframe in treeview column.
        for i in range(counter):
            tree.insert('', i, values=df.iloc[i,:].tolist())
        tree.pack(expand=tk.YES, fill=tk.BOTH)


def Table_add(firm, country, model, storage, diagonal, cpu, ram, amount, os):
    global df, counter
    mdf.loc[counter] = [counter+1, firm, country, model, os, int(storage), diagonal, cpu, int(ram), amount]
    tree.destroy()
    Table(root, mdf)


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        global mdf
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (w, h))
        frame_toolbox = tk.Frame(root, bd=5)
        frame_toolbox.pack(side='top', fill=tk.X)

        # 1-st frame with controls
        frame_box1 = tk.LabelFrame(frame_toolbox, text='Редактирование', bd=5)
        frame_box1.pack(side='left', fill=tk.Y, expand=1)

        # 2-nd frame with controls
        frame_box2 = tk.LabelFrame(frame_toolbox, text='Анализ', bd=5)
        frame_box2.pack(side='left', fill=tk.Y, expand=1)

        # 3-rd frame with controls
        frame_box3 = tk.LabelFrame(frame_toolbox, text='Фильтр', bd=5)
        frame_box3.pack(side='left', fill=tk.Y, expand=1)

        # frame for the Table
        frame_table = tk.Frame(root, bd=2)
        frame_table.pack(side='bottom')


        # elemests of 1-st box
        frame_box1_view = tk.Frame(frame_box1, bd=5)
        frame_box1_buttons = tk.Frame(frame_box1, bd=5)
        frame_box1_top = tk.Frame(frame_box1_buttons, bd=5)
        frame_box1_bottom = tk.Frame(frame_box1_buttons, bd=5)
        text_box = tk.Text(frame_box1_view, width=40, height=10)
        button1_box1=tk.Button(frame_box1_top, text=u'Добавить', command=self.open_dialog)
        button2_box1=tk.Button(frame_box1_top, text=u'Правка')
        button3_box1=tk.Button(frame_box1_bottom, text=u'Удалить')
        button4_box1=tk.Button(frame_box1_bottom, text=u'Экспорт')


        # pack elemests of 1-st box
        frame_box1_view.pack(side='top')
        frame_box1_buttons.pack(side='top')
        frame_box1_top.pack(side='top')
        frame_box1_bottom.pack(side='top')
        text_box.pack(side='top')
        button1_box1.pack(side='left')
        button2_box1.pack(side='left')
        button3_box1.pack(side='left')
        button4_box1.pack(side='left')

        # elemests of 2-nd box
        frame_box2_view = tk.Frame(frame_box2, bd=5)
        frame_box2_buttons = tk.Frame(frame_box2, bd=5)
        text_box = tk.Text(frame_box2_view, width=40, height=10)
        button1_box2=tk.Button(frame_box2_buttons, text=u'Анализ')
        button2_box2=tk.Button(frame_box2_buttons, text=u'Экспорт')


        # pack elemests of 2-nd box
        frame_box2_view.pack(side='top')
        frame_box2_buttons.pack(side='top')
        button1_box2.pack(side='left')
        button2_box2.pack(side='left')
        text_box.pack(side='top')

        # elemests of 3-rd box
        frame_box3_view = tk.Frame(frame_box3, bd=5)
        frame_box3_buttons = tk.Frame(frame_box3, bd=5)
        text_box = tk.Text(frame_box3_view, width=40, height=10)
        button1_box3=tk.Button(frame_box3_buttons, text=u'Первая кнопка', command=self.sorttest)
        button2_box3=tk.Button(frame_box3_buttons, text=u'Вторая кнопка', command=self.sorttest2)


        # pack elemests of 3-rd box
        frame_box3_view.pack(side='top')
        frame_box3_buttons.pack(side='top')
        text_box.pack(side='top')
        button1_box3.pack(side='left')
        button2_box3.pack(side='left')


        xls = pd.read_excel("./Data/Smartphones.xlsx")
        mdf = pd.DataFrame(xls)
        table = Table(root, mdf)


        root.mainloop()


    def open_dialog(self):
        Child()

    def sorttest(self):
       # frame_table.delete
        global df
        ramsize = 8
        df = mdf[mdf['RAM'] == ramsize]
        tree.destroy()
        table = Table(root, df)


    def sorttest2(self):
       # frame_table.delete
        global df
        tree.destroy()
        stor = 256
        df = mdf[mdf['Storage'] == stor]
        table = Table(root, df)



class Child(tk.Toplevel):

    def __init__(self):
        super().__init__(root)
        self.init_child()


    def init_child(self):
        self.title('Добавление')
        self.geometry('260x260+400+300')
        self.resizable(False, False)

#self.entry_firm, self.entry_country, self.entry_model, self.entry_storage, self.entry_diagonal, self.entry_cpu, self.entry_ram, self.entry_amount, self.combobox
        def add():
            global counter, df
            if(entry_firm!='' and entry_country!='' and
               entry_model !='' and entry_storage !='' and
               entry_diagonal !='' and entry_cpu!='' and
               entry_ram !='' and entry_amount !='' and
               combobox!=''):
                print(entry_firm)
                Table_add(entry_firm.get(), entry_country.get(), entry_model.get(), entry_storage.get(), entry_diagonal.get(), entry_cpu.get(), entry_ram.get(), entry_amount.get(), combobox.get())



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


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Программа")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.resizable(False, False)
