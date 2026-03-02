class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):

        def solucion(n):

            if n == 0:
                return 0

            elif n == 1:
                return 1
            
            elif n < 0:
                return None

            return( solucion(n-1) + solucion(n-2) )
        
        return solucion(n)
    
    def secuencia_fibonacci(self, n):

        secuencia = []

        for i in range(n):

            if i == 0 or i == 1:
                secuencia.append(i)

            else:
                secuencia.append( secuencia[i-1] + secuencia[i-2])

        return secuencia
    
    def es_primo(self, n):

        if n <= 1:
            return False
        
        for i in range(2,n):
            if n%i == 0:
                return False
            
        return True
    
    def generar_primos(self, n):

        primos = []

        for i in range(1,n+1):

            if self.es_primo(i) == True:
                primos.append(i)

        return primos
    
    def es_numero_perfecto(self, n):

        if n == 0:
            return False

        divisores = []

        for i in range(1,n):
            if n % i == 0:
                divisores.append(i)

        suma_divisores = 0

        for i in divisores:
            suma_divisores += i

        if suma_divisores == n:
            return True

        else:
            return False
    
    def triangulo_pascal(self, filas):

        pascal = []
        nivel = []

        for i in range(1,filas+1):

            if i == 1:
                nivel.append(1)
                pascal.append(nivel)

            else:
                nivel = [1]
                ultima_lista = pascal[len(pascal)-1]

                for j in range(len(ultima_lista)-1):
                    nivel.append(ultima_lista[j]+ultima_lista[j+1])
                    
                nivel.append(1)
                pascal.append(nivel)

        return pascal
    
    def factorial(self, n):

        if n == 0:
            return 1
        
        elif n < 0:
            return None
        
        else:
            for i in range(1,n):
                n *= i
        
        return n
    
    def mcd(self, a, b):

        if b == 0:
            return a

        elif a % b == 0:
            return b

        mod = a%b
        a = b
        b = mod
    
        return self.mcd(a,b)


    def mcm(self, a, b):

            return (a*b) / self.mcd(a,b)
        

    
    def suma_digitos(self, n):

        digitos = str(n)
        total = 0

        for i in digitos:
            total+=int(i)

        return total
    
    def es_numero_armstrong(self, n):

        digitos = str(n)
        suma = 0

        for i in digitos:
            suma += int(i)**len(digitos)

        if suma == int(digitos):
            return True
        
        else:
            return False
    
    def es_cuadrado_magico(self, matriz):

        constante = 0
        suma = 0
        
        for i in matriz[0]:
            constante += i

        #evaluacion horizontal
        for i in range(1,len(matriz)):
            suma = 0
            for j in range(len(matriz)):
                suma += matriz[i][j]
            if suma != constante:
                return False
        # evaluacion vertical
        for i in range(len(matriz)):
            suma = 0
            for j in range(len(matriz)):
                suma += matriz[j][i]
            if suma != constante:
                return False

        #evaluacion diagonal
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][i]
        if suma != constante:
            return False


        # evalacuacion diagnoal inversa
        suma = 0
        j= len(matriz)-1
        for i in range(len(matriz)):
            suma += matriz[i][j]
            j-=1
        if suma != constante:
            return False

        return True