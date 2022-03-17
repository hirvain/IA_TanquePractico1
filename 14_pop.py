# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 00:44:08 2022

@author: Oscar Antonio García Avila  19310457
"""

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print("Lista original: ")
print(colores)
color1 = colores.pop(1)
color2 = colores.pop(7)
colores_guardados = [color1, color2]
print("Despues de pop: ")
print(colores)
print("Colores eliminados: ")
print(colores_guardados)

