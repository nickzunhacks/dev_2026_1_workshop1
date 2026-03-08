class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):

        texto_invertido = texto[::-1].lower()
        texto = texto.lower()

        texto_invertido = texto_invertido.replace(" ","")
        texto = texto.replace(" ","")

        if texto == texto_invertido:
            return True
        
        else:
            return False
    
    def invertir_cadena(self, texto):

        cadena_invertida = ""

        texto_lista = list(texto)

        for i in range(len(texto_lista)-1,-1,-1):
            cadena_invertida += texto_lista[i]

        return cadena_invertida

    
    def contar_vocales(self, texto):

        vocales = ["a","e","i","o","u"]
        texto = texto.lower()

        num_vocales = 0

        for i in texto:
            if i in vocales:
                num_vocales += 1

        return num_vocales
    
    def contar_consonantes(self, texto):

        vocales = ["a","e","i","o","u"]

        num_consonantes = 0

        texto = texto.lower()

        for i in texto:

            if i in vocales:
                continue
            num_consonantes += 1

        return num_consonantes
    
    def es_anagrama(self, texto1, texto2):

        texto1 = texto1.replace(" ","")
        texto2 = texto2.replace(" ","")

        texto1 = texto1.lower()
        texto2 = texto2.lower()

        if len(texto1) != len(texto2):
            return False
        
        texto1 = list(texto1)
        texto2 = list(texto2)

        for i in range(len(texto1)):
            if texto1[i] not in texto2:
                return False
            
        return True
    
    def contar_palabras(self, texto):

        texto = texto.strip()
        
        if len(texto) == 0:
            return 0
        
        palabras = 1

        for i in texto:
            if i == " ":
                palabras += 1

        return palabras
    
    def palabras_mayus(self, texto):

        texto = list(texto)
        first_letter = True

        for i in range(len(texto)):

            if texto[i] != " " and first_letter == True:
                texto[i] = texto[i].upper()
                first_letter = False
                
            elif texto[i] == " ":
                first_letter = True

        return "".join(texto)
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        pass
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        pass
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass