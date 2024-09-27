from classes.Maquina import Maquina


def main():
    print("Hola mundo")
    maquina = Maquina()
    maquina.cantidadMantenimientosCaros()
    maquina.roturaMasLarga()
    maquina.sumaGastos()


if __name__ == "__main__":
    main()