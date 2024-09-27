class Inmobiliaria:
    def __init__(self):
        self.inmuebles = []
        self.cargar_datos()

    def cargar_datos(self):
        archivo = open("../data/inmuebles.csv")

        for linea in archivo:
            linea = linea[:-1].split(",")
            # tipos = 1:Casa 2:Dpto
            tipo = int(linea[0])
            codigo = linea[1]
            nombre_propietario = linea[2]
            importe_base = float(linea[3])
            superficie = int(linea[4])
            if tipo == 1:
                cant_habitaciones = int(linea[5])
                has_pileta = int(linea[6])
                inmueble = Casa(codigo, nombre_propietario, superficie, importe_base, cant_habitaciones, has_pileta)
                self.inmuebles.append(inmueble)
            elif tipo == 2:
                importe_expensas = float(linea[5])
                nro_piso = int(linea[6])
                inmueble = Departamento(codigo, nombre_propietario, superficie, importe_base, importe_expensas,
                                        nro_piso)
                self.inmuebles.append(inmueble)

    def suma_alquiler(self):
        suma = 0

        for i in self.inmuebles:
            suma += i.importe_definitivo()

        return print(f"1) Suma de alquileres: ${suma}")

    def cant_casas_premium(self):
        cant_premium = 0
        for i in self.inmuebles:
            if isinstance(i, Casa) and i.superficie > 150 and i.cant_habitaciones > 2 and i.has_pileta == 1:
                cant_premium += 1

        return print(f"2) Cantidad de casas premium: {cant_premium}")

    def prop_alquiler_bajo(self):
        persona_alquiler_bajo = None

        # hacemos de pivot con el primer valor de mi colección de objetos
        valor_alquiler_mas_bajo = self.inmuebles[0].importe_definitivo()

        for i in self.inmuebles[1:]:
            importe = i.importe_definitivo()
            if importe < valor_alquiler_mas_bajo:
                valor_alquiler_mas_bajo = importe
                persona_alquiler_bajo = i.nombre_propietario

        if persona_alquiler_bajo is not None:
            return print(f"3) Propietario con el alquiler más bajo: {persona_alquiler_bajo}, ${valor_alquiler_mas_bajo}"
                         f"")
        else:
            return print("No se encontraron inmuebles.")


class Inmueble:
    def __init__(self, codigo, nombre_propietario, superficie, importe_base):
        self.codigo = codigo
        self.nombre_propietario = nombre_propietario
        self.superficie = superficie
        self.importe_base = importe_base


class Casa(Inmueble):
    def __init__(self, codigo, nombre_propietario, superficie, importe_base, cant_habitaciones, has_pileta):
        super().__init__(codigo, nombre_propietario, superficie, importe_base)
        self.cant_habitaciones = cant_habitaciones
        self.has_pileta = has_pileta

    def importe_definitivo(self):
        valor_adicional = 30000
        valor_pileta = 0
        if self.has_pileta == 1:
            valor_pileta = 100000

        return self.importe_base + valor_pileta + (valor_adicional * self.cant_habitaciones)


class Departamento(Inmueble):
    def __init__(self, codigo, nombre_propietario, superficie, importe_base, importe_expensas, nro_piso):
        super().__init__(codigo, nombre_propietario, superficie, importe_base)
        self.importe_expensas = importe_expensas
        self.nro_piso = nro_piso

    def importe_definitivo(self):
        valor_piso = 0
        if self.nro_piso < 3:
            valor_piso = 20000
        return self.importe_base + self.importe_expensas + valor_piso
