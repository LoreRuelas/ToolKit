## Simbolos Aceptados
simbolosAceptados = ["V","~","ꓥ",">","-"]
## Letras Aceptadas
letrasAceptadas = ["p","q","r","s","t"]
## Lista de la proposición separada por partes
listaBase = []

def tablasV():

    # Listas que necesitaremos a lo largo del programa
    global simbolosAceptados
    global letrasAceptadas
    global listaBase

    # Pide frase
    print (simbolosAceptados, " ", letrasAceptadas)
    frase = PedirEnunciado()

    # Comprueba que el enunciado se válido
    while ComprobarNombre(frase) == False:
        frase = PedirEnunciado()
        ComprobarNombre(frase)

    # Separa los carácteres de la proposición en elementos de una lista
    listaBase = SepararEnLista(listaBase, frase)

    # Calcula columnas, filas y numero de letras
    columnas = CalculaColumnas(listaBase)
    numLetras = CalcularLetras(listaBase, letrasAceptadas)
    filas = CalculaFilas(numLetras)

    # Crea una matriz en base a la lista que contiene los elementos del enunciado
    matrizBase = ValoresLetras(listaBase,filas, columnas)

    # LLena los campos de las premisas con su valor correspondiente
    llenaLetras(listaBase, matrizBase, filas,letrasAceptadas)

    # Hace la evaluación de las premisas segun los operadores
    evaluaOper(listaBase, filas, matrizBase, simbolosAceptados)

    # Muestra la matriz
    Mostrar(matrizBase,listaBase)


def evaluaOper(lista, num_filas, matrizProceso,simbolos):
    ## Column inicialia en 0 cada que entra a evaluar un nuevo comando ya que necesita empezar a evaluar el enunciado dsd el inicio
    ## Column va aumentando en 1 -> asi itera en las diferentes columnas

    # 1) Evalúa negaciones
    column = 0
    for oper in lista:
        if oper in simbolos:
            if oper == "~":
                # En base a la que tiene a su derecha hace la negación
                EvaluaNegacion(column + 1, column, num_filas, matrizProceso)
        column = column + 1      

    # 2) Evalúa conjunciones
    column = 0
    for oper in lista:
        if oper in simbolos:
            if oper == "ꓥ":
                # Define las columnas(premisas) a evaluar, la de la derecha e izquierda del operador
                izquierda = column - 1
                derecha = column + 1
                # Si tiene negación antes de la premisa que va a evaluar, entonces evalúa la columna de la negación de esa premisa
                if ( column > 1 and lista[izquierda -1] == "~" ) :
                    izquierda = column -2
                if ( lista[derecha] == "~" ) :
                    derecha = column +1 # tiene que ser el mismo por que la negacion va primero que el param
                EvaluaAnd(izquierda, derecha, column, num_filas, matrizProceso)
        column = column + 1

    # 3) Evalúa disyunciones
    column = 0
    for oper in lista:
        if oper in simbolos:
            if oper == "V":
                # Define las columnas(premisas) a evaluar, la de la derecha e izquierda del operador
                izquierda = column - 1
                derecha = column + 1
                 # Si tiene negación antes de la premisa que va a evaluar, entonces evalúa la columna de la negación de esa premisa
                if ( column > 1 and lista[izquierda -1] == "~" ) :
                    izquierda = column -2
                if ( lista[derecha] == "~" ) :
                    derecha = column +1 # tiene que ser el mismo por que la negacion va primero que el param
                EvaluaOr(izquierda, derecha, column, num_filas, matrizProceso)
        column = column + 1

    # 4) Evalúa condicionales
    column = 0
    for oper in lista:
        if oper in simbolos:
            if oper == ">":
                # Define las columnas(premisas) a evaluar, la de la derecha e izquierda del operador
                izquierda = column - 1
                derecha = column + 1
                 # Si tiene negación antes de la premisa que va a evaluar, entonces evalúa la columna de la negación de esa premisa
                if ( column > 1 and lista[izquierda -1] == "~" ) :
                    izquierda = column -2
                if ( lista[derecha] == "~" ) :
                    derecha = column +1 # tiene que ser el mismo por que la negacion va primero que el param
                EvaluaUni(izquierda, derecha, column, num_filas, matrizProceso)
        column = column + 1
    
    # 5) Evalúa bicondicionales
    column = 0
    for oper in lista:
        if oper in simbolos:
            if oper == "-":
                # Define las columnas(premisas) a evaluar, la de la derecha e izquierda del operador
                izquierda = column - 1
                derecha = column + 1
                 # Si tiene negación antes de la premisa que va a evaluar, entonces evalúa la columna de la negación de esa premisa
                if ( column > 1 and lista[izquierda -1] == "~" ) :
                    izquierda = column -2
                if ( lista[derecha] == "~" ) :
                    derecha = column +1 # tiene que ser el mismo por que la negacion va primero que el param
                EvaluaBicon(izquierda, derecha, column, num_filas, matrizProceso)
        column = column + 1

