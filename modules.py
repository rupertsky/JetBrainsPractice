#Named with prev suffix "_script"
"""__main__ pattern
# safe_module.py

name = "George"

if __name__ == "__main__":
    print("Hello,", name)

The name of the module is always available in the built-in variable __name__.
When you are executing a script __name__ has a value "__main__".
So here we check the value of __name__ and print the line only if the module is executed as a script.

# safe_bye.py script

from safe_module import name

print("Bye,", name)
The output is the following:
Bye, George

In general, if you have more than just one line to execute in a script
it's convenient to move all that code into a function called main and then call it like that:

# safe_main_module.py

name = "George"

def main():
    print("Hello,", name)

if __name__ == "__main__":
    main()

Note, that the naming itself doesn't affect the way a function is executed,
it's just a convention to indicate that this function is run only when the file is used like a script.

    """

import csv


def archivo(doc):

    with open(doc, encoding="utf-8") as arch_csv:
        next(arch_csv)
        reader = csv.DictReader(arch_csv)
        data = []
        for i in arch_csv:
            i = i.rstrip('\n')
            row = i.split('|')
            codigo = row[0]
            nombre = row[1]
            region = row[2]
            anio = str(row[3])
            co_2 = str(row[4])
            per_capita = str(row[5])
            data.append({
                'cod_pais': codigo,
                'nom_pais': nombre,
                'region': region,
                'anio': anio,
                'co2': co_2,
                'co2_percapita': per_capita
            })
    return data


def main(x):
    paises = archivo(x)
    for i in paises:
        codigopais = i['cod_pais']
        nombrepais = i['nom_pais']
        region = i['region']
        anio = i['anio']
        cO2 = i['co2']
        capita = i['co2_percapita']
        print(f"Codigo de pais: {codigopais}, Nombre del pais: {nombrepais}, Region: {region}, Año: {anio}"
              f"CO2 (kt): {cO2}, CO2 per capita (toneladas metricas): {capita} ")

main('Emisiones_CO2.csv')

"""
if __name__ == "__main__":
    nom_archivo = 'Emisiones_CO2.csv'
    main(nom_archivo)
"""