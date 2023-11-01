color=['Kier','Karo','Pik','Trefl']
figury=[{'Figure':'As','Power':14},
        {'Figure':'Król','Power':13},
        {'Figure':'Dama','Power':12},
        {'Figure':'Jopek','Power':11},
        {'Figure':'10','Power':10},
        {'Figure':'9','Power':9}]
allCards=[]
for c in color:
    for f in figury:
        aCard= f.copy()
        aCard['Color']=c
        allCards.append(aCard)

import random

random.shuffle(allCards)
"""print(allCards)"""
gracz1=[]
gracz2=[]

gracz1=allCards[:12]
gracz2=allCards[12:]
""""
imax=len(allCards)-1
i=0
while i<=imax:
    if i%2==0:
        gracz1.append(allCards[i])
        i+=1

    else:
        gracz2.append(allCards[i])
        i += 1

print("Karty Gracza1 to: ",gracz1)
print("Karty Gracza2 to: ",gracz2)
"""
while len(gracz1) > 0 and len(gracz2) > 0:
    card1 = gracz1.pop(0)
    card2 = gracz2.pop(0)
    talia=[]

    if card1["Power"] == card2["Power"]:        
        while card1["Power"] == card2["Power"]:
            talia.append(card1)
            talia.append(card2)
        
            if len(gracz1)<2:
                gracz1 = []
                print('PLAY-1')
                break
            elif len(gracz2)<2:
                gracz2 = []
                print('PLAY-2')
                break
            else:
                card1 = gracz1.pop(0)
                card2 = gracz2.pop(0)
                talia.append(card1)
                talia.append(card2)
                card1 = gracz1.pop(0)
                card2 = gracz2.pop(0)
        else:
            if card1["Power"] > card2["Power"]:
                talia.append(card1)
                talia.append(card2)
                gracz1.extend(talia)
               
            
            else:
                talia.append(card1)
                talia.append(card2)
                gracz2.extend(talia)
                
              



    elif card1["Power"] > card2["Power"]:
        gracz1.append(card1)
        gracz1.append(card2)
        
        print('PLAY-2',card2,len(gracz2),len(gracz1),card1)
    else:
        gracz2.append(card1)
        
        gracz2.append(card2)
        print('PLAY-1', card2, len(gracz2), len(gracz1), card1)

if len(gracz1)<0:
    print('Win-2')
else: 
    print('Win-1')
