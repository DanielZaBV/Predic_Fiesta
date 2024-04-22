import tensorflow as tf

# Crear un tensor constante
tensor = tf.constant([[1, 2], [3, 4]])

# Realizar una operación con TensorFlow
result = tf.reduce_sum(tensor)

print("Suma de los elementos del tensor:", result.numpy())
