import tkinter as tk
from app import Main

if __name__ == "__main__":
    root = tk.Tk()
    root["bg"] = "#B0C7E4"
    root.state("zoomed")
    root.title("Программа")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.resizable(False, False)
    Main(root)
    root.mainloop()
    