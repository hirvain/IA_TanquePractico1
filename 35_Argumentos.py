# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 02:08:01 2022

@author: Oscar Antonio García Avila  19310457
"""

#¿Cuántos argumentos se utilizan en cada una de estas llamadas?
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')   #4 Argumentos
colores('lila', 'negro', 'rojo')               #3 Argumentos
colores('rosa')                                #1 Argumento
colores('marrón', 'naranja')                   #2 Argumentos

#Completa el siguiente fragmento de código:
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('rojo', 'negro')


#Crea una función que realice la suma de cinco números utilizando solo *args.
#Debes imprimir el resultado en la consola. 
def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('Suma de los 5 numeros:', resultado)

suma(1, 2, 25, 3, 10)