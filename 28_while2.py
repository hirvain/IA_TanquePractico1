# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 01:35:07 2022

@author: Oscar Antonio García Avila  19310457
"""

x = 0

while x <= 30:
	x += 1  
	if x == 4 or x == 6 or x == 10:
		print('Se saltó el valor ', x, ' de x')
		continue
	if x == 15:
		print('Se rompió la ejecución del bucle cuando x valía: ', x)
		break
	print(x)