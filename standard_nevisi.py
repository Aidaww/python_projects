kochik=0
bozorg=0
kalame=input('vared kon !   ')
for letter in  kalame:
    if letter.islower():
        kochik=kochik+1
    if letter.isupper():
        bozorg=bozorg+1
if bozorg>kochik:
    kalame=kalame.upper()
else:
    kalame=kalame.lower()
print(kalame)       