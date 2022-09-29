import tkinter as tk

raiz = tk.Tk()

playa = tk.IntVar()
montagna = tk.IntVar()
campo = tk.IntVar()

def imprimir():
    opcionSeleccionada = ''

    if playa.get() == 1:
        opcionSeleccionada += ' playa'
    if montagna.get() == 1:
        opcionSeleccionada += ' montaña'
    if campo.get() == 1:
        opcionSeleccionada += ' campo'

    labelSelecc.config(text=opcionSeleccionada)


tk.Label(raiz, text='Donde te gustaría vacacionar este verano?').pack()

tk.Checkbutton(raiz, text='Playa', variable=playa, onvalue=1, offvalue=0, command=lambda:imprimir()).pack()
tk.Checkbutton(raiz, text='Montaña', variable=montagna, onvalue=1, offvalue=0, command=lambda:imprimir()).pack()
tk.Checkbutton(raiz, text='Campo', variable=campo, onvalue=1, offvalue=0, command=lambda:imprimir()).pack()

labelSelecc = tk.Label(raiz)
labelSelecc.pack()

raiz.mainloop()
