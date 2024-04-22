import tensorflow as tf
import calculador as clc # Importando mi calculador.py con alias clc

# Creando el modelo

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(8, activation = 'relu', input_shape = (1,)),
    tf.keras.layers.Dense(4)
])

model.compile(
    optimizer = 'adam',
    loss = 'mse'
)

model.fit(clc.x_train, clc.y_train, epochs = 10)