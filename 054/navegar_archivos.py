import tkinter as tk
from tkinter import Button, filedialog

root = tk.Tk()

def abreFichero():
    fichero = filedialog.askopenfilename(
        title='Abrir',
        initialdir='D:/Rodri/SystemFolders/Descargas',
        filetypes=(
            ('Contiene CINCUENTA 😁', '50*'),
            ('Documentos de Rodri', '*.ddd'),
            ('Ficheros de texto', '*.txt')
        )
    )
    print(fichero)

tk.Button(root, text='Buscar un archivo', command=abreFichero).pack()
root.mainloop()
