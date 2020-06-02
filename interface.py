from tkinter import * #

window = Tk()
window.title("База Данных")
window.geometry('900x540+300+200')

menu = Menu(window)  # меню (toolbar)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Новый')  # новый элемент меню
menu.add_cascade(label='Файл', menu=new_item)  # новый элемент внутри каскада меню
window.config(menu=menu)

# надо переписать табличку тут
frame = Frame(window, relief=RAISED, borderwidth=1)
frame.pack(fill=BOTH, expand=True)
closeButton = Button(window, text="Close")
closeButton.pack(side=RIGHT, padx=5, pady=5)
okButton = Button(window, text="OK")
okButton.pack(side=RIGHT)

table_frame = Frame(window,borderwidth=1)
table_frame.grid(column=0, row=0)

table.tree = Treeview(self, columns = ('cod', 'proizv', 'strana', 'codtov', 'model', 'oc', 'vnutrpam', 'diagonal', 'proc', 'operpam', 'kolvo'),  height=40, show='headings')
table.tree.column('cod', width=60, anchor=tk.CENTER)
table.tree.column('proizv', width=60, anchor=tk.CENTER)
table.tree.column('strana', width=60, anchor=tk.CENTER)
table.tree.column('codtov', width=60, anchor=tk.CENTER)
table.tree.column('model', width=60, anchor=tk.CENTER)
table.tree.column('oc', width=60, anchor=tk.CENTER)
table.tree.column('vnutrpam', width=60, anchor=tk.CENTER)
table.tree.column('diagonal', width=60, anchor=tk.CENTER)
table.tree.column('proc', width=60, anchor=tk.CENTER)
table.tree.column('operpam', width=60, anchor=tk.CENTER)
table.tree.column('kolvo', width=60, anchor=tk.CENTER)
table.tree.heading('cod', text='код производителя')
table.tree.heading('proizv', text='производитель')
table.tree.heading('strana', text='страна')
table.tree.heading('codtov', text='код товара')
table.tree.heading('model', text='модель')
table.tree.heading('oc', text='ОС')
table.tree.heading('vnutrpam', text='внутренняя память')
table.tree.heading('diagonal', text='диагональ экрана')
table.tree.heading('proc', text='процессор')
table.tree.heading('operpam', text='оперативаная память')
table.tree.heading('kolvo', text='кол-во')
table.tree.pack()

window.mainloop()
