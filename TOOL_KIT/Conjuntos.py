'''Se realizara operaciones de 3 conjuntos (A, B ,C ) con una cardinaldiad e 10 elementos, los conjutnos seran de caracter
alfanumerico

dentro de un conjunto los valores no se puenden repetir por lo que solo se imprimira un solo elemento'''


#funciones Esenciales del programa
from ntpath import join
from os import sep
import re

def UNION(conjunto1,conjunto2,conjunto3):
    operacion  = input("Ingresa la operacion a realizar: ")
    parentesis =  re.findall(r'\(.*?\)', operacion)#PRIMERO ENCONTRAMOS UN POSIBLE ARGUMENTO EN PARENTESIS PARA RESOLVERLO
    contParentesis =0
    print("\n\tPROCESO\n===================")
    print("\nParentesis de la operacion: \t",parentesis)#Se borrara, es para la comprobacion del dato

    operacion = operacion.replace(" ","") #Quitamos los espacios dentro de la operacion
    operacion = operacion.split(sep='-') #Transformamos a lista y separamos los argumentos en este caso identificamos si hay 2 argumentos
    for dato in operacion:
        if len(dato) > 1:
            indice  = operacion.index(dato)
            del operacion[indice] #Solo dejamos la variable a comparar con el parentesis
    print("Numero de conjunto a comparar con el parentesis: \t",operacion)
    
    #En el caso de encontrar un parentesis se realiza lo siguiente
    if len(parentesis) >= 1: 
        parentesis = "".join(parentesis) #REHACEMOS UNA CADENA PARA QUITAR LOS PARENTESIS Y REALIZAR LA OPERACION
        parentesis = parentesis.replace("(","")
        parentesis = parentesis.replace(")","")
        parentesis = parentesis.split(sep=' ') #SEPARAMOS LOS ARGUMENTOS DENTRO DEL PARENTESIS
        
        print('Valores dentro del parentesis a comparar: \t',parentesis)

        #Transformacion de valores dentro del parentesis 1 = conjunto1
        try:
            dato1 = parentesis.index("1") #Capturamos el indice de la variable para cambiar su valor por el conjunto anteriormente proporcionado
            parentesis[dato1] = conjunto1 #Teniendo el indice remplazamos el indice por el conjunto existente
        except:
            pass
        try:
            dato2 = parentesis.index("2")
            parentesis[dato2] = conjunto2
        except:
            pass
        try:
            dato3 = parentesis.index("3")
            parentesis[dato3] = conjunto3
        except:
            pass

            #union en parentesis
        if "|" in parentesis[:]:
            indiceEliminar = parentesis.index('|')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] | parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')
            
            #interseccion en parentesis
        elif "&" in parentesis[:]:
            indiceEliminar = parentesis.index('&')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] & parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')

            #Diferencia en parentesis
        elif "~" in parentesis[:]:
            indiceEliminar = parentesis.index('~')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] - parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')
        
            #Simetrica en parentesis
        elif "^" in parentesis[:]:
            indiceEliminar = parentesis.index('^')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] ^ parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')

        contParentesis += 1 #En el caso de haber un parentesis este contador nos ayudara a saber realizar la union final

    #REALIZAMOS LA UNION DE TODO 
    
    #Damos el valor del conjunto dentro de la lista (operacion), 1 = conjunto1
    try:
        dato1 = operacion.index("1") #Capturamos el indice de la variable para cambiar su valor por el conjunto anteriormente proporcionado
        operacion[dato1] = conjunto1
    except:
        pass
    try:
        dato2 = operacion.index("2")
        operacion[dato2] = conjunto2
    except:
        pass
    try:
        dato3 = operacion.index("3")
        operacion[dato3] = conjunto3
    except:
        pass



    if contParentesis == 1: #EN el caso de haber un parentesis realiza la union final entre valor individual y el resultado del parentesis
        try:
            union_final = operacion[0] | subUnion
            print('\n\nUnion Resultante: ',union_final)
        except:
            print('\n<><><><><><><><><><>\n\tFalta de argumentos por evaluar\n<><><><><><><><><><>')
    elif contParentesis == 0: #No hay parentesis, entonces busca un posible segundo valor dentro de la lista principal
        try:
            union_final = operacion[0] | operacion[1]
            print('\n\nUnion Resultante: ',union_final)
        except:
            print('\n<><><><><><><><><><>\n\tFalta de argumentos por evaluar\n<><><><><><><><><><>')


