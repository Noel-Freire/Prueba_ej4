from clases import Fijo, Variable

def opcion1(diccionario):
    print("Introduce los datos del empleado: ")
    tipo = str(input("Tipo de empleado (fijo/temporal): "))
    nombre = str(input("Introduce el nombre: "))
    nif = str(input("Introduce el nif: "))
    fecha = str(input("Introduce la fecha de nacimiento (dd/mm/aaaa): "))
    if tipo == "fijo":
        sueldo = float(input("Introduce el sueldo base mensual: "))
        alta = float(input("Introduce el año de alta en la empresa: "))
        complemento = float(input("Introduce el complemento anual: "))
        if not nif in diccionario:
            diccionario[nif] = Fijo(nombre, fecha, sueldo, alta, complemento)
        else:
            print("El usuario ya está registrado")
    else:
        sueldo = float(input("Introduce el sueldo mensual: "))
        alta = str(input("Introduce la fecha de alta (dd/mm/aaaa): ")) 
        baja = str(input("Introduce la fecha de baja (dd/mm/aaaa): "))
        if not nif in diccionario:
            diccionario[nif] = Variable(nombre, fecha, sueldo, alta, baja)
        else:
            print("El usuario ya está registrado")
        
    return diccionario

def opcion2(diccionario):
    nif = str(input("Introduce el nif del empleado que quieres borrar: "))
    if nif in diccionario:
        del diccionario[nif]
    else:
        print("El nif no está guardado")

    return diccionario
    
def opcion3(diccionario):
    for nif in diccionario:
        print(nif," ",diccionario[nif].nombre, end =" - ")
        if isinstance(diccionario[nif],Fijo):
            print("fijo")
        else:
            print("temporal")

    if diccionario == {}: 
        print("No hay nadie contratado.")

def opcion4(diccionario):
    nif = str(input("Introduce el NIF del empleado: "))

    if nif in diccionario:
        print("Nombre:", diccionario[nif].nombre)
        print("NIF:", nif)
        print("Fecha nacimiento:", diccionario[nif].fecha_nacimiento)
        print("Tipo: empleado", end = " ")
        if isinstance(diccionario[nif], Fijo):
            print("fijo")
            print("Año de alta:", int(diccionario[nif].año_alta))
            print("Sueldo base:", int(diccionario[nif].sueldo_mensual))
            print("Complemento anual:", int(diccionario[nif].complemento_anual))
            print("Sueldo mensual:", int(diccionario[nif].sueldo_mensual))
        else:
            print("temporal")
            print("Sueldo mensual:", int(diccionario[nif].sueldo_mensual))
            print("Fecha de alta:", diccionario[nif].alta)
            print("Fecha de baja:", diccionario[nif].baja)

def opcion5(diccionario):
    mes = int(input("Introduce el mes de nacimiento (1-12): "))
    recuento = 0
    print("Están de cumpleaños: ")
    for nif in diccionario:
        lista = []
        lista = diccionario[nif].fecha_nacimiento.split("/")
        if int(lista[1]) == mes:
            print(f"{diccionario[nif].nombre}, {diccionario[nif].fecha_nacimiento}")
            recuento += 1

    if recuento == 0: 
        print("No hay nadie de cumpleaños\n")



def elegir_modo(opcion, diccionario):
    if opcion == 1:
        diccionario = opcion1(diccionario)
    elif opcion == 2:
        diccionario = opcion2(diccionario)
    elif opcion == 3:
        opcion3(diccionario)
    elif opcion == 4:
        opcion4(diccionario)
    elif opcion == 5:
        opcion5(diccionario)

def mostrar_menu():
    print("Menú de opciones\n")
    print("(1) Añadir empleado")
    print("(2) Borrar empleado")
    print("(3) Mostrar lista empleados")
    print("(4) Mostrar detalle de un empleado")
    print("(5) Mostrar empleados cumpleaños")
    print("(6) Terminar\n")
    opcion = int(input("Elige una opción:"))

    return opcion

if __name__ == "__main__":
    opcion = 0
    diccionario = {}
    while opcion != 6:
        opcion = mostrar_menu()
        elegir_modo(opcion, diccionario)