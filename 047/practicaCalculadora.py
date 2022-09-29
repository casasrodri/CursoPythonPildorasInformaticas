import tkinter as tk

raiz = tk.Tk()

miFrame = tk.Frame(raiz)
miFrame.pack()

# ------------ PANTALLA ---------------------
pantalla = tk.Entry(miFrame)
pantalla.grid(row=1, column=1, padx= 10, pady=10, columnspan=4)
pantalla.config(background='black', fg='green', justify='right')


# ------------ FILA 1 ---------------------
boton7 = tk.Button(miFrame, text='7', width=3)
boton7.grid(row=2, column=1)
boton8 = tk.Button(miFrame, text='8', width=3)
boton8.grid(row=2, column=2)
boton9 = tk.Button(miFrame, text='9', width=3)
boton9.grid(row=2, column=3)
botonMult = tk.Button(miFrame, text='x', width=3)
botonMult.grid(row=2, column=4)


# ------------ FILA 2 ---------------------
boton4 = tk.Button(miFrame, text='4', width=3)
boton4.grid(row=3, column=1)
boton5 = tk.Button(miFrame, text='5', width=3)
boton5.grid(row=3, column=2)
boton6 = tk.Button(miFrame, text='6', width=3)
boton6.grid(row=3, column=3)
botonDiv = tk.Button(miFrame, text='/', width=3)
botonDiv.grid(row=3, column=4)


# ------------ FILA 3 ---------------------
boton1 = tk.Button(miFrame, text='1', width=3)
boton1.grid(row=4, column=1)
boton2 = tk.Button(miFrame, text='2', width=3)
boton2.grid(row=4, column=2)
boton3 = tk.Button(miFrame, text='3', width=3)
boton3.grid(row=4, column=3)
botonResta = tk.Button(miFrame, text='-', width=3)
botonResta.grid(row=4, column=4)


# ------------ FILA 4 ---------------------
botonComa = tk.Button(miFrame, text='.', width=3)
botonComa.grid(row=5, column=1)
boton0 = tk.Button(miFrame, text='0', width=3)
boton0.grid(row=5, column=2)
botonIgual = tk.Button(miFrame, text='=', width=3)
botonIgual.grid(row=5, column=3)
botonSuma = tk.Button(miFrame, text='+', width=3)
botonSuma.grid(row=5, column=4)


raiz.mainloop()
