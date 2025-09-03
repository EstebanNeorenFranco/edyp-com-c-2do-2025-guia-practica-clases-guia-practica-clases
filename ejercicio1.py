# A - Indicá qué devuelven las siguientes expresiones. Analizalo con tus compañeros y luego ejecutá las instrucciones en la máquina para comprobar tu respuesta.

# class Camion:
#     def __init__(self, patente, marca, carga, anio): #supuse que había un error al cargar las variables así que lo modifiqué
#         self.patente = patente
#         self.marca = marca
#         self.carga = carga
#         self.anio = anio

#     def __str__(self):
#         return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"

# furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
# furgon2 = furgon1
# furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
# furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

# print(furgon1 == furgon2) 
# Da True porque solo compara identidad sin tener en cuenta el estado en memoria

# print(furgon1 is furgon2) 
# Da True porque son el mismo objeto en memoria

# print(furgon3 == furgon4) 
# Da False porque compara identidad sin tener en cuenta el estado en memoria y estos son diferentes

# print(furgon3 is furgon4) 
# Da False porque compara si son el mismo espacio en memoria y estos son diferentes

# print(furgon1 == furgon4) 
# Da Fasle porque son diferentes objetos en memoria, falta el metodo __eq__ para compararlos correctamente

### B - Modificá el código dado para que la comparación de dos objetos de la clase Camion devuelva True cuando 
### todos sus atributos sean iguales.

# class Camion:
#     def __init__(self, patente, marca, carga, anio): #supuse que había un error al cargar las variables así que lo modifiqué
#         self.patente = patente
#         self.marca = marca
#         self.carga = carga
#         self.anio = anio
    
#     def __eq__(self, other):
#         if isinstance(other, Camion):
#             return (self.patente == other.patente and
#                     self.marca == other.marca and
#                     self.carga == other.carga and
#                     self.anio == other.anio)

#     def __str__(self):
#         return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"

# furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
# furgon2 = furgon1
# furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
# furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

# print(furgon1 == furgon4) 

### C - ¿Qué atributo hace único a nuestros objetos? Identificá el atributo que hace único al objeto Camion y 
### modificá el código para que la comparación de dos objetos de la clase Camion devuelva True cuando ese atributo sea igual.

# El atributo que hace diferente al resto es patente

# class Camion:
#     def __init__(self, patente, marca, carga, anio): #supuse que había un error al cargar las variables así que lo modifiqué
#         self.patente = patente
#         self.marca = marca
#         self.carga = carga
#         self.anio = anio
    
#     def __eq__(self, other):
#         if isinstance(other, Camion):
#             return (self.patente == other.patente)

#     def __str__(self):
#         return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"

# furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
# furgon2 = furgon1
# furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
# furgon4 = Camion("ABC123", "VW", 1000, 2020)

# print(furgon1 == furgon4) 

### D - Si dos personas tienen el mismo DNI, entonces... ¡Son la misma persona! ¿Cómo evitarías asignar el mismo DNI 
### a dos personas distintas? Siguiendo esta analogía, adaptá el código anterior para el caso de los camiones.

# class Camion:
#     lista_patentes = set()

#     def __init__(self, patente, marca, carga, anio): #supuse que había un error al cargar las variables así que lo modifiqué
#         if patente in Camion.lista_patentes:
#             raise ValueError(f'Error: La patente asignada ya está en uso')
#         self.patente = patente
#         self.marca = marca
#         self.carga = carga
#         self.anio = anio
#         Camion.lista_patentes.add(patente)
  
#     def __eq__(self, other):
#         if isinstance(other, Camion):
#             return (self.patente == other.patente)

#     def __str__(self):
#         return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"

# furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
# furgon4 = Camion("ABC123", "VW", 1000, 2020)

### F - Creá un pequeño menú que te permita:

### Registrar un nuevo camión.
### Modificar la carga de un camión.
### Mostrar por terminal la lista de camiones registrados, del más antiguo al más moderno.
### Mostrar por terminal la marca que más veces fue registrada.

class Camion:
    dic_camiones = {}
    lista_patentes = set()    

    def __init__(self, patente, marca, carga, anio):
        self.patente = patente
        self.marca = marca
        self.carga = carga
        self.anio = anio
  
    def __eq__(self, other):
        if isinstance(other, Camion):
            return (self.patente == other.patente)

    def __str__(self):
        return f"{self.patente} | Carga: {self.carga} Marca: {self.marca} Año: {self.anio}"

    def mostrar_camiones():
        print('Lista de los camiones:')
        for c in sorted(Camion.dic_camiones.values(), key=lambda x: x.anio):
            print(c)
        
    def add_camiones():
        patente = input('Indicar patente: ')
        if patente in Camion.lista_patentes:
            raise ValueError(f'Error: La patente asignada ya está en uso')
        marca = input('Indicar marca: ')
        carga = int(input('Indicar carga: '))
        anio = int(input('Indicar año: '))

        nuevo = Camion(patente, marca, carga, anio)
        Camion.dic_camiones[patente] = nuevo
        Camion.lista_patentes.add(patente)
       
        return ('Nuevo camion agregado')
    
    def modificar_carga():
        patente = input("Ingrese la patente del camión: ")
        if patente in Camion.dic_camiones:
            nueva_carga = int(input('Indica nueva carga'))
            Camion.dic_camiones[patente].carga = nueva_carga
            print(f"Carga modificada para el camión {patente}.")
    
    def top_marca_registrada():
        marcas = []
        for i in Camion.dic_camiones.values():
            if i.marca not in marcas:
                marcas.append(i.marca[0])
        max = 0
        marca_max = ''
        for m in marcas:
            cant = marcas.count(m)
            if cant > max:
                max = cant
                marca_max = m
        
        print('La marca con más unidades es: ',marca_max)
        
def menu():
    while True:
        print("\n--- MENÚ CAMIONES ---")
        print("1. Registrar nuevo camión")
        print("2. Modificar carga de un camión")
        print("3. Mostrar lista de camiones")
        print("4. Mostrar marca más registrada")
        print("5. Salir")

        opcion = int(input("\nSeleccione una opción: "))

        if opcion == 1:
            ret = Camion.add_camiones()
            print(ret)

        if opcion == 3:
            Camion.mostrar_camiones()

        if opcion == 2:
            Camion.modificar_carga()

        if opcion == 4:
            Camion.top_marca_registrada()
            
        if opcion == 5:
            break
            
menu()