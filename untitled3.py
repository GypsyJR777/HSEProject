import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from filters import Child_filter

def open_dialog():
        pass
        #Child_add()

def change():
        #Change()
        pass

def delete():
       # Delete()
       pass

def analysis():
        #Kowalski_analis()
        pass



def saved():
        global mdf
        mdf.to_pickle("../Data/smartphones.pkl")
        writer = pd.ExcelWriter('../Output/Result.xlsx')
        mdf.to_excel(writer, 'smartphones')
        writer.save()

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
    def init_main(self):
        global mdf
        def Table(parent=None, xls=None):
            global counter, tree, df
            df = pd.DataFrame(xls)
            count = len(df)
            headings = ["Product Code", "Manufacturer", "Country", "Model", "OS", "Storage", "Diagonal", "CPU", "RAM", "Amount"]
            tree = ttk.Treeview(root, show="headings", selectmode="browse")
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
#        root = tk.Tk()
#        root["bg"]="#B0C7E4"
#        root.state("zoomed")
#        root.title("Программа")
#        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#        root.geometry("%dx%d+0+0" % (w, h))
#        root.resizable(False, False)
        
        w, h = root.winfo_screenwidth()-100, root.winfo_screenheight()-100
        root.geometry("%dx%d+0+0" % (w, h))
        frame_toolbox = tk.Frame(bd=5, bg="#B0C7E4")
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
        button1_box3=tk.Button(frame_box2, text=u'Фильтр', command=self.sort, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        #button2_box3=tk.Button(frame_toolbox, bg="#B0C7E4", image=photo, compound=tk.LEFT, relief="flat")

        # pack elemests of toolbox
        button1_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
        button2_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
        button3_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
        button4_box1.pack(side='left', padx=5, ipadx=8, ipady=8)
        button1_box2.pack(side='left', padx=5, ipadx=8, ipady=8)
        button1_box3.pack(side='left', padx=5, ipadx=8, ipady=8)
        #button2_box3.pack(side='right')

        try:
            xls = pd.read_pickle("../Data/smartphones.pkl")
        except (FileNotFoundError, EOFError):
            xls = pd.DataFrame(columns=["Product Code", "Manufacturer", "Country", "Model", "OS", "Storage", "Diagonal", "CPU", "RAM", "Amount"])
        mdf = pd.DataFrame(xls)
        Table(root, mdf)
        
        root.mainloop()
        print('DataFrame is written successfully to Excel Sheet.')


    def sort(self):
        global mdf
        Child_filter(tree, mdf)


root = tk.Tk()
root["bg"]="#B0C7E4"
root.state("zoomed")
app = Main(root)
app.pack()
root.title("Программа")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.resizable(False, False)