def INTERSECCION(conjunto1,conjunto2,conjunto3):
    
    operacion  = input("Ingresa la operacion a realizar: ")
    parentesis =  re.findall(r'\(.*?\)', operacion)#PRIMERO ENCONTRAMOS UN POSIBLE ARGUMENTO EN PARENTESIS PARA RESOLVERLO
    contParentesis =0
    print("\n\tPROCESO\n===================")
    print("\nParentesis de la operacion: \t",parentesis)#Se borrara, es para la comprobacion del dato

    operacion = operacion.replace(" ","") #Quitamos los espacios dentro de la operacion
    operacion = operacion.split(sep='-') #Transformamos a lista y separamos los argumentos en este caso identificamos si hay 2 argumentos
    for dato in operacion:
        if len(dato) > 1:
            indice  = operacion.index(dato)
            del operacion[indice] #Solo dejamos la variable a comparar con el parentesis
    print("Numero de conjunto a comparar con el parentesis: \t",operacion)
    
    #En el caso de encontrar un parentesis se realiza lo siguiente
    if len(parentesis) >= 1: 
        parentesis = "".join(parentesis) #REHACEMOS UNA CADENA PARA QUITAR LOS PARENTESIS Y REALIZAR LA OPERACION
        parentesis = parentesis.replace("(","")
        parentesis = parentesis.replace(")","")
        parentesis = parentesis.split(sep=' ') #SEPARAMOS LOS ARGUMENTOS DENTRO DEL PARENTESIS
        
        print('Valores dentro del parentesis a comparar: \t',parentesis)

        #Transformacion de valores dentro del parentesis 1 = conjunto1
        try:
            dato1 = parentesis.index("1") #Capturamos el indice de la variable para cambiar su valor por el conjunto anteriormente proporcionado
            parentesis[dato1] = conjunto1 #Teniendo el indice remplazamos el indice por el conjunto existente
        except:
            pass
        try:
            dato2 = parentesis.index("2")
            parentesis[dato2] = conjunto2
        except:
            pass
        try:
            dato3 = parentesis.index("3")
            parentesis[dato3] = conjunto3
        except:
            pass

            #union en parentesis
        if "|" in parentesis[:]:
            indiceEliminar = parentesis.index('|')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] | parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')
            
            #interseccion en parentesis
        elif "&" in parentesis[:]:
            indiceEliminar = parentesis.index('&')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] & parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')

            #Diferencia en parentesis
        elif "~" in parentesis[:]:
            indiceEliminar = parentesis.index('~')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] - parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')
        
            #Simetrica en parentesis
        elif "^" in parentesis[:]:
            indiceEliminar = parentesis.index('^')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] ^ parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')

        contParentesis += 1 #En el caso de haber un parentesis este contador nos ayudara a saber realizar la union final

    #REALIZAMOS LA UNION DE TODO 
    
    #Damos el valor del conjunto dentro de la lista (operacion), 1 = conjunto1
    try:
        dato1 = operacion.index("1") #Capturamos el indice de la variable para cambiar su valor por el conjunto anteriormente proporcionado
        operacion[dato1] = conjunto1
    except:
        pass
    try:
        dato2 = operacion.index("2")
        operacion[dato2] = conjunto2
    except:
        pass
    try:
        dato3 = operacion.index("3")
        operacion[dato3] = conjunto3
    except:
        pass



    if contParentesis == 1: #EN el caso de haber un parentesis realiza la union final entre valor individual y el resultado del parentesis
        try:
            union_final = operacion[0] & subUnion
            print('\n\nUnion Resultante: ',union_final)
        except:
            print('\n<><><><><><><><><><>\n\tFalta de argumentos por evaluar\n<><><><><><><><><><>')
    elif contParentesis == 0: #No hay parentesis, entonces busca un posible segundo valor dentro de la lista principal
        try:
            union_final = operacion[0] & operacion[1]
            print('\n\nUnion Resultante: ',union_final)
        except:
            print('\n<><><><><><><><><><>\n\tFalta de argumentos por evaluar\n<><><><><><><><><><>')


