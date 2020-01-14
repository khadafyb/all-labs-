def process(txtf):
    count=0
    words=[]
    with open(txtf,'r') as f:
        for line in f:
            for word in line.split():
                w=word.strip(",.;:?-![]_\"")
                if len(w) > 8:
                    words.append(w)
    return words

def hyphen(txtf):
    count=0
    words=[]
    with open(txtf,'r') as f:
        for line in f:
            for word in line.split():
                for char in word:
                    if "-" in char :
                        words.append(word)
    return words

def line_count(txtf):
    count=0
    counter=[]
    words=[]
    index={}
    with open(txtf,'r') as f:
        for line in f:
            count+=1
            for word in line.split():
                if len(word) > 8:
                    index[word].append(counter)
                else:
                    index[word]=[counter]
    return index

def line_count2(txtf):
    count=0
    counter=[]
    words=[]
    index={}
    with open(txtf,'r') as f:
        for line in f:
            count+=1
            for word in line.split():
                if len(word) > 8:
                    index[word].append(counter)
                else:
                    index[word]=[counter]
    sorted(index.keys())
    index[word]
    return index

#def pretty(dic):

def dna(txtf):
    with open (txtf,"r") as f:
        for line in f:
            for word in line.split():
                for char in word:
                    if char not in "ACTGN":
                        print(line)
def dna_dict(txtf):
    dicti={'A':0,'C':0,'G':0,'T':0,'N':0}
    with open (txtf,"r") as f:
        for line in f:
            for word in line.split():
                for char in word:
                    if char in dicti:
                        dicti[char]+=1
    return dicti

def dna_dict2(txtf):
    dicti={'AA':0,'CC':0,'GG':0,'TT':0,'NN':0}
    with open (txtf,"r") as f:
        for line in f:
            for word in line.split():
                for char in word:
                    if char in dicti:
                        dicti[char]+=1
    return dicti
