import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from bd import Table
from filtres import Child_filter



class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.init_main()
    
    
    def init_main(self):   
        global mdf, her
        frame_toolbox = tk.Frame(bd=5, bg="#B0C7E4")
        frame_toolbox.pack(side='top', fill=tk.X)
        
        frame_table = tk.Frame(bd=5, bg="#B0C7E4")
        
        her = frame_table
        
        #frame with controls
        frame_box2 = tk.Frame(frame_toolbox, bd=5, bg="#B0C7E4")
        frame_box2.pack(side='left', fill=tk.Y, expand=1)

        photo = tk.PhotoImage(file = r"../img.png")
        photo = photo.subsample(25, 25)

        # elemests of toolbox
        button1_box1 = tk.Button(frame_box2, text=u'Добавить', command=self.open_dialog, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button2_box1 = tk.Button(frame_box2, text=u'Правка', command=self.change, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button3_box1 = tk.Button(frame_box2, text=u'Удалить', command=self.delete, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button4_box1 = tk.Button(frame_box2, text=u'Экспорт', command=self.saved, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button1_box2 = tk.Button(frame_box2, text=u'Анализ', command=self.analysis, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        button1_box3 = tk.Button(frame_box2, text=u'Фильтр', command=self.sort, bg="#5E46E0", fg="white", font="TimesNewRoman 16")
        #button2_box3 = tk.Button(frame_toolbox, bg="#B0C7E4", image=photo, compound=tk.LEFT, relief="flat")

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
        Table(frame_table, mdf)
    
    
    def open_dialog(self):
        '''
        Функция вызывает класс Child_add для создания окна добавления нового элемента таблицы
        Получает: -
        Возвращает: -
        Автор:
        '''
        pass

    def sort(self):
        '''
        Функция вызывает класс Child_filter для сортировки таблицы
        Получает: -
        Возвращает: -
        Автор:
        '''
        global mdf, her
        Child_filter(mdf, her)


    def change(self):
        '''
        Функция вызывает класс Change для редактирования элемента таблицы
        Получает: -
        Возвращает: -
        Автор:
        '''
        pass


    def delete(self):
        '''
        Функция вызывает класс Delete для удаления элемента таблицы
        Получает: -
        Возвращает: -
        Автор:
        '''
        pass


    def analysis(self):
        '''
        Функция вызвывает класс Kowalski_analis для различных методов анализа
        Получает: -
        Возвращает: -
        Автор:
        '''
        pass


    def saved(self):
        '''
        Функция сохраняет таблицу в формате Excel
        Получает: -
        Возвращает: -
        Автор: Матвеев В.Е.
        '''
        global mdf
        #mdf.to_pickle("../Data/smartphones.pkl")
        writer = pd.ExcelWriter('../Output/Result.xlsx')
        mdf.to_excel(writer, 'smartphones')
        writer.save()
        print('DataFrame is written successfully to Excel Sheet.')
        
        
#root = tk.Tk()
#root["bg"] = "#B0C7E4"
#root.state("zoomed")
#root.title("Программа")
#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.geometry("%dx%d+0+0" % (w, h))
#root.resizable(False, False)
#Main(root)
