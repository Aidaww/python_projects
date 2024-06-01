y=[]
count=0
tedad=0
for i in range(0,3):
    x=int(input('vared kon! '))
    y.append(x)
    
for i in range(0,3):
    for b in range(1,len(y)+1):
        if y[i]%b==0:
            count=count+1  
    if count >tedad:
        print(y[i])
        tedad=count
    count=0
print(y[i],tedad)
     

  
    