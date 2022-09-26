# Creación de paquetes distribuibles

1. Crear el archivo `setup.py` con la escrtura de ejemplo
2. Desde consola ejecutar `python setup.py sdist`
3. En la carpeta ./dist se encuentra el archivo distribuible con extensión `.tar.gz`
4. Para instalar, se debe ejecutar la siguiente instrucción: `pip install .\<paquete.tar.gz>`
5. Una vez instalado, ya se encuentra disponible para importarlos desde cualquier ruta.
