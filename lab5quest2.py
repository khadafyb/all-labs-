def consonant(string):
    con=0
    for i in string:
        if i in "bBCcdDbBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXzZ":
            con+=1
    return con 
