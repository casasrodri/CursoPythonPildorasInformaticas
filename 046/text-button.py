import tkinter as tk
from typing import Text

root = tk.Tk()

frame = tk.Frame(root, width=1200, height=600)
frame.pack()

# Text

comentariosLabel = tk.Label(frame, text='Comentarios:')
comentariosLabel.grid(row=0, column=0, sticky='nw', padx=5, pady=5)

comentariosText = tk.Text(frame, width=16, height=5)
comentariosText.grid(row=0, column=1, sticky='w', padx=5, pady=5)

scrollVertical = tk.Scrollbar(frame, command=comentariosText.yview)
scrollVertical.grid(row=0, column=2, sticky='nsew')

comentariosText.config(yscrollcommand=scrollVertical.set)

# Entry
miNombre = tk.StringVar()
editable = tk.Entry(frame, textvariable=miNombre)
editable.grid(row=1,column=0)

# Button
def apretarGuardar():
    print('Se ha guardado el campo en la base de datos...')
    print(comentariosText.get("1.0","end-1c"))
    miNombre.set('Rodrigo')

botonGuardar = tk.Button(root, text='Guardar', command=apretarGuardar)
botonGuardar.pack()

root.mainloop()