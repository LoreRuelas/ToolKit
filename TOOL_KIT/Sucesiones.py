
# Variable global
formula = ''
limiteInferior = 0
limiteSuperior = 0


def sumatoria(superior: int, inferior: int): #función usada para crear objetos funciones definidas por el usuario, este caso el inferior y superior son enteros
    if superior < inferior: #en caso de que los limites sean iguales
        return 0
    else:
        try: # Este try es en caso de que la funcion recursiva pueda causar una indeterminacion en el denominador, evitamos el problema. Ejemplo: 1/0
            valor = {'n': int(superior)} #  definimos los valores que se van a sustituir, en este caso solo es "n"
            valor = eval(formula, valor) # el eval se encargará de evaluar el string y lo sustituira por las variables que se le pasen en el segundo 
            #parámetro, a lo que ingrese el usuario eval, encargado de evaluar la fórmula y reemplazar los valores que le pasamos
            print('{}. = {}'.format(superior, valor))
            return valor + sumatoria(int(superior - 1), int(inferior))# regresa el valor mas la sumatoria que es el superior menos 1 y el inferior 
        except:
            return 0


def mainSucesiones(): # Funcion main para luego integrarlo al toolkit principal
    global limiteInferior,limiteSuperior,formula # Datos a modificar para realizar las operaciones

    print('''
                DAME LOS SIGUIENTES VALORES COMO SE TE PIDAN
    1)limite inferior            2)limite superior            3)formula(n)
    ''') #orden el que se le pide al usuaruo que se ingresen los datos
    limiteInferior = int(input('1) : ')) # Ingresar limite inferior
    limiteSuperior = int(input('2) : ')) # Ingresar limite Superior 
    formula = input('3) : ') # Ingresar la formula en terminos de n

    resultado = sumatoria(limiteSuperior, limiteInferior) # Se pasa los parametros a la funcion de la sucesion y se captura en resultado
    print('Resultado de la sumatoria: ', resultado) #se imprimirá el resultado de la fórmula con los limites asignados

#mainSucesiones() # main principal

