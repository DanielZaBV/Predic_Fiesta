import tensorflow as tf
import calculador as clc # Importando mi calculador.py con alias clc
import numpy as np

# Creando el modelo

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(8, activation = 'relu', input_shape = (1,)),
    tf.keras.layers.Dense(4)
])

model.compile(
    optimizer = 'adam',
    loss = 'mse'
)

# Entrenamiento

model.fit(clc.x_train, clc.y_train, epochs = 1000)

print("Ingresa el número de invitados:")
num_invi_ing = int(input()) # Número de invitados para el cual hacer predicciones

num_input = np.array([[num_invi_ing]]) # Afuerza tuve que hacer esto, espero ya jale

# Predicción

prediccion = model.predict(num_input)  # Predicción para el nuevo caso

print("Predicciones para el número de invitados:", num_invi_ing)
print("Refrescos:", round(prediccion[0][0]))
print("Botellas de agua:", round(prediccion[0][1]))
print("Papas fritas:", round(prediccion[0][2]))
print("Rebanadas de pizza:", round(prediccion[0][3]))
