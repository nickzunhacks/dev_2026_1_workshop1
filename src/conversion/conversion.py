class Conversion:
    def celsius_a_fahrenheit(self, celsius):

        return (celsius * 9/5) + 32
        
    
    def fahrenheit_a_celsius(self, fahrenheit):

        return (fahrenheit - 32) * 5/9
    
    def metros_a_pies(self, metros):
        """
        Convierte distancia de metros a pies.
        
        Args:
            metros (float): Distancia en metros
            
        Returns:
            float: Distancia en pies
            
        Factor: 1 metro = 3.28084 pies
        
        Ejemplo:
            metros_a_pies(1) -> 3.28084
        """
        return metros * 3.28084
    
    def pies_a_metros(self, pies):
        """
        Convierte distancia de pies a metros.
        
        Args:
            pies (float): Distancia en pies
            
        Returns:
            float: Distancia en metros
            
        Factor: 1 pie = 0.3048 metros
        
        Ejemplo:
            pies_a_metros(3.28084) -> 1.0
        """

        return pies * 0.3048

        pass
    
    def decimal_a_binario(self, decimal):

        def solucion(decimal):

            if decimal == 0:
                return "0"

            elif decimal == 1:
                return "1"

            else: 
                return solucion( int(decimal/2) ) + str(decimal % 2) 
            
        return solucion(decimal)

    
    def binario_a_decimal(self, binario):

        potencia = len(binario) - 1
        decimal = 0

        for i in binario:

            if i == '1':
                decimal += 2**potencia
                
            potencia -= 1

        return decimal
    
    def decimal_a_romano(self, numero):

        romanos = {
            'M' : 1000,
            'CM' : 900,
            'D' : 500,
            'CD' : 400,
            'C' : 100,
            'XC' : 90,
            'L' : 50,
            'XL' : 40,
            'X' : 10,
            'IX' : 9,
            'V' : 5,
            'IV' : 4,
            'I' : 1
        }
        romano = ''
        decimal_aux = numero

        while decimal_aux > 0:
            for i in romanos:
                if romanos[i] <= decimal_aux:
                    romano += i
                    decimal_aux -= romanos[i]
                    break
        return romano
    
    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        
        Args:
            romano (str): Número romano válido
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
        pass
    
    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.
        
        Args:
            texto (str): Texto a convertir (letras y números)
            
        Returns:
            str: Código Morse separado por espacios
            
        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
        pass
    
    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        
        Args:
            morse (str): Código Morse separado por espacios
            
        Returns:
            str: Texto decodificado
            
        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
        """
        pass