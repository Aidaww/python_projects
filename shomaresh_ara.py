 
Esm=(input('vared kon!  '))
ara=dict()
while (Esm != str(-1)):
    ara[Esm]=ara.get(Esm,0)+1
    Esm=(input('vared kon!  '))
    
for item in ara:
    print(item,ara[item])
    

