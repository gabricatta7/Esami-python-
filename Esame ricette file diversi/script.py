from pathlib import Path
import os
from collections import Counter

ricette = {}
files = os.listdir("dati")
for f in files:
    if os.path.isfile("dati/"+f):
        ricetta = f.split('.')[0]
        ricette[ricetta] = {}
        
        with open("dati/"+f) as file:
            for i in (file.read()).splitlines():
                ingrediente = i.split(',')[0]
                quantIngr =  int(i.split(',')[1])
                
                ricette[ricetta][ingrediente] = quantIngr
print(ricette)


#punto 1 
listIngr = []
for i in ricette:
    #print(ricette[i])
    for j in ricette[i]:
        #print(j)
        listIngr.append(j)

str = ''
with open("1.txt","w") as o:
    for k in listIngr:
        count = listIngr.count(k)
        str += f'{k} : {count} \n'
    o.write(str) 

#punto 2 
with open("2.txt","w") as o:
    for t in ricette:
        o.write(t+':'+'\n')
        #print(list(ricette[t].values())) 
        totaleIngr = sum(list(ricette[t].values()))
        #print(totaleIngr)
        #percentuale singolo ingrediente
        
        for i in ricette[t]:
            percIngr = ricette[t][i] * 100 / totaleIngr
            #arrotondo a una cifra 
            percIngr = round(percIngr,1)
            if i == list(ricette[t].keys())[-1]:
                o.write (f'{percIngr}% di {i} \n') 
            else:
                o.write (f'{percIngr}% di {i} \n')       

   
#punto3 
with open("3.txt","w") as o:
    for j in ricette:
        maxIngrValore = 0
        maxIngr = ''
        for k in ricette[j]:
            if ricette[j][k]>= maxIngrValore:
                maxIngrValore = ricette[j][k]
                maxIngr = k
        o.write(f'{j} : {maxIngr} con {maxIngrValore}\n')    
   