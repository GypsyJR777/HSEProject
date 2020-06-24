"""
Функция создает главное окно программы, задает размер, цвет фона
Получает: -
Возвращает: -
Автор: Демидов И.Д., Матвеев В.Е., Будин А.М.
"""

import tkinter as tk
import sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from app import Main

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT["bg"] = "#B0C7E4"
    ROOT.state("zoomed")
    ROOT.title("База данных смартфонов")
    W, H = ROOT.winfo_screenwidth()-100, ROOT.winfo_screenheight()-100
    ROOT.geometry("%dx%d+0+0" % (W, H))
    ROOT.resizable(True, True)
    Main(ROOT)
    ROOT.mainloop()
