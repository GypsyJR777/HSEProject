import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd


def Table(parent=None, xls=None):
        df = pd.DataFrame(xls)
        count = len(df)
        headings = ["Product Code", "Manufacturer", "Country", "Model", "OS", "Storage", "Diagonal", "CPU", "RAM", "Amount"]
        tree = ttk.Treeview(parent, show="headings", selectmode="browse")
        tree["columns"]=headings
        tree["displaycolumns"]=headings

        for head in headings:
            tree.heading(head, text=head, anchor=tk.CENTER)
            tree.column(head, anchor=tk.CENTER, width=50)

        for i in range(count):
            tree.insert('', i, values=df.iloc[i,:].tolist())

        scrollbar = tk.Scrollbar(tree, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")

        scrollbarx = tk.Scrollbar(tree, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=scrollbarx.set)

        scrollbarx.pack(side="bottom", fill="x")
        tree.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
        parent.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
