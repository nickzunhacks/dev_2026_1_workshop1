class Stats:
    def promedio(self, numeros):

        promedio = 0
        cantidad = len(numeros)

        if cantidad == 0:
            return promedio

        for i in numeros:
            promedio += i

        promedio /= cantidad

        return promedio
    
    def mediana(self, numeros):

        if len(numeros) == 0:
            return 0

        numeros.sort()

        if len(numeros) % 2 == 0:  
            return self.promedio( [ numeros[ int(len(numeros)/2) ], numeros[ int(len(numeros)/2 - 1)]  ] )
        
        else:
            return numeros[ int(len(numeros)/2) ]
    
    def moda(self, numeros):

        if len(numeros) == 0:
            return None
        
        elementos = {}

        for i in numeros:
            try:
                elementos[i] += 1
            except:
                elementos[i] = 1
                
        mayor = max(elementos, key=elementos.get)
        return mayor
    
    def desviacion_estandar(self, numeros):

        if len(numeros) == 0:
            return 0
        
        med = self.mediana(numeros)
        sumatoria = 0

        for i in numeros:
            sumatoria += (i-med)**2      

        desviacion = ( sumatoria / len(numeros) ) ** 0.5
        return desviacion
    
    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        La varianza es el cuadrado de la desviación estándar.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La varianza
            
        Ejemplo:
            varianza([1, 2, 3, 4, 5]) -> 2.0
        """
        pass
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: La diferencia entre max y min
            
        Ejemplo:
            rango([1, 5, 3, 9, 2]) -> 8
        """
        pass