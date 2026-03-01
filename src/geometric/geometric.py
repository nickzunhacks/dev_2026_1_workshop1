PI = 3.1416

class Geometria:
    """
    Class with geometric exercises.
    Include basic and funny operations in 2D and 3D.
    """

    def area_rectangulo(self, base, altura):

        if base < 0 or altura < 0:
            return 0

        return base*altura
    
    def perimetro_rectangulo(self, base, altura):

        return base*2 + altura*2
    
    def area_circulo(self, radio):

        if radio < 0:
            return 0
        
        return PI * radio**2
    
    def perimetro_circulo(self, radio):

        if radio < 0:
            return 0

        return round(2 * PI * radio,2)

    
    def area_triangulo(self, base, altura):

        if base < 0 or altura < 0:
            return 0

        return (base*altura)/2
    
    def perimetro_triangulo(self, lado1, lado2, lado3):

        return lado1 + lado2 + lado3
    
    def es_triangulo_valido(self, lado1, lado2, lado3):

        if lado1 + lado2 > lado3:
            return True
        
        elif lado1 < 0 or lado2 < 0 or lado3 < 0:
            return False
        
        else:
            return False
    
    def area_trapecio(self, base_mayor, base_menor, altura):

        return ( (base_mayor+base_menor)*altura ) / 2
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):

        return (diagonal_mayor * diagonal_menor) / 2
    
    def area_pentagono_regular(self, lado, apotema):

        return (5*lado*apotema) /2
    
    def perimetro_pentagono_regular(self, lado):

        return 5 * lado
    
    def area_hexagono_regular(self, lado, apotema):

        return (lado*6*apotema) / 2
    
    def perimetro_hexagono_regular(self, lado):

        return lado*6
    
    def volumen_cubo(self, lado):

        if lado < 0:
            return 0

        return lado**3
    
    def area_superficie_cubo(self, lado):

        return 6*lado**2
    
    def volumen_esfera(self, radio):

        return 4/3 * PI * radio**3
    
    def area_superficie_esfera(self, radio):

        return 4*PI*radio**2
    
    def volumen_cilindro(self, radio, altura):
        return radio**2*PI*altura
    
    def area_superficie_cilindro(self, radio, altura):
        return 2*PI*radio*(altura+radio)
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        return ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    
    def punto_medio(self, x1, y1, x2, y2):
        return ((x1 + x2)/2) , ((y1 + y2)/2)
    
    def pendiente_recta(self, x1, y1, x2, y2):
        return (y2-y1)/(x2-x1)
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        a = y2-y1
        b = -(x2-x1)
        c = -(a*x1 + b*y1)

        if a == 0:

            b *= -1
            c *= -1

            while( b%2 == 0 and c%2 == 0 or b%3 == 0 and c%3 == 0 ):
            
            
                if b%2 == 0 and c%2 == 0:
                    b /= 2
                    c /= 2


                elif b%3 == 0 and c%3 == 0:
                    b /= 3
                    c /= 3

        return( int(a),int(b),int(c) )
    
    def area_poligono_regular(self, num_lados, lado, apotema):
        return ((num_lados*lado) * apotema) / 2
    
    def perimetro_poligono_regular(self, num_lados, lado):
        return num_lados*lado