def DIFERENCIA(conjunto1,conjunto2,conjunto3):
        
    operacion  = input("Ingresa la operacion a realizar: ")
    parentesis =  re.findall(r'\(.*?\)', operacion)#PRIMERO ENCONTRAMOS UN POSIBLE ARGUMENTO EN PARENTESIS PARA RESOLVERLO
    contParentesis =0
    print("\n\tPROCESO\n===================")
    print("\nParentesis de la operacion: \t",parentesis)#Se borrara, es para la comprobacion del dato

    operacion = operacion.replace(" ","") #Quitamos los espacios dentro de la operacion
    operacion = operacion.split(sep='-') #Transformamos a lista y separamos los argumentos en este caso identificamos si hay 2 argumentos
    for dato in operacion:
        if len(dato) > 1:
            indice  = operacion.index(dato)
            del operacion[indice] #Solo dejamos la variable a comparar con el parentesis
    print("Numero de conjunto a comparar con el parentesis: \t",operacion)
    
    #En el caso de encontrar un parentesis se realiza lo siguiente
    if len(parentesis) >= 1: 
        parentesis = "".join(parentesis) #REHACEMOS UNA CADENA PARA QUITAR LOS PARENTESIS Y REALIZAR LA OPERACION
        parentesis = parentesis.replace("(","")
        parentesis = parentesis.replace(")","")
        parentesis = parentesis.split(sep=' ') #SEPARAMOS LOS ARGUMENTOS DENTRO DEL PARENTESIS
        
        print('Valores dentro del parentesis a comparar: \t',parentesis)

        #Transformacion de valores dentro del parentesis 1 = conjunto1
        try:
            dato1 = parentesis.index("1") #Capturamos el indice de la variable para cambiar su valor por el conjunto anteriormente proporcionado
            parentesis[dato1] = conjunto1 #Teniendo el indice remplazamos el indice por el conjunto existente
        except:
            pass
        try:
            dato2 = parentesis.index("2")
            parentesis[dato2] = conjunto2
        except:
            pass
        try:
            dato3 = parentesis.index("3")
            parentesis[dato3] = conjunto3
        except:
            pass

            #union en parentesis
        if "|" in parentesis[:]:
            indiceEliminar = parentesis.index('|')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] | parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')
            
            #interseccion en parentesis
        elif "&" in parentesis[:]:
            indiceEliminar = parentesis.index('&')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] & parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')

            #Diferencia en parentesis
        elif "~" in parentesis[:]:
            indiceEliminar = parentesis.index('~')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] - parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')
        
            #Simetrica en parentesis
        elif "^" in parentesis[:]:
            indiceEliminar = parentesis.index('^')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] ^ parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')

        contParentesis += 1 #En el caso de haber un parentesis este contador nos ayudara a saber realizar la union final

    #REALIZAMOS LA UNION DE TODO 
    
    #Damos el valor del conjunto dentro de la lista (operacion), 1 = conjunto1
    try:
        dato1 = operacion.index("1") #Capturamos el indice de la variable para cambiar su valor por el conjunto anteriormente proporcionado
        operacion[dato1] = conjunto1
    except:
        pass
    try:
        dato2 = operacion.index("2")
        operacion[dato2] = conjunto2
    except:
        pass
    try:
        dato3 = operacion.index("3")
        operacion[dato3] = conjunto3
    except:
        pass



    if contParentesis == 1: #EN el caso de haber un parentesis realiza la union final entre valor individual y el resultado del parentesis
        try:
            union_final = operacion[0] - subUnion
            print('\n\nUnion Resultante: ',union_final)
        except:
            print('\n<><><><><><><><><><>\n\tFalta de argumentos por evaluar\n<><><><><><><><><><>')
    elif contParentesis == 0: #No hay parentesis, entonces busca un posible segundo valor dentro de la lista principal
        try:
            union_final = operacion[0] - operacion[1]
            print('\n\nUnion Resultante: ',union_final)
        except:
            print('\n<><><><><><><><><><>\n\tFalta de argumentos por evaluar\n<><><><><><><><><><>')


