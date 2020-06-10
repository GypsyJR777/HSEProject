import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from bd import Table
from filters import Child_filter
from add import Child_add
from change import Change
from delete import Delete
from graphs import Kowalski_analis

def open_dialog():
    global mdf, parent
    Child_add(mdf, parent)

def sort():
    global mdf, parent
    Child_filter(mdf, parent)

def change():
    global mdf, parent
    Change(mdf, parent)

def delete():
    global mdf, parent
    Delete(mdf, parent)

def analysis():
    global mdf, parent
    Kowalski_analis(mdf, parent)

def saved():
    global mdf
    mdf.to_pickle("../Data/smartphones.pkl")
    writer = pd.ExcelWriter('../Output/Result.xlsx')
    mdf.to_excel(writer, 'smartphones')
    writer.save()

def elems(par):
    frame_toolbox = tk.Frame(par, bd=5, bg="#B0C7E4")
    frame_toolbox.pack(side='top', fill=tk.X)

    #frame with controls
    frame_box2 = tk.Frame(frame_toolbox, bd=5, bg="#B0C7E4")
    frame_box2.pack(side='left', fill=tk.Y, expand=1)

    # frame for the Table
    photo = tk.PhotoImage(file = r"../img.png")
    photo = photo.subsample(25, 25)

    # elemests of toolbox
    button1_box1=tk.Button(frame_box2, text=u'Добавить', command=open_dialog, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
    button2_box1=tk.Button(frame_box2, text=u'Правка', command=change, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
    button3_box1=tk.Button(frame_box2, text=u'Удалить', command=delete, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
    button4_box1=tk.Button(frame_box2, text=u'Экспорт', command=saved, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
    button1_box2=tk.Button(frame_box2, text=u'Анализ', command=analysis, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
    button1_box3=tk.Button(frame_box2, text=u'Фильтр', command=sort, bg="#5E46E0", fg="white", font="TimesNewRoman 16")

    # pack elemests of toolbox
    button1_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
    button2_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
    button3_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
    button4_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
    button1_box2.pack(side='left', padx=5, ipadx=8, ipady=8)
    button1_box3.pack(side='left', padx=5, ipadx=8, ipady=8)

def open_bd(par):
    global mdf, parent
    parent = par
    try:
        xls = pd.read_pickle("../Data/smartphones.pkl")
    except (FileNotFoundError, EOFError):
        xls = pd.DataFrame(columns=["Product Code", "Manufacturer", "Country", "Model", "OS", "Storage", "Diagonal", "CPU", "RAM", "Amount"])
    mdf = pd.DataFrame(xls)
    Table(par, mdf)

class Main(tk.Frame):
    def __init__(self):
        root = tk.Tk()
        root["bg"]="#B0C7E4"
        root.state("zoomed")
        root.title("Программа")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (w, h))
        root.resizable(False, False)
        w, h = root.winfo_screenwidth()-100, root.winfo_screenheight()-100
        root.geometry("%dx%d+0+0" % (w, h))

        elems(root)
        open_bd(root)
        root.mainloop()

        print('DataFrame is written successfully to Excel Sheet.')
