# Ejercicio 2: Modelar una computadora
# 
# En este archivo debés crear la clase Computadora siguiendo las consignas del README.
# Recordá:
# - Definir atributos relevantes en el constructor (__init__), con valores por defecto.
# - Implementar el método __str__ para mostrar la información esencial.
# - Instanciar al menos 3 computadoras con distintos valores.
# - Llevar la cuenta de computadoras creadas (usar variable de clase).
# - Implementar al menos 2 métodos de los sugeridos (updateOS, PM, addRAM, getCapacity).
# - Crear otra clase para un componente (ej: Disco, RAM, etc.) con su propio __init__, __str__ y al menos un método.
# 
# ¡No olvides probar todos los métodos y comentar tu criterio para los valores

class Memoria:

    dic_memorias = {}

    def __init__(self, nro_serie, tipo, capacidad_tot, capacidad_res):
        try:
            capacidad_tot = int(capacidad_tot)
            capacidad_res = int(capacidad_res)

            self.nro_serie = nro_serie
            self.tipo = tipo
            self.capacidad_tot = capacidad_tot
            self.capacidad_res = capacidad_res
            self.archivos = []

            if nro_serie not in Memoria.dic_memorias:
                    Memoria.dic_memorias[nro_serie] = {
                        "tipo": tipo,
                        "capacidad_tot": capacidad_tot,
                        "capacidad_res": capacidad_res,
                    }
        except:
            print(f'ERROR: No se cargó correctamente los datos de la memoria {nro_serie}')
    
    def __str__(self):
        return (f'|{self.nro_serie} - Tipo: {self.tipo} Capacidad Total: {self.capacidad_tot} Capacidad Restante: {self.capacidad_res}')
    
    def write():
        nro = int(input('Ingresar numero de serie de la memoria: '))
        nom = input('Ingresar nombre del archivo: ')
        tam = int(input('Ingresar tamaño del archivo (en GB): '))
        dif = Memoria.dic_memorias[nro]['capacidad_tot'] - tam

        if dif < 0 :
            print('No hay suficiente espacio en el disco')
            return

        Memoria.dic_memorias[nro]['capacidad_res'] = dif
        Computadora.dic_computadoras[nro]['memoria'] = dif
        print(f"Se ha cargado correctamente el archivo {nom}, memoria restante {dif}GB")
        Computadora.dic_computadoras[nro]['archivos'].append(nom)

    
    def get_capacidad(self):
        return (self.capacidad_tot)

class Computadora: 
    dic_computadoras = {}

    def __init__(self, nro_serie , marca , modelo, procesador, pantalla, ram, memoria, os = 'Desconocido',archivos = None):
        try:
            nro_serie = int(nro_serie)
            self.nro_serie = (nro_serie)
            self.marca = marca
            self.modelo = modelo
            self.procesador = procesador
            self.pantalla = pantalla
            self.ram = ram
            self.memoria = memoria
            self.os = os
            if archivos is None:
                archivos = []
            self.archivos = archivos

            if nro_serie not in Computadora.dic_computadoras:
                Computadora.dic_computadoras[nro_serie] = {
                    "marca": marca,
                    "modelo": modelo,
                    "procesador": procesador,
                    "pantalla": pantalla,
                    "ram": ram,
                    "memoria": memoria,
                    "os": os,
                    "archivos": archivos,
                }
        except:
            print(f'ERROR: No se cargó correctamente los datos de la computadora {nro_serie}')

    def __str__(self):
        return (f'| {self.nro_serie} - Marca: {self.marca} Modelo: {self.modelo} Procesador: {self.procesador} Pantalla: {self.pantalla} Ram: {self.ram} Memoria: {self.memoria.capacidad_tot} OS: {self.os}')
    
    def updateOS():
        comp = int(input(f'Indicar el numero de serie de la computadora: '))
        act_os = input(f'Indicar el nuevo OS la computadora: ')
        Computadora.dic_computadoras[comp]['os'] = act_os
        print(f"OS actualizado correctamente para la computadora {comp}")

    def addRam():
        comp = int(input(f'Indicar el numero de serie de la computadora: '))
        act_ram = Computadora.dic_computadoras[comp]['ram']
        ram_agg = int(input(f'Indicar la camntidad de GB de ram a agregar: '))
        tot = act_ram + ram_agg
        Computadora.dic_computadoras[comp]['ram'] = tot
        print(f"Ram agregada. Cantidad total {tot}")
    
    def getComputadoras():
        for nro_serie, datos in Computadora.dic_computadoras.items():
            print(f"\nComputadora {nro_serie}:")
            for clave, valor in datos.items():
                if isinstance(valor, Memoria):
                    print(f"  {clave}: {valor.capacidad_tot}")
                else:
                    print(f"  {clave}: {valor}")

mem1 = Memoria(1, 'HDD', 1000, 1000)
mem2 = Memoria(2, 'SSD', 120, 120)
mem3 = Memoria(3, 'SSD', 120, 120)     

com1 = Computadora(1,'Lenovo','ZenBook','I5',14,8,mem1,'Win 11')
com2 = Computadora(2,'Apple','MacBook','M3',14,1000,mem2)
com3 = Computadora(3,'HP','EliteBook','R7',17,120,mem3)



#Computadora.updateOS()
#Computadora.addRam()
Memoria.write()
Computadora.getComputadoras()
