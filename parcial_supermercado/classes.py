class Empresa():
    def __init__(self):
        self.sucursales = []
        self.cargarDatos()

    def cargarDatos(self):
        archivo = open("./sucursales.csv", "rt")
        
        for linea in archivo:
            linea = linea[:-1].split(",")
            tipo = int(linea[0])
            nro = linea[1]
            superficie = int(linea[2])
            facturacion = float(linea[3])
            adicional = float(linea[4])

            if tipo == 1:
                sucursal = Hiper(nro, superficie, facturacion, adicional)
                
            elif tipo == 2:
                sucursal = Super(nro, superficie, facturacion, adicional)

            else:
                sucursal = Mini(nro, superficie, facturacion, adicional)

            self.sucursales.append(sucursal)

        archivo.close()

    def sumaGanancia(self):
        ganancia = 0

        for sucursal in self.sucursales:
            ganancia += sucursal.getFacturacion()

        return print(f"Importe de ganancia: ${ganancia}")

    def localesNoRentables(self):
        noRentables = []

        for suc in self.sucursales:
            if isinstance(suc, Hiper) and suc.getRentabilidad() < 50:
                noRentables.append(suc)
            elif isinstance(suc, Mini) and suc.getRentabilidad() < 35:
                noRentables.append(suc)
            elif isinstance(suc, Super) and suc.getRentabilidad() < 40 and suc.tipoSucursal == 0:
                noRentables.append(suc)
            elif isinstance(suc, Super) and suc.getRentabilidad() < 45 and suc.tipoSucursal == 1:
                noRentables.append(suc)

        if noRentables:
            print("Sucursales no rentables:\n")
            for sucursal in noRentables:
                print(f"Nro. Sucursal: {sucursal.numero}, Rentabilidad: {sucursal.getRentabilidad()}%")
            print(f"Cantidad de locales no rentables: {len(noRentables)}")
        else:
            print("Todas las sucursales son rentables.")


    def localMasRentable(self):
        masRentable = None
        rentabilidad = 0

        for suc in self.sucursales:
            if rentabilidad < suc.getRentabilidad():
                rentabilidad = suc.getRentabilidad()
                masRentable = suc
        
        if rentabilidad != 0:
            print(f"Local más rentable: {masRentable.numero}, Tipo Sucursal: {type(masRentable).__name__}, Rentabilidad: {rentabilidad}%")
        else: 
            print(f"No hay local más rentable que otros")

    def __str__(self):
        return f"- Sucursales de empresa:\n" + "\n".join([str(s) for s in self.sucursales])


class Sucursal():
    def __init__(self, numero, superficie, facturacion):
        self.numero = numero
        self.superficie = superficie
        self.facturacion = facturacion

    def __str__(self):
        return f"|Numero: {self.numero}|Superficie: {self.superficie}|Facturación: {self.facturacion}"
    

class Hiper(Sucursal):
    def __init__(self, numero, superficie, facturacion, importeGanadoAlquileres):
        super().__init__(numero, superficie, facturacion)
        self.importeGanadoAlquileres = importeGanadoAlquileres

    def __str__(self):
        return f"|Tipo Hiper|{super().__str__()} |Importe Ganado: {self.importeGanadoAlquileres}"

    def getFacturacion(self):
        return self.facturacion + self.importeGanadoAlquileres
    
    def getRentabilidad(self):
        return (self.facturacion - self.importeGanadoAlquileres) / self.superficie

class Super(Sucursal):
    def __init__(self, numero, superficie, facturacion, tipoSucursal):
        super().__init__(numero, superficie, facturacion)
        self.tipoSucursal = tipoSucursal

    def __str__(self):
        return f"|Tipo Super|{super().__str__()}|Tipo Sucursal: {self.tipoSucursal}"

    def getFacturacion(self):
        return self.facturacion
    
    def getRentabilidad(self):
        return (self.facturacion) / self.superficie

class Mini(Sucursal):
    def __init__(self, numero, superficie, facturacion, importePagadoAlquileres):
        super().__init__(numero, superficie, facturacion)
        self.importePagadoAlquileres = importePagadoAlquileres

    def __str__(self):
        return f"|Tipo Mini|{super().__str__()}|Importe Pagado: {self.importePagadoAlquileres}"
    
    def getFacturacion(self):
        return self.facturacion - self.importePagadoAlquileres
    
    def getRentabilidad(self):
        return (self.facturacion - self.importePagadoAlquileres) / self.superficie