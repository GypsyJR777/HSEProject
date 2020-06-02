import sys
sys.path.append('../Library/')



import pickle
import pandas as pd
from tkinter import Tk, Frame, Toplevel, Label, Entry, Button, Checkbutton, Scale, Canvas, Scrollbar, FLAT, GROOVE, N, S, E, W, IntVar, END, YES, BOTH, SOLID, LabelFrame
from materials import road_to_data

global base
'''
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
'''
def import_lib(import_filename):
    import pickle
    from tkinter.messagebox import showerror
    try:
        libfile = open(import_filename, 'rb')
    except:
        showerror(title='Ошибка!', message="Файл не найден!")
    else:
        lib = pickle.load(libfile)
        libfile.close()
    return lib


def show_base():
    for widget in frame.winfo_children():
        widget.destroy()
    frame.grid_forget()
    n = 0
    Label(frame, text="Haзвание").grid(row=n, column=0, pady=5)
    Label(frame, text="Автор").grid(row=n, column=1, pady=5)
    Label(frame, text="Раздел").grid(row=n, column=2, pady=5)
    Label(frame, text="Страницы").grid(row=n, column=3, pady=5)
    Label(frame, text="Цена").grid(row=n, column=4, pady=5)
    Label(frame, text="Год издания").grid(row=n, column=5, pady=5)






window = tk.Tk()
window.title("База Данных")
menu = tk.Menu()  # меню (toolbar)
new_item = tk.Menu(menu, tearoff=0)
new_item.add_command(label='Новый')  # новый элемент меню
menu.add_cascade(label='Файл', menu=new_item)  # новый элемент внутри каскада меню
window.config(menu=menu)
#table = Table(window, headings=('Код производителя', 'Производитель', 'Страна','Код товара', 'Модель', 'Внутренняя память', 'Диагональ экрана', 'Процессор','Оперативная память', 'Кол-во смартфонов'),rows=((123, 456, 789), ('abc', 'def', 'ghk')))
table.pack(expand=tk.YES, fill=tk.BOTH)
base = import_lib(road_to_data)
show_base()
window.mainloop()
