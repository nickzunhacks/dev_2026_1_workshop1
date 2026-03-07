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
        
        med = self.promedio(numeros)
        sumatoria = 0

        for i in numeros:
            sumatoria += (i-med)**2      

        desviacion = ( sumatoria / len(numeros) ) ** 0.5
        return desviacion
    
    def varianza(self, numeros):

        return (self.desviacion_estandar(numeros))**2
    
    def rango(self, numeros):

        if len(numeros) == 0:
            return 0
        
        maximo = max(numeros)
        minimo = min(numeros)

        return maximo - minimo