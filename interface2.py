from tkinter import * #

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')


menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Новый')
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)


window.mainloop()
