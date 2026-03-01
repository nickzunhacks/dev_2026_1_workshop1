class Logica:
    """
    Clase con métodos para realizar operaciones de lógica booleana y algoritmos.
    """
    
    def AND(self, a, b):

        if a == True and b == True:
            return True
        
        else:
            return False
    
    def OR(self, a, b):

        if a == True or b == True:
            return True
        
        else:
            return False
    
    def NOT(self, a):

        if a:
            return False
        
        else:
            return True
    
    def XOR(self, a, b):

        if a and not b:
            return True
        
        elif b and not a:
            return True
        
        else:
            return False
    
    def NAND(self, a, b):
        
        if a and b:
            return False
        else:
            return True
    
    def NOR(self, a, b):

        if not a and not b:
            return True
        
        else:
            return False
    
    def XNOR(self, a, b):

        if a and b:
            return True
        
        elif not a and not b:
            return True
        
        else:
            return False
    
    def implicacion(self, a, b):

        if a and not b:
            return False
        
        else:
            return True

        
    
    def bi_implicacion(self, a, b):

        if a and b:
            return True
        
        elif not a and not b:
            return True
        
        else:
            return False