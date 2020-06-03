import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

xls = pd.read_excel('./Data/Smartphones.xlsx')
df = pd.DataFrame(xls)
df_col = df.columns.values

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


window = tk.Tk()
window.title("База Данных")

# меню (toolbar)
main_menu = tk.Menu()

file_menu = tk.Menu(tearoff=0)
file_menu.add_command(label="Новый")
file_menu.add_command(label="Открыть")
file_menu.add_separator()
file_menu.add_command(label="Сохранить")
file_menu.add_command(label="Сохранить как")

main_menu.add_cascade(label="Файл", menu=file_menu)

window.config(menu=main_menu)


# фрейм с кнопками управления
frame_toolbox = tk.Frame(window, bd=5)
frame_toolbox.pack(side='top', fill=tk.X)

# фрейм 1-ого элемента управления
frame_box1 = tk.Frame(frame_toolbox, bd=5)
frame_box1.pack(side='left', fill=tk.Y, expand=1)

# фрейм 2-ого элемента управления
frame_box2 = tk.Frame(frame_toolbox, bd=5)
frame_box2.pack(side='left', fill=tk.Y, expand=1)

# фрейм 3-ого элемента управления
frame_box3 = tk.Frame(frame_toolbox, bd=5)
frame_box3.pack(side='left', fill=tk.Y, expand=1)

# фрейм с табличкой
frame_table = tk.Frame(window, bd=2)
frame_table.pack(side='bottom')

# таблица
'''
table = Table(frame_table, headings=('Код производителя', 'Производитель', 'Страна',
'Код товара', 'Модель', 'Внутренняя память', 'Диагональ экрана', 'Процессор',
'Оперативная память', 'Кол-во смартфонов'),
rows=((123, 456, 789, 7, 9, 10, 13), ('abc', 'def', 'ghk')))
table.pack(expand=tk.YES, fill=tk.BOTH)
'''

# элементы 1-го блока
frame_box1_top = tk.Frame(frame_box1, bd=5)
frame_box1_bottom = tk.Frame(frame_box1, bd=5)
button1_box1=tk.Button(frame_box1_top, text=u'добавить')
button2_box1=tk.Button(frame_box1_top, text=u'Правка')
button3_box1=tk.Button(frame_box1_bottom, text=u'Удалить')
button4_box1=tk.Button(frame_box1_bottom, text=u'Экспорт')


# упаковка элементов 1-го блока
frame_box1_top.pack(side='top')
frame_box1_bottom.pack(side='top')
button1_box1.pack(side='left')
button2_box1.pack(side='left')
button3_box1.pack(side='left')
button4_box1.pack(side='left')

# элементы 2-го блока
button1_box2=tk.Button(frame_box2, text=u'Анализ')
button2_box2=tk.Button(frame_box2, text=u'Экспорт')

# упаковка элементов 1-го блока
button1_box2.pack(side='left')
button2_box2.pack(side='left')

# элементы 3-го блока
button1_box3=tk.Button(frame_box3, text=u'Первая кнопка')
button2_box3=tk.Button(frame_box3, text=u'Вторая кнопка')

# упаковка элементов 1-го блока
button1_box3.pack(side='left')
button2_box3.pack(side='left')

tree = ttk.Treeview(window)

tree["columns"]=(df_col)
counter = len(df)
rowLabels = df.index.tolist()
#generating for loop to create columns and give heading to them through df_col var.
for x in range(10):
    tree.column(x, width=100 )
    tree.heading(x, text=df_col[x])
#generating for loop to print values of dataframe in treeview column.
for i in range(15):
    tree.insert('', i, text=rowLabels[i], values=df.iloc[i,:].tolist())
tree.pack(expand=tk.YES, fill=tk.BOTH)

window.mainloop()
