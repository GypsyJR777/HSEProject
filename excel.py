import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

bd = pd.read_excel('./Data/Smartphones.xlsx', sheet_name='Sheet1')

# print whole sheet data
#print(bd.keys())
key = bd.columns.values

print(key)
a = {}
for i in key:
    for j in bd[i]:
        a[i] = j
df = pd.DataFrame(bd)
#print(a)
































'''
class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
        global value, key
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings
        for head in key:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
            for row in bd[head]:
                table.insert('', tk.END, values=str(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)
'''

window = tk.Tk()
window.title("База Данных")
menu = tk.Menu()  # меню (toolbar)
new_item = tk.Menu(menu, tearoff=0)
new_item.add_command(label='Новый')  # новый элемент меню
menu.add_cascade(label='Файл', menu=new_item)  # новый элемент внутри каскада меню
window.config(menu=menu)
#table = Table(window, headings=('Код производителя', 'Производитель', 'Страна','Код товара', 'Модель', 'Внутренняя память', 'Диагональ экрана', 'Процессор','Оперативная память', 'Кол-во смартфонов'),rows=((123, 456, 789), ('abc', 'def', 'ghk')))
#table.pack(expand=tk.YES, fill=tk.BOTH)


tree = ttk.Treeview(window)
rowLabels = df.index.tolist()
tree["columns"]=(key)
counter = len(df)
for x in range(len(key)):
    tree.column(key[x], width=100)
    tree.heading(key[x], text=key[x])
    for i in range(counter):
        tree.insert('', i, text=rowLabels[i], values=df.iloc[i,:].tolist())
tree.pack()
window.mainloop()
