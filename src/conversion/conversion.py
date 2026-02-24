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

        romano_aux = romano
        decimal = 0

        while len(romano_aux) > 0:

            if romano_aux[:2] in romanos:
                decimal += romanos[ romano_aux[:2] ]
                romano_aux = romano_aux[2:]

            else:
                decimal += romanos[romano_aux[:1]]
                romano_aux = romano_aux[1:]

        return decimal
    
    def texto_a_morse(self, texto):

        texto_morse = {
            'A' : '.-',
            'B' : '-...',
            'C' : '-.-.',
            'E' : '.',
            'H' : '....',
            'L' : '.-..',
            'O' : '---',
            'S' : '...',
            '1' : '.----',
            '2' : '..---',
            '3': '...--'
        }

        texto_aux = texto.upper()
        morse = ""

        for i in texto_aux:
            morse += texto_morse[i] + " "

        morse = morse[0: len(morse)-1 ]

        return morse

    def morse_a_texto(self, morse):

        morse_texto = {
            "" : "",
            '.-' : 'A',
            '-...' : 'B',
            '-.-.' : 'C',
            '.' : 'E',
            '....' : 'H',
            '.-..' : 'L',
            '---' : 'O',
            '...' : 'S',
            '.----' : '1',
            '..---' : '2',
            '...--': '3'
        }

        texto = ""
        letra = ""
        morse_aux = morse + " "

        for i in morse_aux:
            
            if i == " ":
                texto += morse_texto[letra]
                letra = ""

            else:
                letra += i

        return texto