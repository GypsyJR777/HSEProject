import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
def __init__(self, root):
super().__init__(root)
self.init_main()

def init_main(self):
toolbar1 = tk.Frame(bg='blue', bd=3)
toolbar1.pack(side=tk.RIGHT, fill=tk.Y)
toolbar2 = tk.Frame(bg='blue', bd=3)
toolbar2.pack(side=tk.BOTTOM, fill=tk.X)
btn_open_dialog = tk.Button(toolbar1, text='Добавить', command=self.open_dialog, bg='YELLOW', bd=0, compound = tk.TOP)
btn_open_dialog.pack(side=tk.LEFT)
self.tree = ttk.Treeview(self, columns = ('cod', 'proizv', 'strana', 'codtov', 'model', 'oc', 'vnutrpam', 'diagonal', 'proc', 'operpam', 'kolvo'), height=40, show='headings')

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
