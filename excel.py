import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

window = tk.Tk()
window.title("Добро пожаловать в приложение PythonRu")


menu = tk.Menu(window)
new_item = tk.Menu(menu, tearoff=0)
new_item.add_command(label='Новый')
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)
window.mainloop()



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


        '''toolbar1 = tk.Frame(bg='blue', bd=3)
        toolbar1.pack(side=tk.RIGHT, fill=tk.Y)
        toolbar2 = tk.Frame(bg='blue', bd=3)
        toolbar2.pack(side=tk.BOTTOM, fill=tk.X)
        xls = pd.read_excel('./Data/Smartphones.xlsx')
        df = pd.DataFrame(xls)
        df_col = df.columns.values
        df_col = df.columns.values
        tree = ttk.Treeview(root)
        tree["columns"]=(df_col)
        counter = len(df)
        rowLabels = df.index.tolist()
        df.reset_index(drop=True, inplace=True)
        #generating for loop to create columns and give heading to them through df_col var.
        for x in range(9):
            tree.column(x)
            tree.heading(x, text=df_col[x])
        #generating for loop to print values of dataframe in treeview column.
        for i in range(counter):
            tree.insert('', i, text=rowLabels[i], values=df.iloc[i,:].tolist())
        tree.pack(expand=tk.YES, fill=tk.BOTH)
        btn_open_dialog = tk.Button(toolbar1, text='Добавить', command=self.open_dialog, bg='YELLOW', bd=0, compound = tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)'''
        '''self.tree = ttk.Treeview(self, columns = ('cod', 'proizv', 'strana', 'codtov', 'model', 'oc', 'vnutrpam', 'diagonal', 'proc', 'operpam', 'kolvo'), height=40, show='headings')

        self.tree.column('cod', width=60, anchor=tk.CENTER)
        self.tree.column('proizv', width=60, anchor=tk.CENTER)
        self.tree.column('strana', width=60, anchor=tk.CENTER)
        self.tree.column('codtov', width=60, anchor=tk.CENTER)
        self.tree.column('model', width=60, anchor=tk.CENTER)
        self.tree.column('oc', width=60, anchor=tk.CENTER)
        self.tree.column('vnutrpam', width=60, anchor=tk.CENTER)
        self.tree.column('diagonal', width=60, anchor=tk.CENTER)
        self.tree.column('proc', width=60, anchor=tk.CENTER)
        self.tree.column('operpam', width=60, anchor=tk.CENTER)
        self.tree.column('kolvo', width=60, anchor=tk.CENTER)

        self.tree.heading('cod', text='код производителя')
        self.tree.heading('proizv', text='производитель')
        self.tree.heading('strana', text='страна')
        self.tree.heading('codtov', text='код товара')
        self.tree.heading('model', text='модель')
        self.tree.heading('oc', text='ОС')
        self.tree.heading('vnutrpam', text='внутренняя память')
        self.tree.heading('diagonal', text='диагональ экрана')
        self.tree.heading('proc', text='процессор')
        self.tree.heading('operpam', text='оперативаная память')
        self.tree.heading('kolvo', text='кол-во')

        self.tree.pack()
        '''



    def open_dialog(self):
        Child()



class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Дочернее окно')
        self.geometry('720x480+400+300')
        self.resizable(False, False)

        label_description = ttk.Label(self, text='Операционная система')
        label_description.place(x=560,y=40)

        self.entry_cod = ttk.Entry(self)
        self.entry_cod.place(x=10, y=100)

        self.entry_proizv = ttk.Entry(self)
        self.entry_proizv.place(x=60, y=100)

        self.entry_strana = ttk.Entry(self)
        self.entry_strana.place(x=110, y=100)

        self.entry_codtov = ttk.Entry(self)
        self.entry_codtov.place(x=160, y=100)

        self.entry_model = ttk.Entry(self)
        self.entry_model.place(x=260, y=100)

        self.entry_vnutrpam = ttk.Entry(self)
        self.entry_vnutrpam.place(x=310, y=100)

        self.entry_diagonal = ttk.Entry(self)
        self.entry_diagonal.place(x=360, y=100)

        self.entry_proc = ttk.Entry(self)
        self.entry_proc.place(x=410, y=100)

        self.entry_operpam = ttk.Entry(self)
        self.entry_operpam.place(x=460, y=100)

        self.entry_kolvo = ttk.Entry(self)
        self.entry_kolvo.place(x=510, y=100)

        self.combobox = ttk.Combobox(self, values=[u'Android',u'IOS', u'BlackBerry'])
        self.combobox.place(x=560, y=100)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=620, y=440)

        btn_add = ttk.Button(self, text='Добавить')
        btn_add.place(x=220, y=170)
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
    root.mainloop()
