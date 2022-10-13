import tkinter as tk


raiz = tk.Tk()

miFrame = tk.Frame(raiz)
miFrame.pack()

# ------------ PANTALLA ---------------------

numeroPantalla = tk.StringVar()

pantalla = tk.Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx= 10, pady=10, columnspan=4)
pantalla.config(background='black', fg='green', justify='right')

# --- Pulsación teclado

def numero_pulsado(num):
    if not (num == '0' and numeroPantalla.get() == ''):
        numeroPantalla.set(numeroPantalla.get() + num)

# ---> Agregadas por Rodri
num1=None
operation=None
def operacion_pulsada(ope):
    global num1, operation
    if num1 is None:
        num1 = float(numeroPantalla.get())
        operation = ope
        numeroPantalla.set('')

def resultado():
    global num1, operation
    num2 = float(numeroPantalla.get())
    if operation == 'x':
        resultado = num1 * num2
    elif operation == '/':
        resultado = num1 / num2
    elif operation == '+':
        resultado = num1 + num2
    elif operation == '-':
        resultado = num1 - num2

    num1 = None
    operation = None

    numeroPantalla.set(str(resultado))

# ------------ FILA 1 ---------------------
boton7 = tk.Button(miFrame, text='7', width=3, command=lambda:numero_pulsado('7'))
boton7.grid(row=2, column=1)
boton8 = tk.Button(miFrame, text='8', width=3, command=lambda:numero_pulsado('8'))
boton8.grid(row=2, column=2)
boton9 = tk.Button(miFrame, text='9', width=3, command=lambda:numero_pulsado('9'))
boton9.grid(row=2, column=3)
botonMult = tk.Button(miFrame, text='x', width=3, command=lambda: operacion_pulsada('x'))
botonMult.grid(row=2, column=4)


# ------------ FILA 2 ---------------------
boton4 = tk.Button(miFrame, text='4', width=3, command=lambda:numero_pulsado('4'))
boton4.grid(row=3, column=1)
boton5 = tk.Button(miFrame, text='5', width=3, command=lambda:numero_pulsado('5'))
boton5.grid(row=3, column=2)
boton6 = tk.Button(miFrame, text='6', width=3, command=lambda:numero_pulsado('6'))
boton6.grid(row=3, column=3)
botonDiv = tk.Button(miFrame, text='/', width=3, command=lambda: operacion_pulsada('/'))
botonDiv.grid(row=3, column=4)


# ------------ FILA 3 ---------------------
boton1 = tk.Button(miFrame, text='1', width=3, command=lambda:numero_pulsado('1'))
boton1.grid(row=4, column=1)
boton2 = tk.Button(miFrame, text='2', width=3, command=lambda:numero_pulsado('2'))
boton2.grid(row=4, column=2)
boton3 = tk.Button(miFrame, text='3', width=3, command=lambda:numero_pulsado('3'))
boton3.grid(row=4, column=3)
botonResta = tk.Button(miFrame, text='-', width=3, command=lambda: operacion_pulsada('-'))
botonResta.grid(row=4, column=4)


# ------------ FILA 4 ---------------------
botonComa = tk.Button(miFrame, text='.', width=3, command=lambda:numero_pulsado('.'))
botonComa.grid(row=5, column=1)
boton0 = tk.Button(miFrame, text='0', width=3, command=lambda:numero_pulsado('0'))
boton0.grid(row=5, column=2)
botonIgual = tk.Button(miFrame, text='=', width=3, command=lambda:resultado())
botonIgual.grid(row=5, column=3)
botonSuma = tk.Button(miFrame, text='+', width=3, command=lambda: operacion_pulsada('+'))
botonSuma.grid(row=5, column=4)


raiz.mainloop()
