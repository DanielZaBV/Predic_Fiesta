# Este codigo calcula el resultado mediante operaciones

import math


def soda(_invi) :
    return(math.ceil(_invi/2))

def agua(_invi) :
    return(_invi)

def papa(_invi) :
    return(math.ceil(_invi/3))

def pizza(_invi) :
    return(_invi*3)



print("Ingresa el número de invitados")
num_invi = int(input(int))


print(f"Refrescos: {soda(num_invi)}")
print(f"Botellas de agua: {agua(num_invi)}")
print(f"Bolsas de papas fritas: {papa(num_invi)}")
print(f"Rebanadas de pizza: {pizza(num_invi)}")