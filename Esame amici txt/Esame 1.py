
gruppo = {}
#creazione struttra dati
dati = open("input.txt").readlines()
for i in range(len(dati)):
    dati[i] = dati[i].strip('\n')
gruppo = {}
for i in range(len(dati)):
    if dati[i].endswith("->"):              #TROVATA CHIAVE LISTA AMICI
        nome = dati[i].strip("->")
        if nome not in gruppo:        #SE NON ESISTE GIA', CREARE NUOVA LISTA
            gruppo[nome] = []
    else:
        gruppo[nome].append(dati[i])       #AGGIUNGE NOME


#-------------->per ogni persona stampo numero degli amici
p2 = open("2.txt", "w+")
for key, values in gruppo.items():
    numeroAmici = len(list(values))
    p2.write(key+'---->'+str(numeroAmici)+'\n')

#-------------->calolo persone con max amici e min amici e le metto in una lista
p1 =    open("1.txt",'w+') 
personePopolari = []
personeBho = []
for persona in gruppo:
    amiciMax = max(len(gruppo[persona]) for persona in gruppo)
    if len(gruppo[persona]) == amiciMax:
        personePopolari.append(persona)
    amiciMin = min(len(gruppo[persona]) for persona in gruppo)
    if len(gruppo[persona]) == amiciMin:
        personeBho.append(persona)
stringaPersonepopolari = str([i for i in personePopolari])
stringaPersonebho = str([i for i in personeBho])
p1.write('La persona con piu amici è: '+stringaPersonepopolari.replace('[','').replace(']','').replace("'",'')+'\n'+'La persona con meno amici è: '+stringaPersonebho.replace('[','').replace(']','').replace("'",''))



#------------>trovo persone con gli stessi amici
p2 = open("2.txt", "w+")
personeStessiAmici = []
listaAmici = []
for key, values in gruppo.items():
    listaAmici.append(values)
count = []
counter = 0
for i in listaAmici:
    if i not in count:
        counter += 1
        count.append(i)
    else:
        counter += 1
    if counter > 1:
        personeStessiAmici.append([t for t in gruppo if gruppo[t]==i])  
stringaPersonestessiamici = str([i for i in personeStessiAmici])
p2.write('Le persone con gli stessi amici sono: '+stringaPersonestessiamici.replace('[','').replace(']','').replace("'",''))


#--------->creo tabella
tabella = []
r = []
personeGruppo = ['Matteo','Marco','Luca','Anna','Franco']
for i in range(5):
    for j in range(5):
        r.append("\t"+'0')
    tabella.append(r)
    r = []
for i in range(len(tabella)):
    for j in range(len(tabella[i])):
        print(tabella[i][j], end='  ')
    print()


             