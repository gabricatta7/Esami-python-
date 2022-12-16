def ColonnaUguale4(m1,j1,m2,j2):
    if len(m1) != len(m2):
        return False
    for i in range(len(m1)):
        if m1[i][j1] != m2[i][j2]:
            return False
    return True

def ColonnaUguale3(m1,m2,j2):
    for j in range(len(m1[0])):
        if ColonnaUguale4(m1,j,m2,j2):
            return True
    return False

def ColonnaUguale2(m1,m2):
    for j in range(len(m2[0])):
        if ColonnaUguale3(m1,m2,j):
            return True
    return False

def TutteColonneUguali(m1,m2):
    if len(m1[0]) != len(m2[0]):
        return False
    for j in range(len(m1[0])):
       if not ColonnaUguale3(m2,m1,j):
           return False
    for j in range(len(m2[0])):
       if not ColonnaUguale3(m1,m2,j):
           return False
    return True

def sudoku(m):
    s = sum(m[0])
    for r in m:
        if sum(r) != s:
            return  False
    for j in range(len(m[0])):
        sj = 0
        for r in m:
            sj += r[j]
        if sj != s:
            return False
    return True

matrici = {}
with open("dati.txt") as f:
    for l in f:
        l =l.strip()
        if len(l)>0:
            s = l.split(",")
            r = [int(s[i]) for i in range(1,len(s))]
            if s[0] in matrici:
                matrici[s[0]].append(r)
            else:
                matrici[s[0]] = [r]

################# punto 1 #######################
# in questo punto chiamo A la prima matrice. Stampare tutte le matrici che abbiano una colonna uguale ad una della matrice A
with open("1.txt","w") as o:
    key = list(matrici.keys())
    for i in range(1,len(key)):
        if ColonnaUguale2(matrici[key[0]],matrici[key[i]]):
            o.write(key[i]+"----->A\n")
################# punto 2 #######################
# per ogni matrice trovare la riga di somma massima
with open("2.txt","w") as o:
    for k,v in matrici.items():
        mo = sorted(v, key=lambda r:sum(r))
        o.write(k+str(mo[-1])+"\n")
################# punto 3 #######################
# in questo punto chiamo A la prima matrice. Stampare tutte le matrici i cui valori siano compresi in quelli della matrice A
with open("3.txt","w") as o:
    valA = []
    for r in matrici["A"]:
        for x in r:
            valA.append(x)
    key = list(matrici.keys())
    for i in range(1,len(key)):
        contenuta = True
        for r in matrici[key[i]]:
            if x not in valA:
                contenuta = False
        if contenuta:
            o.write(key[i]+"\n")
################# punto 4 #######################
# Stampare tutte le coppie di matrici che hanno le stesse colonne (senza duplicati)
with open("4.txt","w") as o:
    key = list(matrici.keys())
    for i in range(len(key)):
        for j in range(i+1,len(key)):
            if TutteColonneUguali(matrici[key[i]],matrici[key[j]]):
                o.write(key[i]+"---->"+key[j])

################# punto 5 #######################
# Stampare le matrici sudoku (anche non quadrate), cioè quelle per cui la somma di tute le righe edi tutte le colonne ha lo stesso valore
with open("5.txt","w") as o:
    for k,v in matrici.items():
        if sudoku(v):
            o.write(k+ " e' sudoku  \n")