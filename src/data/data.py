class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        
        lista_invertida = []
    
        for i in range(len(lista)-1,-1,-1):
            lista_invertida.append(lista[i])
            
        return lista_invertida
    
    def buscar_elemento(self, lista, elemento):
        
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
            
    
    def eliminar_duplicados(self, lista):

        if len(lista) == 0:
            return lista

        lista_depurada = []
        lista_depurada.append(lista[0])
        repetido = False

        for i in range(1,len(lista)): 
        
            for j in range(len(lista_depurada)):

                if lista[i] == lista_depurada[j] and type(lista[i]) == type(lista_depurada[j]):

                    repetido = True
                    break

            if repetido == False:
                lista_depurada.append(lista[i])

            else:
                repetido = False
            
        return lista_depurada
    
    def merge_ordenado(self, lista1, lista2):

        listaCombinada = []

        while len(lista1) != 0 and len(lista2) != 0:
        
        
            if lista1[0] > lista2[0]:
                print(lista1[0], "mayor que", lista2[0])
                listaCombinada.append(lista2[0])
                lista2.remove(lista2[0])


            elif lista2[0] > lista1[0]:
                print(lista2[0], "mayor que", lista1[0])
                listaCombinada.append(lista1[0])
                lista1.remove(lista1[0])


            else:
                print("son iguales")
                listaCombinada.append(lista1[0])
                listaCombinada.append(lista2[0])
                lista1.remove(lista1[0])
                lista2.remove(lista2[0])


        if len(lista1) != 0:
            for i in range(len(lista1)):
                listaCombinada.append(lista1[i])


        elif len(lista2) != 0:
            for i in range(len(lista2)):
                listaCombinada.append(lista2[i])

        return listaCombinada
    
    def rotar_lista(self, lista, k):
        
        if len(lista) != 0:

            for i in range(k):

                ultimo = lista[len(lista)-1]
                lista.remove(lista[len(lista)-1])
                lista.insert(0,ultimo)

        return lista



    
    def encuentra_numero_faltante(self, lista):

        lista.sort()

        if(lista[0] != 1):
            return 1
    
        else:
            print(lista)
            for i in range(len(lista)-1):

                if lista[i] - lista[i+1] != -1:
                    print(lista[i] - lista[i+1])
                    return lista[i]+1

            return lista[len(lista)-1]+1
    
    def es_subconjunto(self, conjunto1, conjunto2):

        for i in conjunto1:
            
            if i not in conjunto2:
                return False
            
        return True
    
    def implementar_pila(self):
        
        lista = []

        def push(x): lista.append(x)
        def pop(): return lista.pop()
        def peek(): return lista[-1] 


        def is_empty(): 
            if len(lista) == 0: return True
            else: return False


        return{

            "push" : push,
            "pop" : pop,
            "peek" : peek,
            "is_empty" : is_empty

        }
    
    def implementar_cola(self):

        lista = []

        def enqueue(x): lista.append(x)
        def dequeue(): return lista.pop(0)
        def peek(): return lista[0] 

        def is_empty(): 
            if len(lista) == 0: return True
            else: return False

        return{
            "enqueue" : enqueue,
            "dequeue" : dequeue,
            "peek" : peek,
            "is_empty" : is_empty
        }
    
    def matriz_transpuesta(self, matriz):

        traspuesta = [] 

        if len(matriz) == 0:
            return matriz

        for i in range(len(matriz[0])):
            traspuesta.append([])

        for i in range(len(traspuesta)):

            for j in range(len(matriz)):
                traspuesta[i].append(matriz[j][i])

        return traspuesta