import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root, width=500, height=400)
frame.pack()

label = tk.Label(frame, text="Hola a todos, esto es un label de texto...")
#label.pack()

label.place(x=100, y=200)

# Otra forma
param = {
    'text':     'Mi nombre es Lucca 🐶', 
    'fg':       'blue',
    'font':     ('Comic Sans MS', 20)
}
tk.Label(frame, param).place(x=150, y=250)

# Importar imagen (png o gif, sino usar otro formato)
img = tk.PhotoImage(file='044/yorkie.png')
tk.Label(root, image=img).place(x=0, y=0)

root.mainloop()