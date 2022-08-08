import Sucesiones
import RelacionesFunciones
import tablasV
import Conjuntos


def ImprimeBienvenida():
    print("                BIENVENIDO               \n")
    print(" Esta es una ToolKit de la clase de... \n")
    print(" Fundamentos de Ciencias Computacionales\n")
    
    print("ToolKits (Herramientas) disponibles...\n")
    print("1) Tablas de Verdad\n")
    print("2) Conjuntos\n")
    print("3) Sucesiones\n")
    print("4) Relaciones & Funciones\n")


def InputToolKit():
    select = input("Ingrese el inciso de la herramienta con la que desea interactuar: ")
    while select != "1" and select != "2" and select != "3" and select != "4":
        select = input("Ingrese correctamente el inciso de la herramienta con la que desea interactuar: ")
    select = int(select)

    return select

def CorreTool(tool):
    
    # Segun la opción seleccionada imprime el tírylo de la Tool y corre el .py que corresponde

    print("\n-------------------------------------------------------------------------------\n")
    if tool == 1:
        print("\n                          TABLAS DE VERDAD      \n")
        tablasV.tablasV()
    elif tool == 2:
        print("\n                          CONJUNTOS       \n")
        Conjuntos.conjuntos()
    elif tool == 3:
        print("\n                          SUCESIONES      \n")
        Sucesiones.mainSucesiones()
    else:
        print("\n                          RELACIONES & FUNCIONES      \n")
        RelacionesFunciones.FuncionesRelaciones()


def main():
    ImprimeBienvenida()
    tool = InputToolKit()
    CorreTool(tool)




#Final
if __name__ == "__main__":
    main()

    

    

    


    


