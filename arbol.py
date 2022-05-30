from nodo import Nodo

class Arbol:
    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    # Funciones públicas

    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)
    
    def isBranch(self,nodo):
        if nodo.izquierda is None and nodo.derecha is None:
            return True
        else:
            return False
        
    #Target sum
    #Recibimos en las funciones 
    # path: que sera el camino de datos trazado
    # tarSum: que sera el sumero a llegar
    # nodo: raiz
    # vay: que llevara la suma de cada nodo
    def tarSum(self,path,tarSum,nodo,var):
        ## Si ya se llego a la suma y el nodo no tiene hijos entondes se devuelve la lista con el path 
        if nodo.dato + var == tarSum and nodo.isBranch:
            path.append(nodo.dato)
            return print(path)
        else:
        ## de lo contrario se suma el dato a la variable de la suma,
        # se agrega a la lista path y se sigue con la busqueda
            var + nodo.dato
            path.append(nodo.dato)
            self.tarSum(path,tarSum,nodo.izquierdo,var)
            self.tarSum(path,tarSum,nodo.derecho,var)
    
    ##Smallest kth
    ##se reciben las variables
    #nodo: raiz
    #kt valor th°
    ## arr que almacenara todos los valores
    ## recorreremos todo el arbol agregando los valores a la lista arr
    ## cuando todos los datos esten en la lista se devolvera el valot th -1 ya que las listas comienzan desde 0P
    def smallKt(self,nodo,kt,arr):
        if nodo.isBranch == True:
            arr.append(nodo.dato)
            arr.sort()
            return arr[kt-1]
        else:
            arr.append(nodo.dato)
            self.smallKt(nodo.izquierdo,kt,arr)
            self.smallKt(nodo.derecho,kt,arr)
            
        