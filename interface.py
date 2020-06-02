# from tkinter import * #
#
# window = Tk()
# window.title("База Данных")
# window.geometry('900x540+300+200')
# window.resizable(False, False)
#
# class Table(Frame):
#     def __init__(self, parent=None, headings=tuple(), rows=tuple()):
#         super().__init__(parent)
#
#         table = Treeview(self, show="headings", selectmode="browse")
#         table["columns"]=headings
#         table["displaycolumns"]=headings
#
#         for head in headings:
#             table.heading(head, text=head, anchor=CENTER)
#             table.column(head, anchor=CENTER)
#
#         for row in rows:
#             table.insert('', END, values=tuple(row))
#
#         scrolltable = Scrollbar(self, command=table.yview)
#         table.configure(yscrollcommand=scrolltable.set)
#         scrolltable.pack(side=RIGHT, fill=Y)
#         table.pack(expand=YES, fill=BOTH)
#
# class menu(object):
#     """docstring for menu."""
#
#     def __init__(self, arg):
#         super(menu, self).__init__()
#         self.arg = arg
#
         # menu = Menu(window)  # меню (toolbar)
         # new_item = Menu(menu, tearoff=0)
         # new_item.add_command(label='Новый')  # новый элемент меню
         # menu.add_cascade(label='Файл', menu=new_item)  # новый элемент внутри каскада меню
         # window.config(menu=menu)
#
# frame_menu = Frame(window, width=900, height=100, bg='yellow')
# frame_menu.grid(column=0,row=0)
#
# frame_bd = Frame(window, width=900, height=100, bg='blue')
# frame_bd.grid(column=0,row=1)
#
# window.mainloop()




import tkinter as tk
import tkinter.ttk as ttk


class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


window = tk.Tk()
window.title("База Данных")
menu = tk.Menu()  # меню (toolbar)
new_item = tk.Menu(menu, tearoff=0)
new_item.add_command(label='Новый')  # новый элемент меню
menu.add_cascade(label='Файл', menu=new_item)  # новый элемент внутри каскада меню
window.config(menu=menu)
table = Table(window, headings=('Код производителя', 'Производитель', 'Страна',
'Код товара', 'Модель', 'Внутренняя память', 'Диагональ экрана', 'Процессор',
'Оперативная память', 'Кол-во смартфонов'),
rows=((123, 456, 789), ('abc', 'def', 'ghk')))
table.pack(expand=tk.YES, fill=tk.BOTH)
window.mainloop()
