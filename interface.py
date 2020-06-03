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


# фрейм с кнопками управления
frame_toolbar = tk.Frame(window, bg='red', bd=2)
frame_toolbar.pack(side='top')

# фрейм 1-ого элемента управления
frame_box1 = tk.Frame(frame_toolbar, bg='purple', bd=2)
frame_box1.pack()

# фрейм 2-ого элемента управления
frame_box2 = tk.Frame(frame_toolbar, bg='black', bd=2)
frame_box2.pack()

# фрейм 3-ого элемента управления
frame_box3 = tk.Frame(frame_toolbar, bg='blue', bd=2)
frame_box3.pack()

# фрейм с табличкой
frame_table = tk.Frame(window, bg='green', bd=2)
frame_table.pack(side='bottom')

# таблица
table = Table(frame_table, headings=('Код производителя', 'Производитель', 'Страна',
'Код товара', 'Модель', 'Внутренняя память', 'Диагональ экрана', 'Процессор',
'Оперативная память', 'Кол-во смартфонов'),
rows=((123, 456, 789, 7, 9, 10, 13), ('abc', 'def', 'ghk')))
table.pack(expand=tk.YES, fill=tk.BOTH)



button1=tk.Button(frame_box1, text=u'Первая кнопка')
button2=tk.Button(frame_box2, text=u'Вторая кнопка')
button3=tk.Button(frame_box3, text=u'Первая кнопка')
#button4=tk.Button(frame_table, text=u'Вторая кнопка')
button1.pack()
button2.pack()
button3.pack()
#button4.pack()




window.mainloop()
