def randtup(n):
    import random
    alist = []
    for i in range(0,n):
        alist.append((random.randint(0,9), random.randint(0,999)))
    return alist
        

def tupremove(list1):
    seen=set()
    corrected=[]
    for a,b in list1:
        if not a in seen:
            seen.add(a)
            corrected.append((a,b))
    return corrected
def wordcheck(n,f):
    r=set(n)
    t=set(f)
    if r==t:
        print("given words are the same")
    else:
        print("words are not the same")
list1=[x**2 for x in range(0,11)]
list2=[x for x in range(0,101)]
dic={x**2: x for x in range(0,101)}

def get_random_word():
    import random
    random.randint(0,len(lista)-1)
def draw(errors):
    if error==0:
        print("+----+")
    elif error==1:
        print("+----+")
        print("     |"
        print("     o")
    elif error==2:
        print("+----+")
        print("     |"
        print("     o")
        print("    /|\\")
    


seen_list=[]
let=input("enter a letter")
if let not in seen_list:
    seen_list.append(let)
    return let
else:
    let=(input("enter another letter")
    
