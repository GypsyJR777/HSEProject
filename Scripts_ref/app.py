import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from bd import Table

def open_dialog():
    global tree, mdf, parent
    Child_add(tree, mdf, parent)

def sort():
    global tree, mdf, parent
    Child_filter(tree, mdf, parent)

def change():
    global tree, mdf, parent
    Change(tree, mdf, parent)

def delete():
    global tree, mdf, parent
    Delete(tree, mdf, parent)

def analysis():
    global tree, mdf, parent
    Kowalski_analis(tree, mdf, parent)

def saved():
    global mdf
    mdf.to_pickle("../Data/smartphones.pkl")
    writer = pd.ExcelWriter('../Output/Result.xlsx')
    mdf.to_excel(writer, 'smartphones')
    writer.save()

def Elements():
    global tree, mdf, parent
    frame_toolbox = tk.Frame(parent, bd=5, bg="#B0C7E4")
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
    button2_box3=tk.Button(frame_toolbox, bg="#B0C7E4", image=photo, compound='left', relief="flat")

    # pack elemests of toolbox
    button1_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
    button2_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
    button3_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
    button4_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
    button1_box2.pack(side='left', padx=5, ipadx=8, ipady=8)
    button1_box3.pack(side='left', padx=5, ipadx=8, ipady=8)
    button2_box3.pack(side='right')

def Open_bd():
    global tree, mdf, parent
    try:
        xls = pd.read_pickle("../Data/smartphones.pkl")
    except (FileNotFoundError, EOFError):
        xls = pd.DataFrame(columns=["Product Code", "Manufacturer", "Country", "Model", "OS", "Storage", "Diagonal", "CPU", "RAM", "Amount"])
    mdf = pd.DataFrame(xls)
    tree = Table(parent, mdf)

class Main(tk.Frame):
    def __init__(self):
        global tree, mdf, parent
        root = tk.Tk()
        root["bg"]="#B0C7E4"
        root.state("zoomed")
        root.title("Программа")
        parent = root
        Elements()
        Open_bd()
        root.geometry("600x400")
        root.mainloop()
