from guizero import *
import collections
import pprint as pp
def f1(txt):
    output_txt = ""
    vittorie_squadra = {}
    # Trovare squadra che ha vinto più partite DONE
    outot.value = ">Punto1: Trovare squadra che ha vinto più partite"

    for partita in list(partite.keys()):
        if partite[partita]["sq1"] not in vittorie_squadra:
            vittorie_squadra[partite[partita]["sq1"]] = 0
        if partite[partita]["sq2"] not in vittorie_squadra:
            vittorie_squadra[partite[partita]["sq2"]] = 0

        if partite[partita]["punteggio"][0] > partite[partita]["punteggio"][1]:
            vittorie_squadra[partite[partita]["sq1"]] += 1
        elif partite[partita]["punteggio"][0] < partite[partita]["punteggio"][1]:
            vittorie_squadra[partite[partita]["sq2"]] += 1
        elif partite[partita]["punteggio"][0] == partite[partita]["punteggio"][1]:
            vittorie_squadra[partite[partita]["sq1"]] += 1
            vittorie_squadra[partite[partita]["sq2"]] += 1
    # print(vittorie_squadra)
    maxVittorie = ""
    a = max(vittorie_squadra, key=vittorie_squadra.get)
    #print("La squadra che ha vinto più partite e\': ",a)
    output_txt += f'La squadra che ha vinto più partite è: {a}'
    tout.value = output_txt

    app.after(5000, p2)
    app.after(10000, p3)
    app.after(15000, p4)

def riduci():
    giocatore = {}
    for partita in list(partite.keys()):
        if partite[partita]["sq1"] not in giocatore:
            giocatore[partite[partita]["sq1"]] = []
            giocatore[partite[partita]["sq1"]].append(partite[partita]["gol1"])
        elif partite[partita]["sq1"] in giocatore:
            giocatore[partite[partita]["sq1"]].append(partite[partita]["gol1"])
        if partite[partita]["sq2"] not in giocatore:
            giocatore[partite[partita]["sq2"]] = []
            giocatore[partite[partita]["sq2"]].append(partite[partita]["gol2"])
        elif partite[partita]["sq2"] in giocatore:
            giocatore[partite[partita]["sq2"]].append(partite[partita]["gol2"])
    return(giocatore)

def p2():

    output_txt = ""
    outot.value = f"> Punto 2: Per ogni squadra, selezionare il giocatore che ha fatto più gol"

    #print("--> Punto 2:Per ogni squadra, selezionare il giocatore che ha fatto più gol")
    lista = riduci()


    for n_partita, goleador in lista.items():
        # print(n_partita)
        # print(goleador)
        for gol in goleador:
            parta = []
            for g_gol in gol:
                # print(g_gol)
                parta.append(g_gol)
        # print(parta)
        countgol = collections.Counter(parta)
        #print('Il giocatore che ha segnato di più per la', n_partita, 'è:', max(countgol, key=countgol.get))
        #parta = []
        a = max(countgol, key=countgol.get)
        output_txt += f'Il giocatore che ha segnato di più per la {n_partita} è: {a}\n'
        tout.value = output_txt

def p3():
    #print('3')
    output_txt = ""
    outot.value = f"> Punto 3: Trovare il giocatore che ha più doppiette (due goal nella stessa partita)"

    #print("--> Punto 3: Trovare il giocatore che ha più doppiette (due goal nella stessa partita)")
    lista = riduci()
    doppietta = []
    doppiette = []
    doppiette_Calciatore = 0
    for n_partita, goleador in lista.items():
        # print(n_partita)
        # print(goleador)
        for gol in goleador:
            # print(gol)
            countdop = collections.Counter(gol)
            # print(countdop)
            for k, v in countdop.items():
                if v == 2:
                    # print('Punto 3: Il ghiocatore che ha segnato una doppietta per la', n_partita, 'è:', k)
                    doppiette.append(k)
        #print(doppiette)
    countdopt = collections.Counter(doppiette)
    #print('Il giocatore che ha segnato più doppiette è:', max(countdopt, key=countdopt.get))
    a = max(countdopt, key=countdopt.get)
    #print(a)
    output_txt += f'Il giocatore che ha segnato più doppiette è: {a}\n'
    tout.value = output_txt


def p4():
    #print('4')
    output_txt = ""
    outot.value = f"> Punto 4: Per ogni giocatore, indicare le squadre contro cui ha fatto gol"
    #print("--> Punto 4: Per ogni giocatore, indicare le squadre contro cui ha fatto gol")
    calciatore = {}
    for partita in list(partite.keys()):
        if partite[partita]["sq2"] not in calciatore:
            calciatore[partite[partita]["sq2"]] = []
            calciatore[partite[partita]["sq2"]].append(partite[partita]["gol1"])
        elif partite[partita]["sq1"] in calciatore:
            calciatore[partite[partita]["sq2"]].append(partite[partita]["gol1"])
        if partite[partita]["sq1"] not in calciatore:
            calciatore[partite[partita]["sq1"]] = []
            calciatore[partite[partita]["sq1"]].append(partite[partita]["gol2"])
        elif partite[partita]["sq1"] in calciatore:
            calciatore[partite[partita]["sq1"]].append(partite[partita]["gol2"])
    # print(calciatore)
    sqGol = []
    for n_partita, goleador in calciatore.items():
        # print(n_partita)
        # print(goleador)
        for gol in goleador:
            for g_gol in gol:
                # print(g_gol)
                if g_gol not in sqGol:
                    sqGol.append(g_gol)
        #print(f'La/Il {n_partita} ha subito gol dal/i giocatore/i:')
        #print(*sqGol, sep=",")
        output_txt += f'La/Il {n_partita} ha subito gol dal/i giocatore/i:\n'
        for i in range(len(sqGol)):
            output_txt += f'{sqGol[i]}  '
        output_txt +='\n'
        sqGol = []

        tout.value = output_txt



app=App(title="ODIO IL CALCIO",width=600)
Text(app,text="inserisci una lista di partite (- e ,):")
input_base='''Juve-Milan
3-2
Higuain,Dybala,Higuain-Niang,Niang

Napoli-Roma
1-2
Insigne-Totti,Totti

Milan-Juve
1-2
Niang-Higuain,Higuain
'''
outo="OUTPUT"
tin= TextBox(app,text=input_base, width=40, height=12, multiline=True)
outot = Text(app,text=outo)
tout= TextBox(app, width=50, height=10, multiline=True)
txt= tin.value
linee=txt.splitlines()

buffer = []
partite = {}
tempSTR = ""
for riga in linee:
    if len(riga) > 0:
        buffer.append(riga)
        #print(buffer)
    elif len(riga) == 0:
        tempSTR = buffer[0].split("-")
        tempSTR2 = buffer[2].split("-")
        #print(tempSTR)
        #print(tempSTR2)
        partite[buffer[0]] = {
            "sq1": tempSTR[0],
            "sq2": tempSTR[1],
            "punteggio": buffer[1].split("-"),
            "gol1": tempSTR2[0].split(","),
            "gol2": tempSTR2[1].split(",")
        }
        buffer = []
pp.pprint(partite)
PushButton(app,text='run', width=15, command=f1, args=[partite])
app.display()