import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

window = tk.Tk()
window.title("Добро пожаловать в приложение PythonRu")



def Table(parent=None):
        xls = pd.read_excel('./Data/Smartphones.xlsx')
        df = pd.DataFrame(xls)
        df_col = df.columns.values
        tree = ttk.Treeview(root)
        tree["columns"]=(df_col)
        counter = len(df)
        index_col=False
        #generating for loop to create columns and give heading to them through df_col var.
        for x in range(9):
            tree.column(x, width=50)
            tree.heading(x, text=df_col[x])
        #generating for loop to print values of dataframe in treeview column.
        for i in range(counter):
            tree.insert('', i, values=df.iloc[i,:].tolist())
        tree.pack(expand=tk.YES, fill=tk.BOTH)


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (w, h))
        frame_toolbox = tk.Frame(root, bd=5)
        frame_toolbox.pack(side='top', fill=tk.X)

        # 1-st frame with controls
        frame_box1 = tk.Frame(frame_toolbox, bd=5)
        frame_box1.pack(side='left', fill=tk.Y, expand=1)

        # 2-nd frame with controls
        frame_box2 = tk.Frame(frame_toolbox, bd=5)
        frame_box2.pack(side='left', fill=tk.Y, expand=1)

        # 3-rd frame with controls
        frame_box3 = tk.Frame(frame_toolbox, bd=5)
        frame_box3.pack(side='left', fill=tk.Y, expand=1)

        # frame for the Table
        frame_table = tk.Frame(root, bd=2)
        frame_table.pack(side='bottom')


        # elemests of 1-st box
        frame_box1_top = tk.Frame(frame_box1, bd=5)
        frame_box1_bottom = tk.Frame(frame_box1, bd=5)
        button1_box1=tk.Button(frame_box1_top, text=u'Добавить', command=self.open_dialog)
        button2_box1=tk.Button(frame_box1_top, text=u'Правка')
        button3_box1=tk.Button(frame_box1_bottom, text=u'Удалить')
        button4_box1=tk.Button(frame_box1_bottom, text=u'Экспорт')


        # pack elemests of 1-st box
        frame_box1_top.pack(side='top')
        frame_box1_bottom.pack(side='top')
        button1_box1.pack(side='left')
        button2_box1.pack(side='left')
        button3_box1.pack(side='left')
        button4_box1.pack(side='left')

        # elemests of 2-nd box
        button1_box2=tk.Button(frame_box2, text=u'Анализ')
        button2_box2=tk.Button(frame_box2, text=u'Экспорт')

        # pack elemests of 2-nd box
        button1_box2.pack(side='left')
        button2_box2.pack(side='left')

        # elemests of 3-rd box
        button1_box3=tk.Button(frame_box3, text=u'Первая кнопка')
        button2_box3=tk.Button(frame_box3, text=u'Вторая кнопка')

        # pack elemests of 3-rd box
        button1_box3.pack(side='left')
        button2_box3.pack(side='left')


        table = Table(root)


        root.mainloop()


    def open_dialog(self):
        Child()



class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Добавление нового смартфона')
        self.geometry('670x480+400+300')
        self.resizable(False, False)

        label_description_os = ttk.Label(self, text='Операционная система')
        label_description_os.place(x=510,y=60)

        label_description_ram = ttk.Label(self, text='RAM')
        label_description_ram.place(x=410,y=60)

        self.entry_firm = ttk.Entry(self)
        self.entry_firm.place(x=10, y=100)

        self.entry_country = ttk.Entry(self)
        self.entry_country.place(x=60, y=100)

        self.entry_code = ttk.Entry(self)
        self.entry_code.place(x=110, y=100)

        self.entry_model = ttk.Entry(self)
        self.entry_model.place(x=210, y=100)

        self.entry_storage = ttk.Entry(self)
        self.entry_storage.place(x=260, y=100)

        self.entry_diagonal = ttk.Entry(self)
        self.entry_diagonal.place(x=310, y=100)

        self.entry_cpu = ttk.Entry(self)
        self.entry_cpu.place(x=360, y=100)

        self.combobox_ram = ttk.Combobox(self, values=[u'1',u'2', u'3', u'4', 
                                                       u'6', u'8', u'12'])
        self.combobox_ram.place(x=410, y=100)

        self.entry_amount = ttk.Entry(self)
        self.entry_amount.place(x=460, y=100)

        self.combobox_os = ttk.Combobox(self, values=[u'Android',u'IOS', 
                                                      u'BlackBerry'])
        self.combobox_os.place(x=510, y=100)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=570, y=440)

        btn_add = ttk.Button(self, text='Добавить')
        btn_add.place(x=170, y=170)
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

