# Este codigo calcula el resultado mediante operaciones

import math # Para el redondeo
import pandas as pd #Lo necesito para el coso este parecido a un Struct, sepa si funcionan igual

# Declaracion de funciones

def soda(_invi) :
    return(math.ceil(_invi/2))

def agua(_invi) :
    return(_invi)

def papa(_invi) :
    return(math.ceil(_invi/3))

def pizza(_invi) :
    return(_invi*3)




max_invi = 10
data = []

# Llenando un conjunto de datos de entrenamiento con rango 1-10

for num_invi in range(0,max_invi):
    refrescos = soda(num_invi)
    botellas = agua(num_invi)
    papafrita = papa(num_invi)
    rebanadas = pizza(num_invi)

    data.append([num_invi, refrescos, botellas, papafrita, rebanadas]) #Esto va a ir agregando conjuntos de datos uno detras de otro, maso así ([],[],[])


# Asignando un conjunto de datos a una variable o clase diferente por columna (Traté de hacer un Struct)

df = pd.DataFrame(data, columns= ["num_invi", "refrescos", "aguas", "papas", "pizza"])

x_train = df[["num_invi"]].values # Conjunto de número de invitados

y_train = df[["refrescos", "aguas", "papas", "pizza"]].values # Conjunto de resultados por número de invitados

