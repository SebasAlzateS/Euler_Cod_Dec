#Ejercicio 2
#-------------------CIFRADO CESAR-------------
'''
SEBASTIÁN ALZATE
FERNANDO GARCIA
DANIELA SANCHEZ
'''

#Importación de libreria con funciones propias.
import functions2 as ft


print("Programa para codificar o decodificar un mensaje ")
print('-'*75)
print('Ingrese c para codificar o d para decodificar')

menu = ft.opciones('Digite su opción: ')
print('Por favor, ingrese un mensaje valido que solo contenga letras de a - Z.')

mensaje = ft.validar_entrada('Ingrese el mensaje (solo letras a-Z): ')
desplazamiento = ft.dato_entero_positivo('Ingrese el desplazamiento utilizado en el cifrado (número entero): ')


if menu == 0:
    respuesta = ft.cifrar(mensaje, desplazamiento)
    print('El mensaje codificado es: ',respuesta)
else:
    respuesta = ft.decodificar(mensaje, desplazamiento)
    print('El mensaje decodificado es: ',respuesta)


