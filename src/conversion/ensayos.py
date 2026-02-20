def decimal_a_binario(decimal):

    if decimal == 1:
        return "1"
    
    else: 
        return decimal_a_binario( int(decimal/2) ) + str(decimal % 2) 
    
print(decimal_a_binario(255))