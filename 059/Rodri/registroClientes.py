import tkinter as tk
from tkinter import messagebox

raiz = tk.Tk()
raiz.title('Clientes')

# Menú
barraMenu = tk.Menu(raiz)
raiz.config(menu=barraMenu)


# Formulario

# Creo el frame que los contendrá
frameForm = tk.Frame(raiz, padx=5, pady=5)
frameForm.grid(row=0)

# Creo los labels
tk.Label(frameForm, text='ID:').grid(row=0, column=0, sticky='e', padx=5, pady=5)
tk.Label(frameForm, text='Nombre:').grid(row=1, column=0, sticky='e', padx=5, pady=5)
tk.Label(frameForm, text='Apellido:').grid(row=2, column=0, sticky='e', padx=5, pady=5)
tk.Label(frameForm, text='Password:').grid(row=3, column=0, sticky='e', padx=5, pady=5)
tk.Label(frameForm, text='Dirección:').grid(row=4, column=0, sticky='e', padx=5, pady=5)
tk.Label(frameForm, text='Observaciones:').grid(row=5, column=0, sticky='ne', padx=5, pady=5)

# Creo los campos a rellenar
atributos_cliente = {
    'id': tk.StringVar(),
    'nombre': tk.StringVar(),
    'apellido': tk.StringVar(),
    'password': tk.StringVar(),
    'direccion': tk.StringVar()
}

def leer_formulario():
    return {
        'id': atributos_cliente['id'].get(),
        'nombre': atributos_cliente['nombre'].get(),
        'apellido': atributos_cliente['apellido'].get(),
        'password': atributos_cliente['password'].get(),
        'direccion': atributos_cliente['direccion'].get(),
        'observaciones': entries['observaciones'].get("1.0","end-1c")
    }

entries = {
    'id': tk.Entry(frameForm, textvariable=atributos_cliente['id']),
    'nombre': tk.Entry(frameForm, textvariable=atributos_cliente['nombre']),
    'apellido': tk.Entry(frameForm, textvariable=atributos_cliente['apellido']),
    'password': tk.Entry(frameForm, textvariable=atributos_cliente['password']),
    'direccion': tk.Entry(frameForm, textvariable=atributos_cliente['direccion']),
    'observaciones': tk.Text(frameForm, width=15, height=5)
}

r = 0
config_gral = {"column":1, "sticky":'w', "padx":5, "pady":5}
for entry in entries.values():
    entry.grid(row=r, **config_gral)
    r += 1

# Agrego barra de desplazamiento
scrollVertical = tk.Scrollbar(frameForm, command=entries['observaciones'].yview)
scrollVertical.grid(row=5, column=2, sticky='nsew')

entries['observaciones'].config(yscrollcommand=scrollVertical.set)

# Agrego propiedad de password al entry
entries['password'].config(show='●')


# Creación de sub-menus
bbddMenu = tk.Menu(barraMenu, tearoff=False)
borrarMenu = tk.Menu(barraMenu, tearoff=False)
crudMenu = tk.Menu(barraMenu, tearoff=False)
ayudaMenu = tk.Menu(barraMenu, tearoff=False)

# Agrego cada sub-menu a la barra
barraMenu.add_cascade(label='BBDD', menu=bbddMenu)
barraMenu.add_cascade(label='Borrar', menu=borrarMenu)
barraMenu.add_cascade(label='CRUD', menu=crudMenu)
barraMenu.add_cascade(label='Ayuda', menu=ayudaMenu)

# Agrego opciones por menú
    # BBDD

def salirAplicacion():
    valor = messagebox.askquestion('Salir', 'Deseas salir de la aplicación?')
    if valor == 'yes':
        raiz.destroy()

import bbdd
database = None

def crear_conexion():
    global database
    database = bbdd.connect()

    messagebox.showinfo('Base de datos', 'Un éxito la conexión a la base de datos :D')

bbddMenu.add_command(label='Conectar', command=crear_conexion)
bbddMenu.add_command(label='Salir', command=salirAplicacion)

    # Borrar

def limpiar_formulario():
    for entry in atributos_cliente.values():
        entry.set('')

    entries['observaciones'].delete(1.0, tk.END)


borrarMenu.add_command(label='Limpiar formulario', command=limpiar_formulario)

    # CRUD

def control_conexion():
    if database == None:
        messagebox.showerror("Base de datos", "La aplicación no se ha conectado a la base de datos :(")

def create():
    control_conexion()
    id = bbdd.create(database, leer_formulario())
    atributos_cliente['id'].set(str(id))

def read():
    control_conexion()
    cursor = bbdd.read(database, leer_formulario()['id'])
    for row in cursor.fetchall():
        messagebox.showinfo('Información del cliente', row)

def update():
    pass

def delete():
    pass


crudMenu.add_command(label='Insertar', command=create)
crudMenu.add_command(label='Leer', command=read)
crudMenu.add_command(label='Actualizar', command=update)
crudMenu.add_command(label='Eliminar', command=delete)

    #Ayuda

ayudaMenu.add_command(label='Ayuda')
ayudaMenu.add_command(label='Acerca de...')



# Botonera
# Creo el frame que los contendrá
frameBotones = tk.Frame(raiz, padx=5, pady=5)
frameBotones.grid(row=1)


dimensiones = {'width': 6, 'height': 1, 'padx': 3}
padding = {'row': 0, 'padx': 3, 'pady': 5}
tk.Button(frameBotones, text='Create', command=create, **dimensiones).grid(column= 0, **padding)
tk.Button(frameBotones, text='Read', command=read, **dimensiones).grid(column= 1, **padding)
tk.Button(frameBotones, text='Update', command=update, **dimensiones).grid(column= 2, **padding)
tk.Button(frameBotones, text='Delete', command=delete, **dimensiones).grid(column= 3, **padding)


raiz.mainloop()
