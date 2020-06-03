import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

# xls = pd.read_excel('C:/users/ivand/github/HSEProject/Data/Smartphones.xlsx')
# df = pd.DataFrame(xls)
# df_col = df.columns.values

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


class Table(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        xls = pd.read_excel('./Data/Smartphones.xlsx')
        df = pd.DataFrame(xls)
        df_col = df.columns.values
        df_col = df.columns.values
        tree = ttk.Treeview(window)
        tree["columns"]=(df_col)
        counter = len(df)
        rowLabels = df.index.tolist()
        df.reset_index(drop=True, inplace=True)
        #generating for loop to create columns and give heading to them through df_col var.
        for x in range(9):
            tree.column(x, width=100 )
            tree.heading(x, text=df_col[x])
        #generating for loop to print values of dataframe in treeview column.
        for i in range(counter):
            tree.insert('', i, text=rowLabels[i], values=df.iloc[i,:].tolist())
        tree.pack(expand=tk.YES, fill=tk.BOTH)




# main frame for tools
frame_toolbox = tk.Frame(window, bd=5)
frame_toolbox.pack(side='top', fill=tk.X)

# 1-st frame with controls
frame_box1 = tk.Frame(frame_toolbox, bd=5)
frame_box1.pack(side='left', fill=tk.Y, expand=1)

# 2-nd frame with controls
frame_box2 = tk.Frame(frame_toolbox, bd=5)
frame_box2.pack(side='left', fill=tk.Y, expand=1)

# 3-rd frame with controls
frame_box3 = tk.Frame(frame_toolbox, bd=5)
frame_box3.pack(side='left', fill=tk.Y, expand=1)

# frame for the Table
frame_table = tk.Frame(window, bd=2)
frame_table.pack(side='bottom')


# elemests of 1-st box
frame_box1_top = tk.Frame(frame_box1, bd=5)
frame_box1_bottom = tk.Frame(frame_box1, bd=5)
button1_box1=tk.Button(frame_box1_top, text=u'добавить')
button2_box1=tk.Button(frame_box1_top, text=u'Правка')
button3_box1=tk.Button(frame_box1_bottom, text=u'Удалить')
button4_box1=tk.Button(frame_box1_bottom, text=u'Экспорт')


# pack elemests of 1-st box
frame_box1_top.pack(side='top')
frame_box1_bottom.pack(side='top')
button1_box1.pack(side='left')
button2_box1.pack(side='left')
button3_box1.pack(side='left')
button4_box1.pack(side='left')

# elemests of 2-nd box
button1_box2=tk.Button(frame_box2, text=u'Анализ')
button2_box2=tk.Button(frame_box2, text=u'Экспорт')

# pack elemests of 2-nd box
button1_box2.pack(side='left')
button2_box2.pack(side='left')

# elemests of 3-rd box
button1_box3=tk.Button(frame_box3, text=u'Первая кнопка')
button2_box3=tk.Button(frame_box3, text=u'Вторая кнопка')

# pack elemests of 3-rd box
button1_box3.pack(side='left')
button2_box3.pack(side='left')



table = Table(window)
# table
# tree = ttk.Treeview(window)
#
# tree["columns"]=(df_col)
# counter = len(df)
# rowLabels = df.index.tolist()
# df.reset_index(drop=True, inplace=True)
# #generating for loop to create columns and give heading to them through df_col var.
# for x in range(9):
#     tree.column(x, width=100 )
#     tree.heading(x, text=df_col[x])
# #generating for loop to print values of dataframe in treeview column.
# for i in range(counter):
#     tree.insert('', i, text=rowLabels[i], values=df.iloc[i,:].tolist())


window.mainloop()
