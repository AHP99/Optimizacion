from random import randint
#Se asume que se trabajara con Enteros

n = int(input("Cantidad de productos: ")) #Cantidad de productos
Cantrequerimientos = int(input("Cantidad de requisitos: ")) # cantidad de requisitos

#Limites para la generacion de los parametros
requerimientos_inf=int(input("Limite Inferior de los requerimientos: "))
requerimientos_sup=int(input("Limite Superior de los requerimientos: "))

Disponibilidad_inf=int(input("Limite Inferior de la Disponibilidad: "))
Disponibilidad_sup=int(input("Limite Superior de la Disponibilidad: "))

Utilidad_inf=int(input("Limite Inferior de la Utilidad: "))
Utilidad_sup=int(input("Limite Superior de la Utilidad: "))

#Generacion Aletoria de parametros
requerimientos = []
Utilidad = []
Disponibilidad = []

print("\n>>>Problema generado<<<\n")

for i in range(n):
    requerimientos_i=[]

    for x in range(Cantrequerimientos):
        valor = randint(requerimientos_inf,requerimientos_sup)
        requerimientos_i.append(valor)
    requerimientos.append(requerimientos_i)

    ValorUtilidad  = randint(Utilidad_inf, Utilidad_sup)
    Utilidad.append(ValorUtilidad)

    print("producto " + str(i+1) + ":", requerimientos_i)

for j in range(Cantrequerimientos):
    ValorDisponibilidad  = randint(Disponibilidad_inf, Disponibilidad_sup)
    Disponibilidad.append(ValorDisponibilidad)
    

#Generar Modelo Lindo
fo = "max "
for i in range(n):
    fo += str(Utilidad[i]) + 'x' + str(i+1)
    if i < n-1:
        fo+=" + "
    else:
        fo+="\n"
fo+="\n"
#Reestricciones
Rest = "st\n"
for i in range(Cantrequerimientos):
    for j in range(n):
        Rest += str(requerimientos[j][i]) + 'x' + str(j+1)
        if j < n-1:
            Rest+=" + "
    Rest += " <= "
    Rest += str(Disponibilidad[i]) + "\n"

Rest += "\n"
for i in range(n):
    Rest += "x" + str(i+1) + " >= 0\n"
#Crear Archivo
archivo = open("Modelo.ltx","w")
archivo.write(fo)
archivo.write(Rest)
archivo.close()