def SIMETRICA(conjunto1,conjunto2,conjunto3):
        
    operacion  = input("Ingresa la operacion a realizar: ")
    parentesis =  re.findall(r'\(.*?\)', operacion)#PRIMERO ENCONTRAMOS UN POSIBLE ARGUMENTO EN PARENTESIS PARA RESOLVERLO
    contParentesis =0
    print("\n\tPROCESO\n===================")
    print("\nParentesis de la operacion: \t",parentesis)#Se borrara, es para la comprobacion del dato

    operacion = operacion.replace(" ","") #Quitamos los espacios dentro de la operacion
    operacion = operacion.split(sep='-') #Transformamos a lista y separamos los argumentos en este caso identificamos si hay 2 argumentos
    for dato in operacion:
        if len(dato) > 1:
            indice  = operacion.index(dato)
            del operacion[indice] #Solo dejamos la variable a comparar con el parentesis
    print("Numero de conjunto a comparar con el parentesis: \t",operacion)
    
    #En el caso de encontrar un parentesis se realiza lo siguiente
    if len(parentesis) >= 1: 
        parentesis = "".join(parentesis) #REHACEMOS UNA CADENA PARA QUITAR LOS PARENTESIS Y REALIZAR LA OPERACION
        parentesis = parentesis.replace("(","")
        parentesis = parentesis.replace(")","")
        parentesis = parentesis.split(sep=' ') #SEPARAMOS LOS ARGUMENTOS DENTRO DEL PARENTESIS
        
        print('Valores dentro del parentesis a comparar: \t',parentesis)

        #Transformacion de valores dentro del parentesis 1 = conjunto1
        try:
            dato1 = parentesis.index("1") #Capturamos el indice de la variable para cambiar su valor por el conjunto anteriormente proporcionado
            parentesis[dato1] = conjunto1 #Teniendo el indice remplazamos el indice por el conjunto existente
        except:
            pass
        try:
            dato2 = parentesis.index("2")
            parentesis[dato2] = conjunto2
        except:
            pass
        try:
            dato3 = parentesis.index("3")
            parentesis[dato3] = conjunto3
        except:
            pass

            #union en parentesis
        if "|" in parentesis[:]:
            indiceEliminar = parentesis.index('|')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] | parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')
            
            #interseccion en parentesis
        elif "&" in parentesis[:]:
            indiceEliminar = parentesis.index('&')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] & parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')

            #Diferencia en parentesis
        elif "~" in parentesis[:]:
            indiceEliminar = parentesis.index('~')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] - parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')
        
            #Simetrica en parentesis
        elif "^" in parentesis[:]:
            indiceEliminar = parentesis.index('^')
            parentesis.pop(indiceEliminar) #Dejamos solo las variables a evaluar
            print("Conjuntos a evaluar dentro del parentesis: \t",parentesis)

            subUnion = parentesis[0] ^ parentesis[1] #nuevo valor para el parentesis resultado de la su evaluacion resultando un nuevo subconjunto
            print(f'\n*** Valor entre parentesis = {subUnion} ***\n===================')

        contParentesis += 1 #En el caso de haber un parentesis este contador nos ayudara a saber realizar la union final

    #REALIZAMOS LA UNION DE TODO 
    
    #Damos el valor del conjunto dentro de la lista (operacion), 1 = conjunto1
    try:
        dato1 = operacion.index("1") #Capturamos el indice de la variable para cambiar su valor por el conjunto anteriormente proporcionado
        operacion[dato1] = conjunto1
    except:
        pass
    try:
        dato2 = operacion.index("2")
        operacion[dato2] = conjunto2
    except:
        pass
    try:
        dato3 = operacion.index("3")
        operacion[dato3] = conjunto3
    except:
        pass



    if contParentesis == 1: #EN el caso de haber un parentesis realiza la union final entre valor individual y el resultado del parentesis
        try:
            union_final = operacion[0] ^ subUnion
            print('\n\nUnion Resultante: ',union_final)
        except:
            print('\n<><><><><><><><><><>\n\tFalta de argumentos por evaluar\n<><><><><><><><><><>')
    elif contParentesis == 0: #No hay parentesis, entonces busca un posible segundo valor dentro de la lista principal
        try:
            union_final = operacion[0] ^ operacion[1]
            print('\n\nUnion Resultante: ',union_final)
        except:
            print('\n<><><><><><><><><><>\n\tFalta de argumentos por evaluar\n<><><><><><><><><><>')



