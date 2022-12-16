def parse(l):
    s = l.strip().split(' ') #fa qualcosa di magico qui di irrisolvibile
    data = s[0]
    da = s[1]
    a = s[2]
    testo = s[3]
    for i in range(4, len(s)):
        testo += " " + s[i]
    return {'data': data.split(':')[1], 'da': da.split(':')[1], 'a': a.split(':')[1], 'testo': testo.split(':')[1]}

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

# ris contiene una lista di dizionari chiave-valore
# msg è il messaggio grezzo con troppi spazzi bianchi
# messaggio contiene le varie righe divise per i \n ma non ancora suddivise per chiave valore
# contatto contiele il mittente e il destinatario in ordine senza elimare i duplicati
with open("dati2.txt") as f:
    messaggio = []
    k = ""
    msg = f.read().rsplit("\n")
    msg = [i for i in msg if i]
    #while ("" in msg):  # scorre tutti gli elementi per eliminare gli spazi vuoti
    #    msg.remove("")
    for i in range(len(msg)):
        mes = " ".join(msg[i].split()) # per qualche motivo arcano non ci sono più gli spazi bianchi extra
        messaggio.append(mes) #tutti i messaggi "puliti sono stati messi nella lista messaggio"
    #print(messaggio)
    ris = []
    for i in range(len(messaggio)):
        sep = parse(messaggio[i])
        ris.append(sep)
    #print(ris)

    ###### punto 1 ######
with open("1.txt","w") as o:
    for i in range(1,13):
        conta = 0
        o.write("mese"+str(i)+":")
        for j in range(len(ris)):
            mese = (ris[j].get("data").split("-")[1])
            if int(mese) == i:
                conta+=1
        o.write(str(conta) + "\n")
    ###### punto 2 ######
with open("2.txt","w") as o:
    mittente = []
    destinatario = []
    contatto = []
    date = []
    d = []
    t = []
    conta = 1
    for i in range(len(ris)): # salvo tutte le mittente che hanno ricevuto un mex
        if ris[i].get("da") not in mittente:
            mittente.append(ris[i].get("da"))
    for i in range(len(ris)):
        if ris[i].get("a") not in destinatario:
            destinatario.append(ris[i].get("a"))

    for i in range(len(ris)):
        c = ris[i].get("da") + "-" + ris[i].get("a")
        if c not in contatto:
            contatto.append(c)
        temp =ris[i].get("data") + " " + c
        d.append(ris[i].get("data"))
        date.append(temp)
    for i in range(len(mittente)):
        conta = 0
        for j in range(len(ris)):
            if contatto[j].startswith(mittente[i]):
                conta += 1
        o.write("\n"+mittente[i]+" scrive a "+str(conta)+" persone")

    ###### punto 3 ######
with open("3.txt","w") as o:
    massimo = 0
    m = ""
    z = []
    for i in range(len(ris)):
        z.append(ris[i].get("da"))
    try:
        for i in range(len(z)):
            if z[i] == z[i+1]:
                pass
            else:
                if countX(z,z[i]) > massimo:
                    massimo = countX(z,z[i])
                    m = z[i]
    except:
        print("")
    o.write(str(m)+" compare "+ str(massimo)+ " volte")
    ###### punto 4 ######
with open("4.txt","w") as o:
    Mconta = 0
    try:
        #print(d)
        for i in range(len(date)):
            conta = 0
            #print(date[i][:10])
            for j in range(len(date)):
                if date[i][:10].count(d[j]) == 1:
                    conta += 1
            if conta == 1:
                Mconta += 1
            if Mconta == len(d):
                o.write("tutti i giorni si e' inviato un solo messaggio")
    except:
        print("")
    try:
        for i in range(len(date)):
            if ris[i].get("data")+" "+ris[i].get("da")+" "+ris[i].get("a") == ris[i+1].get("data")+" "+ris[i+1].get("a")+" "+ris[i+1].get("da"):
                o.write(ris[i].get("da")+" "+ris[i].get("a")+" "+ris[i].get("data")+"\n")
    except:
        print("")
    ###### punto 5 ######
    print("mammt")