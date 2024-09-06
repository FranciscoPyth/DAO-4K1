import pandas as pd
from classes.Persona import Persona
from classes.Cuenta import Cuenta


def main():
    df_personas = pd.read_csv("data/personas.csv")
    cuenta = None
    personas = []

    for i, row in df_personas.iterrows():
        persona = Persona(row["nombre"], row["edad"], row["dni"])
        personas.append(persona)

    for i in range(len(personas)):
        print(f'Persona {i}: {personas[i]}')

    if personas[0].esMayorDeEdad():
        cuenta = Cuenta(personas[0], 1000)

    print(f'\nSaldo en cuenta: ${cuenta.saldo}')

    
if __name__ == "__main__":
    main()