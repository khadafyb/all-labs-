def lb_funct(string):
    counter=0
    for char in string:
        if char in "1234567890":
            counter+= 1
    return counter 
             
