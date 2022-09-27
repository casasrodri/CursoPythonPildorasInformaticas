import tkinter as tk

root = tk.Tk()
root.title('Calculadora')

pantalla = tk.Frame(root)
pantalla.pack()

num_ope = tk.Frame(root)
num_ope.pack()

numeros = tk.Frame(num_ope)
numeros.grid(row=0, column=0)
operaciones = tk.Frame(num_ope)
operaciones.grid(row=0, column=1)

ingresado = tk.StringVar()

# Interacción
def insertar_pantalla(num):
    ingresado.set(ingresado.get() + str(num))


def calcular():
    if '+' in ingresado.get():
        valores = ingresado.get().split('+')
        resultado = int(valores[0]) + int(valores[1])
    else:
        valores = ingresado.get().split('-')
        resultado = int(valores[0]) - int(valores[1])
    
    ingresado.set(str(resultado))


# Botones

# Números
b1 = tk.Button(numeros, text='1', command=lambda: insertar_pantalla(1))
b1.grid(row=2, column=0)

b2 = tk.Button(numeros, text='2', command=lambda: insertar_pantalla(2))
b2.grid(row=2, column=1)

b3 = tk.Button(numeros, text='3', command=lambda: insertar_pantalla(3))
b3.grid(row=2, column=2)

b4 = tk.Button(numeros, text='4', command=lambda: insertar_pantalla(4))
b4.grid(row=1, column=0)

b5 = tk.Button(numeros, text='5', command=lambda: insertar_pantalla(5))
b5.grid(row=1, column=1)

b6 = tk.Button(numeros, text='6', command=lambda: insertar_pantalla(6))
b6.grid(row=1, column=2)

b7 = tk.Button(numeros, text='7', command=lambda: insertar_pantalla(7))
b7.grid(row=0, column=0)

b8 = tk.Button(numeros, text='8', command=lambda: insertar_pantalla(8))
b8.grid(row=0, column=1)

b9 = tk.Button(numeros, text='9', command=lambda: insertar_pantalla(9))
b9.grid(row=0, column=2)

b0 = tk.Button(numeros, text='0', command=lambda: insertar_pantalla(0))
b0.grid(row=4, column=1)


# Pantalla
label_descripcion = tk.Label(pantalla, text='Resultado:')
label_descripcion.grid(row=0, column=0)


label_numeros = tk.Label(pantalla, textvariable=ingresado)
label_numeros.grid(row=1, column=0)

# Operaciones
bntMas = tk.Button(operaciones, text='+', command=lambda: insertar_pantalla('+'))
bntMas.grid(row=0, column=0)

bntMenos = tk.Button(operaciones, text='-', command=lambda: insertar_pantalla('-'))
bntMenos.grid(row=1, column=0)

bntIgual = tk.Button(operaciones, text='=', command=calcular)
bntIgual.grid(row=2, column=0)


root.mainloop()