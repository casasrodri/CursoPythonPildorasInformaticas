def divide():
    op1 = float(input("Ingresa un numero: "))
    op2 = float(input("Ingresa otro numero: "))
    
    print(f"La división es {str(op1/op2)}")

try: 
    divide()
except ZeroDivisionError:
    print("No se puede dividir por cero!")
except ValueError:
    print("No es un valor válido...")
except:
    print("Otras excepciones!")
finally:
    print("Esta linea se ejecuta sí o sí.")