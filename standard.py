def num(esm):
    esm=esm[0].upper()+esm[1:].lower()
    return esm 


c=[]


for i in range (0,3):
    esm=input('badi  ')
   
    c.append(num(esm))
   
    

print(c)
