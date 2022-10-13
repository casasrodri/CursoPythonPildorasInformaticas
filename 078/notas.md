1. Primero instalar pyinstaller:
    `pip install pyinstaller`
2. Desplazarse al directorio: `cd carpeta`
3. Ejecutar:
`pyinstaller practicaCalculadora.py`
4. Luego buscar el ejecutable dentro de la carpeta *dist*.

De esa forma, se muestra la ventana de comandos por detras y todos los archivos tienen que estar acompañando el .exe.

Si queres sin consola detrás:
`pyinstaller --windowed practicaCalculadora.py`

Si queres que sea un unico archivo (sin necesidad de tener instalado python en esa pc):
`pyinstaller --windowed --onefile practicaCalculadora.py`

Si ademas agregar tu propio icono, hacer esto:
`pyinstaller --windowed --onefile --icon=logo.ico practicaCalculadora.py`