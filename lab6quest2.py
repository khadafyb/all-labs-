def check_string(string):
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            return True
    return False 
