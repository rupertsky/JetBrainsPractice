file = open("C:\\Users\\cajas\\Documents\\Fechas.txt", "w")
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
counter = 2

for i in range(1, 31):
    file.write(f"{dias[counter]} {i} Junio-2022, ")
    counter += 1
    if counter > 6:
        counter = 0
print("¡Successful!")
file.close()