def EvaluaBicon(columnaIzq, columnaDer, columnaEval, num_filas, matrizProceso):
    for i in range(num_filas):
        # V - V = V
        if matrizProceso[i][columnaIzq] == "V" and matrizProceso[i][columnaDer] == "V" :
            matrizProceso[i][columnaEval] = "V"
        # V - F = V
        elif matrizProceso[i][columnaIzq] == "V" and matrizProceso[i][columnaDer] == "F" :
            matrizProceso[i][columnaEval] = "F"
        # F - V = F
        elif matrizProceso[i][columnaIzq] == "F" and matrizProceso[i][columnaDer] == "V" :
            matrizProceso[i][columnaEval] = "F"
        # F - F = F
        else :
            matrizProceso[i][columnaEval] = "V"         

def EvaluaUni(columnaIzq, columnaDer, columnaEval, num_filas, matrizToProcess):
    for i in range(num_filas):
        # V > V = V
        if matrizToProcess[i][columnaIzq] == "V" and matrizToProcess[i][columnaDer] == "V" :
            matrizToProcess[i][columnaEval] = "V"
        # V > F = F
        elif matrizToProcess[i][columnaIzq] == "V" and matrizToProcess[i][columnaDer] == "F" :
            matrizToProcess[i][columnaEval] = "F"
        # F > V = V
        elif matrizToProcess[i][columnaIzq] == "F" and matrizToProcess[i][columnaDer] == "V" :
            matrizToProcess[i][columnaEval] = "V"
        # F > F = F
        else :
            matrizToProcess[i][columnaEval] = "V"  



def EvaluaNegacion(sourceColumn, targetColumn, num_filas, matrizToProcess):
    for i in range(num_filas):
        # ~V -> F
        if matrizToProcess[i][sourceColumn] == "V" :
            matrizToProcess[i][targetColumn] = "F"
        # ~F -> V
        else :
            matrizToProcess[i][targetColumn] = "V"
            
def EvaluaOr(sourceColumn1, sourceColumn2, targetColumn, num_filas, matrizToProcess):
    for i in range(num_filas):
        # V V V -> V
        if matrizToProcess[i][sourceColumn1] == "V" and matrizToProcess[i][sourceColumn2] == "V" :
            matrizToProcess[i][targetColumn] = "V"
        # V V F -> V
        elif matrizToProcess[i][sourceColumn1] == "V" and matrizToProcess[i][sourceColumn2] == "F" :
            matrizToProcess[i][targetColumn] = "V"
        # F V V -> V
        elif matrizToProcess[i][sourceColumn1] == "F" and matrizToProcess[i][sourceColumn2] == "V" :
            matrizToProcess[i][targetColumn] = "V"
        # F V F -> F
        else :
            matrizToProcess[i][targetColumn] = "F"            

def EvaluaAnd(sourceColumn1, sourceColumn2, targetColumn, num_filas, matrizToProcess):
    for i in range(num_filas):
        # V ꓥ V -> V
        if matrizToProcess[i][sourceColumn1] == "V" and matrizToProcess[i][sourceColumn2] == "V" :
            matrizToProcess[i][targetColumn] = "V"
        # V ꓥ F -> F
        elif matrizToProcess[i][sourceColumn1] == "V" and matrizToProcess[i][sourceColumn2] == "F" :
            matrizToProcess[i][targetColumn] = "F"
        # F ꓥ V -> F
        elif matrizToProcess[i][sourceColumn1] == "F" and matrizToProcess[i][sourceColumn2] == "V" :
            matrizToProcess[i][targetColumn] = "F"
        # F ꓥ F -> F
        else :
            matrizToProcess[i][targetColumn] = "F" 

