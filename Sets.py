#Elegir de una lista de numeros, aquel diferente de los demas
numeros = []
c = 0

while c < 6:
    cant = int(input("Ingrese el numero"))
    c += 1
    numeros.append(cant)

def stray(arr):
    print(arr)
    x = set(arr) #Funcion set() nos devuelve solo 1 elemento de cada dado en la lista y su cantidad implicitamente.
    print(x)
    for i in x:
        print(i)
        print(x)
        print(arr.count(i))
        if arr.count(i) == 1:
            print(i)
            return (i)

print(stray(numeros))
