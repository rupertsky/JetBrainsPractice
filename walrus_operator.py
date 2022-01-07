#La funcion del operador walrus ":=" es asignar una variable a un valor predeterminado solo cuando una condicion se da#
#E.g sin walrus
a = [0 for _ in range(5)]
if len(a) > 3:
    print(f"El tamaño {len(a)} no es valido")
#E.g con walrus
x = [0 for _ in range(5)]
if (n := len(x)) > 3:
    print(f"El tamaño {n} no es valido")
else:
    print(f"El tamaño {n} es valido")