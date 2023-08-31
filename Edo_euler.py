#Ejercicio 1
#-------------------EDO PRIMER ORDEN POR EL MÉTODO DE EULER CON TAMAÑO Y NUMERO DE PASOS-------------
'''
SEBASTIÁN ALZATE
FERNANDO GARCIA
DANIELA SANCHEZ
'''

#Importación de libreria con funciones propias.
import functions as ft

print("Solución de una Ecuación Diferencial Ordinaria mediante el Método de Euler")
x0 = ft.dato_numerico("Ingrese el valor inicial de x (x0): ")
y0=ft.dato_numerico("Ingrese el valor inicla de y (y0): ")
h=ft.dato_numerico( "Ingrese el tamaño del paso (h): ")
n=ft.dato_entero_positivo( "Ingrese el número de pasos (n): ")
edo_input = ft.validar_entrada()

resultado = ft.edo_euler(edo_input, x0, y0, h, n)
