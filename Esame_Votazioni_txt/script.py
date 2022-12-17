# d indica i dati.txt grezzi
import operator

with open("dati.txt") as f:
    d = f.read().split("\n")
votazioni = []
citta = {}
k = 0
index = 0
for i in range(0,len(d),4):
    citta[d[i]] = None        #aggiungo la chiave città senza i valori che estraggo dopo
    k += 1              #lunghezza delle mie chiavi del dizionario
for i in range(0,len(d)-k):
    if d[i] in citta.keys():
        d.remove(d[i])

for i in range(len(d)):
    if i % 3 == 0:
        for j in range(3):
            votazioni.append(d[j+i])
        k+=1

k = 1  #uso k come variabile temporanea per estrarre correttamente gli indici
for i in citta.keys():
    index = list(citta).index(i)
    citta.update({i:votazioni[3*index:3*k]})
    k += 1


########## punto 1 ###############
with open("1.txt","w",encoding="utf8") as o:
    max = 0
    cMax = ""  # citta massima / contatto massimo
    for i in citta.keys():
        somma = 0
        for j in range(len(citta)):
            somma += float(citta.get(i)[j][-5:-1])
        if somma > max:
            max = somma
            cMax = i
    o.write("la città dove si è voltato di più è: "+ str(cMax)+"("+str(max)+"%)")
########## punto 2 ###############
with open("2.txt","w",encoding="utf8") as o:
    max = 0
    for i in citta.keys():
        cMax = ""
        for j in range(len(citta)):
            perc = float(citta.get(i)[j][-5:-1])
            if perc > max:
                max = perc
    for i in citta.keys():
        for j in range(len(citta)):
            if citta.get(i)[j].find(str(max)) != -1:
                o.write(citta.get(i)[j])
########## punto 3 ###############
with open("3.txt", "w", encoding="utf8") as o:
    for i in citta.keys():
        somma = 0
        for j in range(len(citta)):
            somma += float(citta.get(i)[j][-5:-1])
        o.write(i + " " + str(somma)+"\n")
########## punto 4 ###############          non funziona il punto 4...
with open("4.txt", "w", encoding="utf8") as o:
    partiti = []
    for i in citta.keys():
        for j in range(len(citta)):
            if citta.get(i)[j].split(", ")[1] not in partiti:
                partiti.append(citta.get(i)[j].split(", ")[1])
    print(partiti)
    for i in range(len(partiti)):
        o.write(partiti[i]+" ") # stampa prima riga
    #################### parte consigliata dal prof (che non funziona) ########################
    for city in citta.keys():
        for p in partiti:
            if p in citta.get(city):
                print("aaaaa")
                #print(citta[city][p].split(", ")[1],end="")
            else:
                print(0,end="")
            print("")
#################### devo ordinare in base ai risultati ########################
    for i in citta.keys():
        primo = 0
        secondo = 0
        terzo = 0
        o.write("\n"+i)
        for j in range(len(citta)):
            if float(citta.get(i)[j][-5:-1]) > primo:
                terzo = secondo
                secondo = primo
                primo = float(citta.get(i)[j][-5:-1])
            elif float(citta.get(i)[j][-5:-1])>secondo:
                terzo = secondo
                secondo = float(citta.get(i)[j][-5:-1])
            else:
                terzo = float(citta.get(i)[j][-5:-1])
        for j in range(len(citta)):
            if primo == 0 or secondo == 0 or terzo == 0:
                if float(citta.get(i)[j][-5:-1])>primo:
                    terzo = secondo
                    secondo = primo
                    primo = float(citta.get(i)[j][-5:-1])
                elif float(citta.get(i)[j][-5:-1])>secondo:
                    terzo = secondo
                    secondo = float(citta.get(i)[j][-5:-1])
                else:
                    terzo = float(citta.get(i)[j][-5:-1])
        print(primo, secondo, terzo)

########## punto 5 ###############
with open("5.txt", "w", encoding="utf8") as o:
    ordine = {}
    for i in citta.keys():
        for j in range(len(citta)):
            ordine[citta.get(i)[j].split(", ")[0]]=float(citta.get(i)[j][-5:-1])
    #ordine.sort(reverse=True)
    d_ordinato = sorted(ordine.items(),key=operator.itemgetter(1),reverse=True)
    for i in range(len(d_ordinato)):
        o.write(str(d_ordinato[i])+"\n")