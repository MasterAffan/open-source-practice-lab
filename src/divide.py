def divide(a, b):
    
    '''
    Divides a by b and returns the result.
    If b is equals to zero then if block runs and it raises the ZeroDivision error 
    and prints the message "Denominator cannot be zero.".
    '''
    
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero.") 
    
    return a / b
