def letter_counter(text):
    dict = {}
    for i in text:
        dict[i] = text.count(i)
    return dict

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

with open("dati.txt") as f:
    mat = f.read().split("\n")
    ris = []
    for elem in mat:
        ris.append(elem.split(" "))
#print(mat)
#print(ris)

##### punto 1 ######
with open("1.txt","w") as o:
    parola_da_cercare = "marco"
    parola_da_cercare = parola_da_cercare.lower()
    o.write("ricerca in orizzontale")
    for i in mat:
        i = i.replace(" ","").lower()
        trovato = False
        temp = i.find(parola_da_cercare)
        if temp != -1:
            trovato = True
        o.write("\n"+str(trovato))
    o.write("\nricerca in verticale")
    for i in range(len(ris)):
        trovato = False
        parola = ""
        for j in range(len(ris)):
            parola = parola + str(ris[j][i])
        temp = parola.lower().find(parola_da_cercare)
        if temp != -1:
            trovato = True
        o.write("\n"+str(trovato))
##### punto 2 ######
    with open("2.txt","w") as o:
        colonne = []
        for i in range(len(ris)):
            trovato = False
            parola = ""
            for j in range(len(ris)):
                parola = parola + str(ris[j][i])
            colonne.append(parola)
        for i in range(len(colonne)):
            for j in range(len(colonne)):
                if colonne[i] == colonne[j] and j!=i:
                    o.write(str(colonne[i])+"\n")
###### punto 3 #######
    with open("3.txt","w") as o:
        test = ""
        parole = ""
        for i in range(len(ris)):
            parola = ""
            for j in range(len(ris)):
                parola = parola + str(ris[j][i]+ "")
            parole = parola + parole
        o.write(str(letter_counter(parole)))
###### punto 4 ######
    with open("4.txt","w") as o:
        col = [*zip(*ris)]
        parole = []
        for i in range(len(col)):
            p = ""
            for j in range(len(col)):
                p = p + str(col[i][j]).lower()
            #print(p)
            parole.append(p)
        #print(parole)
        for i in range(97,123):
            o.write("\n"+"lettera(" + str(chr(i)) + "):")
            for k in range(len(parole)):
                if chr(i) in parole[k]:
                    o.write("\n"+str(k+1)) #il +1 serve per un controllo più "umano" perchè la colonna 1 sarebbe la 0
###### punto 5 ######
    with open("5.txt","w") as o:
        compare = 0
        #controllo orizzontale
        for i in mat:
            i = i.replace(" ", "").lower()
            if "marco" in i:
                compare +=1
        #controllo verticale
        for i in range(len(parole)):
            if "marco" in parole[i]:
                compare += 1
        #controllo diagonale principale
        d1 = ""
        for i in range(len(ris)):
            for j in range(len(ris)):
                if (i == j):
                    d1 = d1 + str(ris[i][j]).lower()
        if "marco" in d1:
            compare += 1
         #controllo diagonale secondaria
        d2 = ""
        for i in range(len(ris)):
            for j in range(len(ris)):
                if (i+j==len(ris)-1):
                    d2 = d2 + str((ris[i][j])).lower()
        if "marco" in d2:
            compare += 1
        o.write("la parola marco compare:"+str(compare)+" volte")
''' diagonale principale
for i in range(len(ris)):
    print("\n")
    for j in range(len(ris)):
        if (i == j):
            print(ris[i][j])
'''