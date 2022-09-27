import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root, width=1200, height=600)
frame.pack()



nombreLabel = tk.Label(frame, text='Nombre:')
nombreLabel.grid(row=0, column=0, sticky='w', padx=5, pady=5) #nombreLabel.place(x=100, y=100)

passLabel = tk.Label(frame, text='Password:')
passLabel.grid(row=1, column=0, sticky='w', padx=5, pady=5)

apellidoLabel = tk.Label(frame, text='Apellido:')
apellidoLabel.grid(row=2, column=0, sticky='w', padx=5, pady=5)

direccionLabel = tk.Label(frame, text='Dirección de la casa:')
direccionLabel.grid(row=3, column=0, sticky='w', padx=5, pady=5)

# Entries

cuadroNombre = tk.Entry(frame)
cuadroNombre.grid(row=0, column=1, padx=5, pady=5) #cuadroTexto.place(x=100, y=100)
cuadroNombre.config(fg='red', justify='center')

cuadroPass = tk.Entry(frame)
cuadroPass.grid(row=1, column=1, padx=5, pady=5)
cuadroPass.config(show='●')

cuadroApellido = tk.Entry(frame)
cuadroApellido.grid(row=2, column=1, padx=5, pady=5)

cuadroDireccion = tk.Entry(frame)
cuadroDireccion.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()