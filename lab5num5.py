def piglatin():
    define=input("input a word: ")
    word=list(define)
    vow=['a','e','i','o','u']
    def vow_con():
            if word[0]==a or word[0]==e or word[0]==i or word[0]==u or word[0]==o and word[-1]!=a or word[-1]!=e or word[-1]!=i or word[-1]!=o or word[-1]!=u:
                finalw=define+"ay"
            return(finalw)
            
    def vow_vow():
        seeing_vowel=True
        for let in word:
            if seeing_consonants:
                if let in vow:
                    finalw=define+way
        return(finalw)
    def con_con():
        be=[]
        en=[]
        seeing_consonant=True
        for let in word:
            if seeing_consonants:
                if let not in vow:
                    be.append(let)
                else:
                    seeing.consonants = False
                    en.append(let)
            else:
                    en.append(let)
        return["".join(en),"".join(be)] 
    if let in vow:
        vow_vow()
    if let not in vow:
        con_con()
    else:
        vow_con()
