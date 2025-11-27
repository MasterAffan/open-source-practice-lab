def divide(a, b):
    
    '''
    Divides a by b and returns the result.
    If b is equals to zero then if block runs and it raises the ZeroDivision error 
    and prints the message "Division by zero is not allowed".
    '''
    
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.") 
    
    return a / b
