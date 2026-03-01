class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):

        permitidos = ["piedra", "papel", "tijera"]

        casos = {
            "tijera papel" : "jugador1",
            "papel piedra" : "jugador1",
            "piedra tijera" : "jugador1",
            "papel tijera" : "jugador2",
            "piedra papel" : "jugador2",
            "tijera piedra" : "jugador2"
        }

        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        if jugador1 == jugador2:
            return "empate"
        
        elif jugador1 not in permitidos or jugador2 not in permitidos:
            return "invalid"
        
        else:
            return casos[jugador1 + " " + jugador2]
        

    
    def adivinar_numero_pista(self, numero_secreto, intento):

        if intento > numero_secreto:
            return "muy alto"
        
        elif intento < numero_secreto:
            return "muy bajo"
        
        else:
            return "correcto"
    
    def ta_te_ti_ganador(self, tablero):

        """"
        [
        ["X", "X", "X"],
        ["O", "O", " "],
        [" ", " ", " "]
        ] -> "X"
        """
        
        vacios = False


        for i in range(0,3):
        
        
            if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
                return(tablero[i][0])


            elif tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
                return(tablero[0][i])


            elif " " in tablero[i]:
                vacios = True


        if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
            return(tablero[0][0])


        elif tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
            return(tablero[0][2])


        elif vacios == False:
            return("empate")

        else:
            return("continua") 
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        pass
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        pass