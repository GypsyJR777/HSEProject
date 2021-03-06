"""
Функция создает базу данных
Получает: -
Возвращает: -
Автор: Матвеев В.Е., Демидов И.Д., Будин А.М.
"""
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import os, sys
sys.path.insert(0, os.path.abspath("../Scripts"))
import app as m

def treeview_sort_column(tv, col, reverse):
    '''
    Функция производит сортировку по столбцам (по возрастанию и по убыванию)
    Получает: tv - объект сортировки, col - название столбца,
        reverse - определяет направление сортировки
    Возращает: -
    Автор: Матвеев В.Е., Демидов И.Д., Будин А.М.
    '''
    l = [(tv.set(k, col), k) for k in tv.get_children()]
    if (col == 'RAM' or col == 'Product Code' or col == 'Amount' or col == 'Storage'):
        l.sort(key=lambda t: int(t[0]), reverse=reverse)
    else:
        l.sort(reverse=reverse)
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)
    # reverse sort next time
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))


def Table(parent=None, xls=None):
    '''
    Функция создает таблицу и добавляет к ней сколлбары
    Получает: parent-название окна, xls-структура DataFrame
    Возращает: -
    Автор: Демидов И.Д, Матвеев В.Е.
    '''
    df = pd.DataFrame(xls)
    count = len(df)
    headings = xls.columns.tolist()
    tree = ttk.Treeview(parent, show="headings", selectmode="browse")
    tree["columns"] = headings
    tree["displaycolumns"] = headings
    for head in headings:
        tree.heading(head, text=head, anchor=tk.CENTER)
        tree.column(head, anchor=tk.CENTER, width=50)
        tree.heading(head, text=head, command=lambda head_=head: treeview_sort_column(tree, head_, False))
    for i in range(count):
        tree.insert('', i, values=df.iloc[i, :].tolist())
    scrollbar = tk.Scrollbar(tree, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    scrollbarx = tk.Scrollbar(tree, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=scrollbarx.set)
    scrollbarx.pack(side="bottom", fill="x")
    tree.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
    m.mdf = m.mdf.reset_index(drop=True)
    parent.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