def conjuntos():
    #Variables para capturar los conjuntos
    cardinalidad  =0
    conjuntoEscrito1 = ""
    conjuntoEscrito2 = ""
    conjuntoEscrito3 = ""
    conjuntoLista1 = ""
    conjuntoLista2 = ""
    conjuntoLista3 = ""

    conjuntoEscrito1 = input('\nIntroduce los valores del conjunto 1 separados por (,): ')
    conjuntoEscrito2  = input('Introduce los valores del conjunto 2 separados por (,): ')
    conjuntoEscrito3  = input('Introduce los valores del conjunto 3 separados por (,): ')
    conjuntoLista1 = conjuntoEscrito1.split(sep=',') #Realizamos la separacion de datos mediante el uso de comas y se transforma a lista
    conjuntoLista2 = conjuntoEscrito2.split(sep=',')
    conjuntoLista3 = conjuntoEscrito3.split(sep=',')

    #DECLARACION DE LOS CONJUNTOS PASANDO LOS VALORES DE LAS LISTAS DONDE ESTOS VALORES SI ESTAN REPETIDOS YA NO SE REPITEN
    conjunto1 = set(conjuntoLista1)
    conjunto2 = set(conjuntoLista2)
    conjunto3 = set(conjuntoLista3)

    #Se checara en relacion a conjunto1,2,3, que los arreglos no exceda los 10 cardinales solicitados
    #Un conjunto en python permite que no se repita el mismo elemento dentro del conjunto
    if (len(conjunto1) <= 10 and len(conjunto1) > 0) and (len(conjunto2) <= 10 and len(conjunto2) > 0) and (len(conjunto3) <= 10 and len(conjunto3) > 0):
        print('\nTodos los conjuntos son validos')
    else:
        print('\nUno de los conjuntos no es valido :)')

    #impresion para verificar los conjuntos
    print(f'\nDatos del conjunto 1: {conjunto1}\nDatos del conjunto 2: {conjunto2}\nDatos del conjunto 3: {conjunto3}\n\n')

    print(F"""
    CARDINALIDAD DE LOS CONJUNTOS
    CONJUNTO 1: {len(conjunto1)}
    CONJUNTO 2: {len(conjunto2)}
    CONJUNTO 3: {len(conjunto3)}""")
    #Pedimos al usuario que opcion desea realizar
    print("""
    INGRESA LA OPCION QUE DESEAS REALIZAR:

    # # # # # # # # #

    1)UNION 
    2)INTERSECCION
    3)DIFERENCIA
    4)SIMETRICA

    # # # # # # # # #""")
    opcion = int(input('OPCION: '))

    print("""
    SYNTAXIS PARA EL PROGRAMA:

    ===================================================
    |          Union = | = ALT+124                    |
    |          Interseccion = & = ALT+38              |
    |          Diferencia = ~ = ALT+45                |
    |          Diferencia Simetrica = ^ = ALT+94      |                                 
    |                                                 |
    |       Ingresa el argumento del conjunto         |
    |   y el otro argumento del conjunto separandolo  |
    |           por un guion (-).                     |
    |                                                 |
    |              EJEMPLO: 1 - (2 | 3)               |
    ===================================================""")

    if opcion == 1:
        UNION(conjunto1,conjunto2,conjunto3)
    elif opcion == 2:
        INTERSECCION(conjunto1,conjunto2,conjunto3)
    elif opcion == 3:
        DIFERENCIA(conjunto1,conjunto2,conjunto3)
    elif opcion == 4:
        SIMETRICA(conjunto1,conjunto2,conjunto3)


