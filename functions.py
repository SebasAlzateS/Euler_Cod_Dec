def edo_euler(edo_input, x0, y0, h, n):
    
    '''
    Resuelve EDO de primer orden utilizando el método de euler
    
    Recibe los siguientes parámetros: 
    edo_input = Entrada de texto donde se indica la EDO (string)
    x0 = valor inicial de x (float)
    y0 = valor inicial de y (float)
    h = tamaño del paso (float))
    n = numero de pasos (Entero)
    
    Imprime resultado de las iteraciones - numeros de pasos
    '''
    #Inicializar variables
    x = x0      
    y = y0  
     
    #Titulo
    print('Iteracion','x','y',sep=('  '*15))  
    print('-'*75)   
    print('0',x0,y0,sep=('  '*15))
    
    #Ciclo For que se repite numero de pasos (debe ser entero)
    for i in range(n): 
        
        y = round(y + float(h) *eval(edo_input),4) #Sumar el valor de y0 con tamaño de paso y redondearlo a 4 decimales
        x = round(x + float(h),4)   #Sumar el valor de x0 con tamaño de paso y redondearlo a 4 decimales
      
        print(i+1, x, y, sep=('  ' * 15), end='\n') #Mostrar cada variable, separarlo 15 espacios y salto de linea


def dato_numerico(enunciado):
    '''
    Recibe el enunciado, lo muestra como un input y retorna dato siempre y cuando no se ingresen letras. 
    
    Retorna: Dato flotante
    '''
    while True:
        dato = input(enunciado)         #Muestra el enunciado y el usuario digita.
        if dato.isalpha():              #Si el dato ingresado tiene letras , no deja seguir.
            print("Entrada no válida - Solo se permiten ingresar numeros.") 
        else:
            break
    return float(dato)


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


def validar_entrada():
    '''
    Valida que el usuario solo ingrese la edo en términos de x y y 
    '''
    caracteres = "xy0123456789+-*/() "    # Caracteres permitidos
    
    # Ciclo que obliga a que se ingrese lo pedido
    while True:
        edo_input = str(input("Ingrese la EDO en términos de x y y (por ejemplo: y - x**1 + 1): "))
        
        entrada_valida = True  # Suponemos que la entrada es válida al principio
        
        for char in edo_input:      #Recorre caracter por caracter 
            if char not in caracteres:  # Si aparece un caracter no valido, se pone en falso, rompe for, se va al print e inicia el while de nuevo
                entrada_valida = False
                break
        
        if entrada_valida:
            break
        else:
            print("Entrada no válida")
        
    return(edo_input)

def dato_numerico2(enunciado):
    '''
    Recibe el enunciado, lo muestra como un input y retorna dato siempre y cuando no se ingresen letras. 
    
    Retorna: Dato flotante

    También descarta caracteres especiales, por ejemplo, ',' ' ' '/' '*' '.' entre otros
    '''
    dato = input(enunciado)
    while dato.isdigit() != True:
        print('El dato que ingresó no es válido')
        dato = input(enunciado)        
    return float(dato)