def llenaLetras(lista, matrizProceso, num_filas,letrasAceptadas):
    level = 0
    column = 0
    procesadasDict = {} # Diccionario para guardar las premisas (sirve para cuando esten repetidas)
    for oper in lista:
        if oper in letrasAceptadas:
            if oper in procesadasDict :
                repeatedLevel = procesadasDict.get(oper) # get(oper) nos da el valor de la "key" para asi identificar qué vamos a repetir
                # Si la premisa está repetida le "indica" al método FillColumnPorNivel que repita lo de esa premisa
                FillColumnPorNivel(column, repeatedLevel, matrizProceso, num_filas)
            else :
                FillColumnPorNivel(column, level, matrizProceso, num_filas)
                # Si la premisa no es repetida la llena y ya
                procesadasDict[oper] = level
            level = level + 1
        column = column + 1

                
def FillColumnPorNivel(column, nivel, matriz,num_filas):
    # Fórmula para calcular repetición y orden de V & F es: 2**(#premisa - 1) 
    loopCnt = 0 # Se inicializa en 1 porque Premisa1 -> (2**0) -> V F V F...
    repeticion = (2 ** (nivel)) # Nivel es el número de premisas que tenemos - 1
    for i in range(0,num_filas, repeticion): 
        # A los pares son V porque las repeticiones son multiplos de 2
        if loopCnt % 2 == 0:
            for j in range(repeticion):
                matriz[i + j][column] = "V"
        else :
        # A los impares son F porque son los "restantes"
            for j in range(repeticion):
                matriz[i + j][column] = "F"
        loopCnt = loopCnt + 1

            
def Mostrar(matriz,lista):
    # Muestra el enunciado(lista), dsp la matriz(tabla de verdad) en formato de cuadrícula o tabla
    print("La tabla de verdad es la siguiente:\n", lista)
    for i in matriz:
        print(i)

def ValoresLetras(listaBase,filas,columnas):
    matrizBase = []
    # En base a las filas y columnas crea una matriz con todos los campos correspondientes
    for i in range (filas):
        matrizBase.append([0 for _ in range(columnas)])  # CAMBIAR
        
    return matrizBase

def CalcularLetras(listaBase, letrasAceptadas):
    contadorLetras = 0
    # Checa cuantas variables hay para asi generar un número correcto de filas
    for item in listaBase:
        if item in letrasAceptadas:
            contadorLetras = contadorLetras + 1
    return contadorLetras

def CalculaColumnas(listaBase):
    # Número de columnas es el número de carácteres en nuestra premisa
    columnas = len(listaBase)
    return columnas

def CalculaFilas(numLetras):
    # Número de filas es 2 elevado al número de premisas 
    filas = (2 ** numLetras)
    return filas

def SepararEnLista(listaBase, frase):
    # Mete cada carácter de la frase en una lista
    for i in (frase):
        listaBase.append(i)
    return listaBase
    

def PedirEnunciado():
    print ("Los operadores aceptados son los siguientes:\n V (disyunción)\n ~ (negación)\n ꓥ (conjunción)\n > (condicional)\n - (bicondicional) ")
    print ("\nLas premisas aceptadas son las siguientes:\n p\n q\n r\n s\n t\n")
    print ("**Recomendación: puede copiar los operadores del texto anterior si no los encuentra en el teclado\n")
    frase = input("INGRESE EL ENUNCIADO A EVALUAR: ")
    # Quita espacios para facilitar su uso
    frase = frase.replace(" ", "")
    #print (frase)
    return frase

def ComprobarNombre(frase):
    global simbolosAceptados
    global letrasAceptadas
    # Checa si cada carácter de la frase(enunciado) está en los elementos válidos
    for i in range (len(frase)):
        if (frase[i] not in simbolosAceptados) and (frase[i] not in letrasAceptadas):
            return False
    # Al regresar True está indicando que terminó de checar la frase y que no necesita volverla a pedir
    return True

