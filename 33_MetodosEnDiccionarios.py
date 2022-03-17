# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 01:58:51 2022

@author: Oscar Antonio García Avila  19310457
"""
#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'. Muestra la última clave ('Modelo') que queda en la consola.

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1
del teclado2['Categoría']
del teclado2['Precio']
print(teclado2['Modelo'])
print(teclado2)