import tkinter as tk
from turtle import width

raiz = tk.Tk()
raiz.config(width=300, height=300)

barraMenu = tk.Menu(raiz)
raiz.config(menu=barraMenu)

archivoMenu = tk.Menu(barraMenu, tearoff=False)
archivoMenu.add_command(label='Nuevo')
archivoMenu.add_separator()
archivoMenu.add_command(label='Guardar')
archivoMenu.add_command(label='Guardar como...')
archivoMenu.add_command(label='Cerrar')
archivoMenu.add_separator()
archivoMenu.add_command(label='Salir')



edicionMenu = tk.Menu(barraMenu, tearoff=False)
edicionMenu.add_command(label='Copiar')
edicionMenu.add_command(label='Cortar')
edicionMenu.add_command(label='Pegar')


herramientasMenu = tk.Menu(barraMenu, tearoff=False)
herramientasMenuBasicas = tk.Menu(herramientasMenu, tearoff=False)
herramientasMenuAvanzadas = tk.Menu(herramientasMenu, tearoff=False)

herramientasMenu.add_cascade(label='Básicas', menu=herramientasMenuBasicas)
herramientasMenu.add_cascade(label='Avanzadas', menu=herramientasMenuAvanzadas)
herramientasMenu.add_checkbutton(label='Modo experto')

ayudaMenu = tk.Menu(barraMenu, tearoff=False)
ayudaMenu.add_command(label='Licencia')
ayudaMenu.add_separator()
ayudaMenu.add_command(label='Acerca de...')

barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
barraMenu.add_cascade(label='Edición', menu=edicionMenu)
barraMenu.add_cascade(label='Herramientas', menu=herramientasMenu)
barraMenu.add_cascade(label='Ayuda', menu=ayudaMenu)

raiz.mainloop()
