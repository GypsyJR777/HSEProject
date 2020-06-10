import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

class Delete(tk.Toplevel):

    def __init__(self):
        super().__init__(root)
        self.init_child()


    def init_child(self):
        self.title('Удаление смартфона')
        self.geometry('400x400+400+300')
        self.resizable(False, False)


        def delete_code():
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
