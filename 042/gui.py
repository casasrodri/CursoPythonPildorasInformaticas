# Algunas librerias
# - Tkinter
# - WxPython
# - PyQT
# - PyGTK
# - TCL/TK

import tkinter as tk

root = tk.Tk()

root.title('Ventana de prueba')

root.resizable(height = True, width = False)
root.geometry('500x300')

root.iconbitmap('042/green.ico')

root.config(bg='green')
root.mainloop()
