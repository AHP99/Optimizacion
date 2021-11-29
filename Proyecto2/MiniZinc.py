from iteration_utilities import unique_everseen
from iteration_utilities import duplicates



from random import randint
#Se asume que se trabajara con Enteros


def creador(Nodos,n_regiones):
    regiones = []
    colindantes = []

    for i in range(Nodos):
            regiones.append(i)
            colindantes.append([])

    for i in range(Nodos): ##toda lista debe tener un minimo de un elemento y un maximo posible de n_regiones.
        n_colindantes = randint(1,n_regiones)
        print(n_colindantes)
        usados = []
        if(n_colindantes == 1):
            n_colindantes+=1
        for n in range(1,n_colindantes):
            candidato = randint(1, n_regiones)

            while candidato in usados:
                candidato = randint(1, n_regiones)

            colindantes[i].append(candidato)
            usados.append(candidato)
        colindantes[i].sort()
    print("Viejo Colindantes:")
    print(colindantes)
    return colindantes
        


def buscar (lista):
    repetidos = list(unique_everseen(duplicates(lista)))
    largo = len(repetidos)
    while largo > 0:
        for x in repetidos:
            pos_rep = lista.index(x)
            lista[pos_rep] = creador(1,n_regiones)[0]
        largo = len(list(unique_everseen(duplicates(lista))))                  
    return





Nodos = int(input("Cuantos nodos hay: ")) #Cantidad de nodos
n_regiones = int(input("Cuantas regiones hay: ")) # cantidad de regiones

colindantes = creador(Nodos,n_regiones)

buscar(colindantes)

print("Nuevo Colindantes:")
print(colindantes)