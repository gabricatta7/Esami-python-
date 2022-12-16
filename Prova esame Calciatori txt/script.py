with open("input.txt") as f:
    temp = f.read().strip().split("\n")
dati = []

# print(int(temp[1].split("-")[0])+int(temp[1].split("-")[1]))
for i in range(len(temp)):
    partita = {}
    punteggio = {}
    goal = 0
    if temp[i].count("-") == 1 and temp[i].split("-")[0].isalpha():  # se sono dalla partita
        marcatori = []
        #print("sono dalla partita", i)
        partita["partita"] = temp[i]
        dati.append(partita)
    if temp[i].split("-")[0].isnumeric():  # se sono dal punteggio
        goal = int(temp[i].split("-")[0]) + int(temp[i].split("-")[1])
        punteggio["punteggio"] = temp[i]
        #print("sono dal punteggio", i)
        dati.append(punteggio)
        if goal == 0:
            dati.append([])
    if temp[i].isalpha():  # se sono dai marcatori
        inizio = goal
        while inizio == 0:
            #print(temp[inizio+i], i)
            marcatori.append(temp[inizio+i])
            inizio -= 1
        #print(marcatori)
        if marcatori not in dati:
            dati.append(marcatori)
#print(dati)

### punto 1 ###  trovare la coppia di squadre che hanno giocato più partite
with open("1.txt","w") as o:
    scontro = []
    for i in range(len(dati)):
        if i % 3 ==0:
            if dati[i].get("partita") not in scontro and (dati[i].get("partita").split("-")[1]+"-"+dati[i].get("partita").split("-")[0]) not in scontro:
                scontro.append(dati[i].get("partita"))
    massimo = 0
    Smassimo = ""
    for i in range(len(scontro)):
        scontroContrario = scontro[i].split("-")[1] + "-" + scontro[i].split("-")[0]
        conta = 0
        for j in range(len(dati)):
            if j % 3 == 0:
                if dati[j].get("partita") in scontro[i] or dati[j].get("partita") in scontroContrario:
                    conta+=1
        if conta>massimo:
            massimo = conta
            Smassimo = scontro[i]
    o.write(str(Smassimo.split("-")[0])+" e "+str(Smassimo.split("-")[1])+" giocano "+ str(massimo)+" volte")
### punto 2 ###
with open("2.txt","w",encoding="utf-8") as o:
    # goal = int(temp[i].split("-")[0]) + int(temp[i].split("-")[1])
    squadra = []
    for i in range(len(dati)):
        if i%3==0:
            squadra.append(dati[i].get("partita").split("-")[0])
            squadra.append(dati[i].get("partita").split("-")[1])
    squadra = list(set(squadra))
    rosa = dict(zip(squadra,[[]]*len(squadra)))
    for i in range(len(dati)):
        controllo = False
        if i % 3 == 0:
            t1 = []
            t2 = []
            Squad1 = dati[i].get("partita").split("-")[0]
            Squad2 = dati[i].get("partita").split("-")[1]
            goalSquad1 = int(dati[i + 1].get("punteggio").split("-")[0])
            goalSquad2 = int(dati[i + 1].get("punteggio").split("-")[1])
        if len(dati[i])>1:
            for j in range(goalSquad1):
                if dati[i][j] not in t1:
                    t1.append(dati[i][j])
            for j in range(goalSquad2):
                if dati[i][j+goalSquad1] not in t2:
                    t2.append(dati[i][j+goalSquad1])
            if rosa[Squad1].count(t1) == 0:
                p1 = rosa.get(Squad1)+t1
                rosa[Squad1] = p1
            if rosa[Squad2].count(t2) == 0:
                p2 = rosa.get(Squad2)+t2
                rosa[Squad2] = p2
    for i in rosa.keys():
        massimo = 0
        giocatore_massimo = ""
        for k in rosa.get(i):
            conta = 0
            if k in rosa.get(i):
                conta = rosa.get(i).count(k)
            if conta>massimo:
                massimo = conta
                giocatore_massimo = k
        o.write("("+i+")"+giocatore_massimo+"["+ str(massimo)+"]\n")
### punto 3 ###
with open("3.txt","w",encoding="utf-8") as o:
    giocatori = []
    for i in range(len(dati)):
        if len(dati[i]) > 1:
            for j in range(len(dati[i])):
                if dati[i][j] not in giocatori:
                    giocatori.append(dati[i][j])
                    giocatori.append(int(0))
    # print(giocatori) #dentro giocatori ho tutti i giocatori che hanno segnato almeno 1 goal
    massimo = 0
    PiuGoal = ""
    for i in range(len(giocatori)):
        if i%2==0:
            conta = 0
            for j in range(len(dati)):
                if len(dati[j])>1:
                    for k in range(len(dati[j])):
                        if giocatori[i] == dati[j][k]:
                            conta += 1
            giocatori[i+1] = conta
            if conta>massimo:
                massimo = conta
                PiuGoal = giocatori[i]
    o.write(PiuGoal +" è il giocatore più prolifico [" +str(massimo)+" goal]")
### punto 4 ###
goal_contro = {}
print(giocatori)
for i in range(len(giocatori)):
    if i%2==0:
        goal_contro[giocatori[i]] = []
print(goal_contro)
### punto 5 ###