import tkinter as tk

root = tk.Tk()

root.title('Ventana de prueba')
# Dado que el root se adapta al frame, no serían necesarios:
#root.resizable(height = True, width = False)
#root.geometry('500x300')
root.iconbitmap('042/green.ico')
root.config(bg='green')

menu = tk.Frame()
menu.config(height='20', bg='gray')
menu.pack(fill='x', expand=True)

frame = tk.Frame()
frame.config(bg='red')
frame.config(width='650', height='350')

# para darle un borde:
frame.config(relief='ridge', bd= 10)

frame.config(cursor='pirate')

# para poner el frame en un lugar determinado:
# frame.pack(side='right', anchor='s')

# para rellenar la ventana:
frame.pack(fill='y', expand=True)


B1 = tk.Button(root, text ="circle", relief=tk.RAISED,\
                         cursor="circle")
B2 = tk.Button(root, text ="plus", relief=tk.RAISED,\
                         cursor="plus")
B1.pack()
B2.pack()

root.mainloop()
