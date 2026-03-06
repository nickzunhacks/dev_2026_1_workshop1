class Matrix:
    """
    Clase con métodos para operaciones sobre matrices.
    Incluye operaciones aritméticas, propiedades y transformaciones matriciales.
    """

    def suma_matrices(self, A, B):

        if len(A[0]) != len(B[0]):
            raise ValueError("numero de columnas incopatible")

        elif len(A) != len(B):
            raise ValueError("numero de filas incopatible")
        
        C = []

        for i in range(len(A)):
            suma = []

            for j in range(len(A[i])):
                suma.append (A[i][j] + B[i][j])

            C.append(suma)

        return C

    def resta_matrices(self, A, B):
        
        if len(A[0]) != len(B[0]):
            raise ValueError("numero de columnas incopatible")
        
        elif len(A) != len(B):
            raise ValueError("numero de filas incopatible")

        C = []

        for i in range(len(A)):
            resta = []

            for j in range(len(A[i])):
                resta.append (A[i][j] - B[i][j])

            C.append(resta)

        return C

    def multiplicar_matrices(self, A, B):

        if len(A[0]) != len(B):
            raise ValueError("matrices incompatibles")

        C = []
        suma = []

        for i in range(len(A)):
            suma = []

            for j in range(len(A)):
                suma.append(0)

                for k in range(len(B)):
                    print(f"suma[{j}] += {A[i][k]} * {B[k][j]}")
                    suma[j] += A[i][k] * B[k][j]

            C.append(suma)

        return C




    def multiplicar_escalar(self, matriz, escalar):
        
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                matriz[i][j] *= escalar
                
        return matriz
            
            

    def transpuesta(self, matriz):
        
        traspuesta = []

        if len(matriz) == 0:
            return traspuesta
        
        for i in range(len(matriz[0])):
            traspuesta.append([fila[i] for fila in matriz])
            
        return traspuesta

    def es_cuadrada(self, matriz):
        
        if len(matriz) == 0:
            return False

        filas = len(matriz)
        columnas = len(matriz[0])

        if filas == columnas:
            return True
        
        else:
            return False

    def es_simetrica(self, matriz):

        traspuesta = self.transpuesta(matriz)

        if traspuesta == matriz:
            return True
        else:
            return False

    def traza(self, matriz):
        
        cuadrada = self.es_cuadrada(matriz)

        if not cuadrada:
            raise ValueError("debe ser cuadrada para calcular la traza")

        traza = 0

        for i in range(len(matriz)):
            traza += matriz[i][i]

        return traza

    def determinante_2x2(self, matriz):

        if len(matriz) != 2 or len(matriz[0]) != 2:
            raise ValueError("matriz debe ser 2x2")
        
        determinante = matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
        return determinante

    def determinante_3x3(self, matriz):

        if len(matriz) != 3 or len(matriz[0]) != 3:
            raise ValueError("matriz debe ser 3x3")
        
        diagonales_principales = matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[1][0]*matriz[2][1]*matriz[0][2] + matriz[2][0]*matriz[0][1]*matriz[1][2]
        diagonales_secundarias = matriz[0][2]*matriz[1][1]*matriz[2][0] + matriz[1][2]*matriz[2][1]*matriz[0][0] + matriz[2][2]*matriz[0][1]*matriz[1][0]

        determinante = diagonales_principales - diagonales_secundarias

        return determinante
    
    def identidad(self, n):

        matriz = []

        for i in range(n):
            matriz.append([])
            for j in range(n):
                matriz[i].append(0)

        for i in range(n):
            matriz[i][i] = 1

        return matriz

    def diagonal(self, matriz):

        cuadrada = self.es_cuadrada(matriz)

        if not cuadrada:
            raise ValueError("La matriz debe ser cuadrada")
        
        diagonal = []

        for i in range(len(matriz)):
            diagonal.append(matriz[i][i])

        return diagonal

    def es_diagonal(self, matriz):

        for i in range(len(matriz)):
            if matriz[i][i] == 0:
                return False
            
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                
                if i == j:
                    pass

                elif matriz[i][j] != 0:
                    return False
                
        return True


    def rotar_90(self, matriz):

        invertida = self.transpuesta(matriz)

        for i in invertida:
            i.reverse()

        return invertida

    def buscar_en_matriz(self, matriz, valor):

        ubicaciones = []
        for i in range(len(matriz)):

            for j in range(len(matriz)):
                
                if matriz[i][j] == valor:
                    ubicaciones.append((i,j))

        return ubicaciones      






