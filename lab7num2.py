import random
for i in range(0,11):
    s="f"+str(i)+".txt"
    with open(s,"w") as outfile:
        x=10+random.gauss(0,0.2)
