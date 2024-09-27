class Mantenimiento():
    def __init__(self, fecha, operario, importe):
        self.fecha = fecha
        self.operario = operario
        self.importe = importe

    def __str__(self):
        return f"ID: {self.id}, Operario: {self.operario}, Fecha: {self.fecha}, Importe: {self.importe}" 


class Correctivo(Mantenimiento):
    def __init__(self, operario, fecha, importe, horas_paradas, pago_tecnico):
        super().__init__(operario, fecha, importe)
        self.horas_paradas = horas_paradas
        self.pago_tecnico = pago_tecnico

    def __str__(self):
        return f"Operario: {self.operario}, Fecha: {self.fecha}, Importe: {self.importe}, horas_paradas: {self.horas_paradas}, pago_tecnico: {self.pago_tecnico}"

    def getImporte(self):
        return self.importe + self.pago_tecnico


class Preventivo(Mantenimiento):
    def __init__(self, operario, fecha, importe, resultado, importe_insumos):
        super().__init__(operario, fecha, importe)
        self.resultado = resultado
        self.importe_insumos = importe_insumos

    def __str__(self):
        return f"Operario: {self.operario}, Fecha: {self.fecha}, Importe: {self.importe}, resultado: {self.resultado}"

    def getImporte(self):
        return self.importe + self.importe_insumos 