# -*- coding: utf-8 -*-
"""RedNeuronalConvertirCaF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gy3gGLoevdLUJhyW05BE_7sWW4N01VNJ
"""

import tensorflow as tf #Libreria inteligencia artificial
import numpy as np #Libreria arreglos numericos

celsius = np.array ([-40 ,-10 ,0 ,8 ,15 ,22, 38],dtype=float)
fahrenheit = np.array([-40 ,14 ,32 ,46 ,59 ,72 , 100],dtype=float)

capa = tf.keras.layers.Dense(units=1,input_shape=[1]) #Capa de tipo densa usando Keras las capas densas tienen conexiones desde cada neurona hacia todas
modelo = tf.keras.Sequential([capa]) #Modelo keras de tipo secuencial

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1), #optimizador Adam permite a la red saber como ajustar los pesos y cesgos de forma eficiente
    loss ='mean_squared_error' #funcion de perdidad usar error cuadratico medio
)

print("Comenzando entrenamiento...")
historial = modelo.fit(celsius,fahrenheit,epochs=1000, verbose=False) #Entenamiento de modelo funcion fit #numero de vueltas epochs = 1000 #verbose=false no mostrar tanto texto al entrenar
print("Modelo entrenado")

import matplotlib.pyplot as plt #Funcion de perdida nos dice que tan mal estan los resultados en cada vuelta
plt.xlabel("# Epoca")
plt.ylabel("# Magnitud de perdida")
plt.plot(historial.history["loss"])

print("Probar red")
resultado = modelo.predict([12.0])
print("El resultado es: " + str(resultado) + " fahrenheit")

print("Variables internas del modelo") #Peso 1.79 #Cesgo 31.9
print (capa.get_weights())