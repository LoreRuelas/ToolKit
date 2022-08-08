from unicodedata import digit

def IngresoNumPar():

    # Ingresa el # de parejas ya que esto facilitará la revisión de sintaxis
    numPar = input("Ingrese el número de parejas ordenadas de enteros que desee: ")
    while numPar.isnumeric() == False:
        numPar = input("\nIngrese el número de parejas ordenadas de enteros que desee: ")

    return int(numPar)


def PideRelacion():

    # Ingresa las parejas ordenadas, si existe una x o y con más de un carácter la separa como un solo elemento
    resList = []
    sub_number = ''
    print ( "\n - Ejemplo de sintaxis requerida: (1,1),(2,2),(3,3),(1,2)")
    completeList = (input("Ingrese las parejas de enteros ordenadas: "))
    
    for c in completeList: #iterate over data char by char

        #Si detecta que el siguiente es una número entonces va metiendo ese numero a un string para al final agregar todo el # como un elemento a la lista
        if c.isdigit() :
           sub_number += c
        else:
            if len(sub_number):
                resList.append(sub_number)
                sub_number = ''
            resList.append(c)

    return resList


def ComprobarLista(numPar, completeList):

    numCaracBien = (numPar*5)+(numPar-1)

    # 1er Criterio a evaluar) que la longitud de la lista sea la correcta para que a ala hora de chacar la sintaxis según indices ni haya problemas
    # 2ndo Criterio a evaluar) Que la sintaxis sea la correcta

    while (numCaracBien != len(completeList)) or (ComprobarSintax(numPar, completeList) == False):
        #print("numCaracBien : " , numCaracBien)
        #print("len completeList : " , len(completeList))
        print ( "\n - Ejemplo de sintaxis requerida: (1,1),(2,2),(3,3),(1,2)")
        completeList = list(input("Ingrese correctamente las parejas ordenadas de enteros con la sintaxis requerida: "))
        

    return completeList


def ComprobarSintax(numPar, completeList):

    # Indice del primer elem segun corresponda
    parAbre = 0
    parCierra = 4
    comas = 2
    num = 1

    # Comprueba posición de parentésis
    for i in range(numPar):
        if completeList[parAbre] != "(" or completeList[parCierra] != ")":
            return False
        parAbre += 6
        parCierra += 6

    # Comprueba comas
    for j in range(numPar + (numPar-1)):
        if completeList[comas] != ",":
            return False
        comas+=3

    # Comprueba numeros
    for k in range(numPar*2):
        if completeList[num].isnumeric() == False:
            return False
        if k % 2 == 0:
            num+=2
        else:
            num+=4

    # Regresa True si todo es correcto
    return True



def PrepararLista(listaVerif):

    # Crea una nueva lista donde SÓLO incluirá los números - ya no los "(" ")" ","
    listaPrep = []
    for item in listaVerif:
        if item.isnumeric():
            listaPrep.append(item)

    return listaPrep


def DeterDomainFake(listaPreparada):

    # Separa las "x" en una lista - es como el dominio pero considera "TODAS" las "x" sin importar si se repiten
    size = len(listaPreparada)
    domain = []
    for i in range (size):
        if i % 2 == 0:
            domain.append(listaPreparada[i])


    return domain

            
def DeterCoDomainFake(listaPreparada):

    # Separa las "y" en una lista - es como el codominio pero considera "TODAS" las "y" sin importar si se repiten
    size = len(listaPreparada)
    coDomain = []
    for i in range (size):
        if i % 2 != 0:
            coDomain.append(listaPreparada[i])


    return coDomain



def ComproReflex(domainF,codomainF):

    # Reflexividad - Que para cada elemento del dominio existe una pareja en la que y = x -> (a,a)  ,  (b,b)
    for i in range(len(domainF)):
        num = domainF[i]

        # Si la x no existe en las "y" entonces no se cumple la Reflexividad
        if num not in codomainF:
            return False
        
        # Checa por cada "x" una "y" igual que tenga una "x" igual
        for j in range(len(codomainF)):
            if num == codomainF[j] and domainF[j] == num:
                flag = True
                break
            else: 
                flag = False

    return flag

                        
def ComproSimetria(domainF,codomainF):
    
    # Checa la simetria de las parejas
    # (a,b) -> (b,a) - Para cada pareja de ordanadas existe una que es simétrica a esta
    for i in range(len(domainF)):
        init = domainF[i]
        next = codomainF[i]
        # Si la x (init) no existe en el codominio entonces quiere decir que no hay existe simetría
        if init not in codomainF:
            return False
        for j in range(len(codomainF)):
            # Checa si sí existe otra pareja que sea igual pero invertida (simetrica)
            if init == codomainF[j] and domainF[j] == next:
                flag = True
                break
            else: 
                flag = False

    return flag



