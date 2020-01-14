def not_list(a_list,p):
    g= list(range(0,p,y))
    for num in g:
        if num in a_list:
            g.remove(num)
    return g

def alt(a_list,a_num):
    result=[]
    for i in range(0,a_num):
        if i not in a_list:
            result.append(i)
    return result
            
        
