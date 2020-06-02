import pandas

excel_data_df = pandas.read_excel('./Data/Smartphones.xlsx', sheet_name='Sheet1')

# print whole sheet data
print(excel_data_df)
print(excel_data_df.columns.ravel())

import tkinter as tk
import tkinter.ttk as ttk


class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings

        for head in excel_data_df.columns.ravel():
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
        for head in excel_data_df.columns.ravel():
            for row in excel_data_df[head].tolist():
                table.insert('', tk.END, values=tuple(str(row)))

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
