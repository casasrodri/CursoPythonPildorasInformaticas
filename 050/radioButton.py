import tkinter as tk

raiz = tk.Tk()

varOpcion = tk.IntVar()

def imprimir():
    print(varOpcion.get())

tk.Label(raiz, text='Genero:').pack()
tk.Radiobutton(raiz, text='Masculino', variable=varOpcion, value=1, command=lambda: imprimir()).pack()
tk.Radiobutton(raiz, text='Femenino', variable=varOpcion, value=2, command=lambda: imprimir()).pack()


raiz.mainloop()
