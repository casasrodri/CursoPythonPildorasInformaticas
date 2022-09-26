import matematicas as mate 
    # Importar así requiere luego hacer referencia al módulo seguido de la función.

mate.sumar(44, 34)

from matematicas import restar
from matematicas import *  # Ojo con el rendimiento
    # Importar así permite usar las funciones sin hacer referencia al módulo
restar(545, 66) 