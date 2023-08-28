def opciones(mensaje):
    '''
    Recibe: el enunciado string (str), luego deja ingresar opcion al usuario, la opcion debe ser "c" o "d".
    
    Retorna: dato entero
    '''
    while True:
        menu = input(mensaje).lower() #El usuario ingresa la opcion, y se convierte a letras minuscula
        caracteres = 'cd'           #Caracteres permitidos
        entrada_valida = True       #Bandera: Se inicializa en verdadero
        
        for char in menu:       #Recorre posicion por posicion, lo ingresado por el usuario    
            if char not in caracteres:  #Si no existe el caracter "c" o "d" en ninguna posicion
                entrada_valida = False   #Cambia el estado a falso
                break                 #Rompe el ciclo for
         
        
        
        if entrada_valida:      #Si entrada_valida = True ; verificar si se ingresó la letra "c" o "d"
            if menu == 'c':
                menu = 0       #Si ingresa c , guardar 0 
                break 
            
            elif menu == 'd':
                menu = 1        #Si ingresa d, gurdar 1
                break 
            else:
                print("Entrada no permitida")   #Si ingresa mas de una c, d o combinadas.
                
        else:
            print("Entrada no permitida")   #Si entrada_valida = False
            
    return int(menu)


def validar_entrada(mensaje):
    '''
    Valida que el usuario solo ingrese letras del alfabeto (inglés)
    '''
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"    # Caracteres permitidos
    
    # Ciclo que obliga a que se ingrese lo pedido
    while True:
        
        alfabeto = input(mensaje)
        entrada_valida = True  # Suponemos que la entrada es válida al principio
        
        for char in alfabeto:
            if char not in caracteres:  # Si aparece un caracter no valido, se pone en falso, rompe for, se va al print e inicia el while de nuevo
                entrada_valida = False
                break
        
        if entrada_valida:
            break
        else:
            print("Entrada no válida")
        
    return(alfabeto)


def dato_entero_positivo(enunciado):
    '''
    Recibe el enunciado, lo muestra como un input y retorna dato siempre y cuando sea entero positivo (solo posea números positivos)

    Retorna: Dato Entero
    '''
    while True:
        dato = input(enunciado)
        if dato.isdigit():  # Utilizamos isdigit() para verificar si el dato está compuesto solo por dígitos
            if int(dato) >= 0:  # Verificamos si el número es positivo o igual a cero
                break
            else:
                print("Entrada no válida - Solo se permiten ingresar números enteros positivos.")
        else:
            print("Entrada no válida - Solo se permiten ingresar números enteros positivos.")
    return int(dato)



def cifrar(mensaje, desplazamiento):
    '''
    Recibe mensaje y desplazamiento deseado
    '''
    resultado = ""          #Se crea un STR donde se almacenará el resultado
    for char in mensaje:    #Recorre mensaje caracter por caracter
        if char.isalpha():  #Si el mensaje contiene letras
            codigo_ascii = ord(char)    #Ascii actual
            
            if char.islower():  #Saber si el caracter actual esta en minuscula
                base = ord('a') #Si es minuscula la base será a
            else:
                base = ord('A') #Si es mayuscula la base será A
            
            codificado = (codigo_ascii - base + desplazamiento) %26 + base
            resultado += chr(codificado)
        
    return resultado
            
def decodificar(mensaje, desplazamiento):
    '''
    Recibe mensaje y desplazamiento deseado
    '''
    resultado = ""          #Se crea un STR donde se almacenará el resultado
    for char in mensaje:    #Recorre mensaje caracter por caracter
        if char.isalpha():  #Si el mensaje contiene letras
            codigo_ascii = ord(char)    #Ascii actual
            
            if char.islower():  #Saber si el caracter actual esta en minuscula
                base = ord('a') #Si es minuscula la base será a
            else:
                base = ord('A') #Si es mayuscula la base será A
            
            codificado = (codigo_ascii - base - desplazamiento) %26 + base
            resultado += chr(codificado)
        
    return resultado        
        