def ComproTransit(domainF,codomainF):

    # Transitividad    -   (a,b) (b,c) -> (a,c)   -   existe (a,b) buscamos una pareja con la misma "y" pero en sus "x"  -> (b,c)...
    # como (a,b) nos llevó a (b,c) -> (Estas 2 están relacionadas) por lo que debe de exitir una pareja que relacione la "x" de la 1ra y la "y" de la 2nda -> (a,c) 
    
    # Itera x & y 
    for i in range(len(codomainF)):
        x = domainF[i]
        y = codomainF[i]

        newList = []
        for h in range(len(domainF)):
            if h != i:
                newList.append(domainF[h])

        # Busca en dominio la y
        for j in range(len(domainF)):
            z = domainF[j]

            # Si no existe por default en esta pareja se cumple -> True
            if y not in domainF:
                flag = True
                break

            # Cuando encuentra una z ("x")  igual a la "y"
            if z == y:
                
                # Establece la "y" de esa z -> "w"
                w = codomainF[j]

                # Busca que exista una x en el domino con una y que sea igual a w
                for k in range(len(domainF)):
                    
                    #Si no existe por default en esta pareja se cumple -> True
                    if x not in newList:
                        flag = True
                        break

                    # Si la encuentra -> True
                    elif x == domainF[k] and w == codomainF[k]:
                        flag = True
                        break

                    # Si no -> False
                    else: 
                        flag = False

                # Al checar todos los "filtros" si al final la bandera == False ya no se cumple la Transitividad para todo el conjunto de parejas 
                if flag == False:
                    return False
            

    # Si se logra pasar todos los filtros se regresa el valor de la bandera
    return flag

    
def ObtainDomain(domainF):

    # Obtiene el dominio descartando repeticiones
    domain = []
    for i in range(len(domainF)):
        if domainF[i] not in domain:
            domain.append(domainF[i]) 
    
    return domain

def ObtainCodomain(codomainF):
    # Obtiene el codominio descartando repeticiones
    codomain = []
    for i in range(len(codomainF)):
        if codomainF[i] not in codomain:
            codomain.append(codomainF[i]) 
    
    return codomain

def IsFuncion(codomainF, domainF):
    
    # Si para x existe una y entonces se trata de una función

    # Establece una x y una y 
    for i in range(len(domainF)):
        x = domainF[i]
        y = codomainF[i]
        # Por cada pareja va comparando con las demás
        for j in range(len(domainF)):
            # Si encuentra una "x" con una "y" que sea diferente con la y que establecimos quiere decir es una relación y no una función -> False
            if x == domainF[j] and i != j and y != codomainF[j]:
                return False

    # Al checar todo si no se regresó el False es porque -> True
    return True

def ImprimirRes(domain,codomain,reflex,simetria,transit,funcion):

    # Imprime los resultados de si las propiedades se cumplen o no

    print("-------------------------------------------------------")
    print("                RELACIONES Y FUNCIONES                 \n")
    print("Características con las que cunmple la pareja ordenada:\n")
    print(" -   TRANSITIVIDAD: ", transit, "\n")
    print(" -   REFLEXIVIDAD: ", reflex, "\n")
    print(" -   SIMETRÍA: ", simetria, "\n")
    print(" -   DOMINIO: ", domain, "\n")
    print(" -   CODOMINIO: ", codomain, "\n")
    if funcion == False:
        print(" -   ES UNA RELACIÓN\n")
    else:
        print(" -   ES UNA FUNCIÓN\n")
    print("-------------------------------------------------------")




def FuncionesRelaciones():

    # Ingreso de la relación como parejas ordenadas
    numPar = IngresoNumPar()
    completeList = PideRelacion()
    listaVerif = ComprobarLista(numPar, completeList)
    listaPreparada = PrepararLista(listaVerif)   
    domainF = DeterDomainFake(listaPreparada)
    codomainF = DeterCoDomainFake(listaPreparada)
    reflex = ComproReflex(domainF,codomainF)
    simetria = ComproSimetria(domainF,codomainF)
    transit = ComproTransit(domainF,codomainF)
    domain = ObtainDomain(domainF)
    codomain = ObtainCodomain(codomainF)
    funcion = IsFuncion(codomainF,domainF)
    ImprimirRes(domain,codomain,reflex,simetria,transit,funcion)




