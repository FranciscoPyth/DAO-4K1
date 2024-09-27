from classes.Mantenimiento import *


class Maquina():
    def __init__(self):
        self.mantenimientos = []
        self.cargarDatos()

    def __str__(self):
        return f"Mantenimientos: {self.mantenimientos}"
    
    def cargarDatos(self):        
        archivo = open("./parcial_mantenimiento/data/mantenimientos.csv", "rt")

        for linea in archivo:
            linea = linea[:-1].split(",")
            tipo = int(linea[0])
            fecha = linea[1]
            operario = linea[2]
            importe = float(linea[3])

            if tipo == 1:
                resultado = int(linea[4])
                insumos = float(linea[5])
                mantenimiento = Preventivo(operario, fecha, importe, resultado, insumos)
            else:
                horas_parada = float(linea[4])
                pago_tecnico = float(linea[5])
                mantenimiento = Correctivo(operario, fecha, importe, horas_parada, pago_tecnico)

            self.mantenimientos.append(mantenimiento)


        archivo.close()


    def sumaGastos(self):
        suma = 0

        for m in self.mantenimientos:
            suma += m.getImporte()

        return print(f"La suma de los gastos es: {suma}")

    def cantidadMantenimientosCaros(self):
        cantidadTotal = 0

        for m in self.mantenimientos:
            if m.getImporte() > 10000:
                cantidadTotal += 1

        return print(f'La cantidad de mantenimientos que superan los $10.000 son: {cantidadTotal}')

    def roturaMasLarga(self):
        roturaMayor = 0
        operario = None
        fecha = None

        for m in self.mantenimientos:
            if isinstance(m, Correctivo):
                if roturaMayor < m.horas_paradas:
                    roturaMayor = m.horas_paradas
                    operario = m.operario
                    fecha = m.fecha

        if roturaMayor != 0:
            return print(f'Fecha: {fecha}, Operario: {operario}')
        else:
            return print('No existe operario con mayor cantidad de horas')