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
        """
        Calcula el determinante de una matriz 3x3 usando la regla de Sarrus.

        Args:
            matriz (list): Matriz 3x3 (lista de listas)

        Returns:
            number: El determinante de la matriz

        Raises:
            ValueError: Si la matriz no es 3x3

        Ejemplo:
            determinante_3x3([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> 0
            determinante_3x3([[1, 0, 0], [0, 2, 0], [0, 0, 3]]) -> 6
        """
        pass

    def identidad(self, n):
        """
        Genera una matriz identidad de tamaño n x n.
        La diagonal principal tiene 1s y el resto 0s.

        Args:
            n (int): Tamaño de la matriz identidad

        Returns:
            list: Matriz identidad n x n

        Ejemplo:
            identidad(2) -> [[1, 0], [0, 1]]
            identidad(3) -> [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        """
        pass

    def diagonal(self, matriz):
        """
        Extrae los elementos de la diagonal principal de una matriz cuadrada.

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            list: Lista con los elementos de la diagonal principal

        Raises:
            ValueError: Si la matriz no es cuadrada

        Ejemplo:
            diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [1, 5, 9]
            diagonal([[3, 0], [0, 7]]) -> [3, 7]
        """
        pass

    def es_diagonal(self, matriz):
        """
        Verifica si una matriz cuadrada es diagonal
        (todos los elementos fuera de la diagonal principal son cero).

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            bool: True si la matriz es diagonal, False en caso contrario

        Ejemplo:
            es_diagonal([[3, 0], [0, 7]]) -> True
            es_diagonal([[1, 2], [0, 4]]) -> False
        """
        pass

    def rotar_90(self, matriz):
        """
        Rota una matriz 90 grados en sentido horario.

        Args:
            matriz (list): Matriz (lista de listas)

        Returns:
            list: Matriz rotada 90 grados en sentido horario

        Ejemplo:
            rotar_90([[1, 2], [3, 4]]) -> [[3, 1], [4, 2]]
            rotar_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        """
        pass

    def buscar_en_matriz(self, matriz, valor):
        """
        Busca un valor en la matriz y retorna todas las posiciones donde se encuentra.

        Args:
            matriz (list): Matriz (lista de listas)
            valor: Valor a buscar en la matriz

        Returns:
            list: Lista de tuplas (fila, columna) con las posiciones del valor.
                  Retorna lista vacía si no se encuentra.

        Ejemplo:
            buscar_en_matriz([[1, 2, 3], [4, 2, 6], [7, 8, 2]], 2) -> [(0, 1), (1, 1), (2, 2)]
            buscar_en_matriz([[1, 2], [3, 4]], 9) -> []
        """
        pass
