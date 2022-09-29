import tkinter as tk
from tkinter import messagebox


raiz = tk.Tk()
raiz.config(width=300, height=300)


def infoAdicional():
    messagebox.showinfo(title='Procesador de Rodri', message='Aplicación creada por Rodri mientras aprende Python')

def avisoLicencia():
    messagebox.showwarning('Licencia', 'Producto bajo licencia GNU.')

def salirAplicacion():
    valor = messagebox.askquestion('Salir', 'Deseas salir de la aplicación?')
    if valor == 'yes':
        raiz.destroy()

def cerrarDocumento():
    valor = messagebox.askretrycancel('Reintentar', 'No es posible cerrar. Documento bloqueado.')
    if valor == True:
        raiz.destroy()

barraMenu = tk.Menu(raiz)
raiz.config(menu=barraMenu)

archivoMenu = tk.Menu(barraMenu, tearoff=False)
archivoMenu.add_command(label='Nuevo')
archivoMenu.add_separator()
archivoMenu.add_command(label='Guardar')
archivoMenu.add_command(label='Guardar como...')
archivoMenu.add_command(label='Cerrar', command=cerrarDocumento)
archivoMenu.add_separator()
archivoMenu.add_command(label='Salir', command=salirAplicacion)



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
ayudaMenu.add_command(label='Licencia', command=avisoLicencia)
ayudaMenu.add_separator()
ayudaMenu.add_command(label='Acerca de...', command=infoAdicional)

barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
barraMenu.add_cascade(label='Edición', menu=edicionMenu)
barraMenu.add_cascade(label='Herramientas', menu=herramientasMenu)
barraMenu.add_cascade(label='Ayuda', menu=ayudaMenu)

raiz.mainloop()
