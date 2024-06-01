code=input('dig  ')
bah=['a','A','e','E','i','I','o','O','u','U']
for i in code:
    for d in range (0,len(bah)):
        if i==bah[d]:
            code=code.replace(bah[d],'.')
print(code.lower())        