class Empleado:
    def __init__(self, nombre, fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

class Variable(Empleado):
    def __init__(self, nombre, fecha_nacimiento, sueldo_mensual, alta, baja):
        super().__init__( nombre, fecha_nacimiento)
        self.alta = alta
        self.baja = baja
        self.sueldo_mensual = sueldo_mensual

class Fijo(Empleado):
    def __init__(self, nombre, fecha_nacimiento, sueldo_mensual, año_alta, complemento_anual):
        super().__init__(nombre, fecha_nacimiento)
        self.año_alta = año_alta
        self.complemento_anual = complemento_anual
        self.sueldo_mensual = sueldo_mensual+(2025-año_alta)*complemento_anual