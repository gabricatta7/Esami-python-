'''
Tempo per la Soluzione: 2 Ore
Realizzare un programma Python dotato di Interfaccia Grafica (GUI). La GUI presenta 2 caselle di testo e tanti pulsanti quanti sono i punti da eseguire.
La prima casella di testo serve per inserire delle informazioni. La seconda casella di testo serve per visualizzare il risultato delle operazioni
attivabili tramite i pulsanti.
Nella casella di testo di input posso scrivere informazioni come da esempio:
Pizza e Altro
XXX
30.5 euro
45.2,10.1

Francescana
XXXXX
200.2 euro
45.5,10.3
Per ogni ristorante ci sono 4 righe: il nome del ristorante, la categoria (numero di X -- da 1 a 5), il prezzo medio per persona (con virgola),
due numeri (con la virgola) che indicano le coordinate del ristorante sulla mappa. C'è una linea vuota tra un ristorante e l'altro.
Il programma deve permettere di inserire nell'interfaccia grafica dati conformi a quelli indicati e calcolare le informazioni richieste nei punti seguenti.
I punti da calcolare sono (Ogni punto vale 6 punti all'esame + 6 punti per la GUI.):

Stampare tutti i ristoranti a 5 stelle
Stampare la media dei prezzi dei ristornanti a 1,2,3,4,5 stelle (media per categoria)
Trovare tutte le coppie di ristoranti a 5 stelle che distano meno di 5 “unità” l’uno dall’altro
Per ogni categoria, trovare il ristorante più economico e quello più costoso di quella categoria
'''
import pprint
import math 
from guizero import *
app = App(title='Esame')

ristoranti = []

#creazione struttura dati 
class ristorante():
    def __init__(self, nome_rist, stelle, prezzo, posizione):
        self.nome = nome_rist
        self.pos = posizione
        self.stelle = stelle
        self.prezzo = prezzo
    def mostra_rist(self):
        print(self.nome)
        print(self.pos)
        print(len(self.stelle))
        print(self.prezzo)

        
def forma(testo):
    ristoranti = []
    txt = testo.strip()
    lines = txt.splitlines()
    for i in range(0, len(lines), 5):
        ristoranti.append(ristorante(lines[i], lines[i+1], float(lines[i+2].strip(" euro")), lines[i+3].split(',')))
        #print(lines[i], lines[i+1], lines[i+2], lines[i+3], sep=" - ")
    return ristoranti


#WORKA
#PUTNO1 Stampare tutti i ristoranti a 5 stelle
def punto1(ristoranti):
    ristoranti = forma(inputTesto.value)
    out.value = ''

    for i in range(len(ristoranti)):
        if len(ristoranti[i].stelle) == 5:
            out.value += f'il ristorante {ristoranti[i].nome} ha 5 stelle'

#PUNTO 2 Stampare la media dei prezzi dei ristornanti a 1,2,3,4,5 stelle (media per categoria)
def punto2(ristoranti):
    out.value = ''
    ristoranti = forma(inputTesto.value)
    prezziS1 = []
    prezziS2 = []
    prezziS3 = []
    prezziS4 = []
    prezziS5 = []
    #riempimento liste prezzi in base categoria 
    for i in range(len(ristoranti)):
        ristoranti[i].mostra_rist()
        if len(ristoranti[i].stelle) == 1:
            prezziS1.append(ristoranti[i].prezzo)
        elif len(ristoranti[i].stelle) == 2:
            prezziS2.append(ristoranti[i].prezzo)
        elif len(ristoranti[i].stelle) == 3:
            prezziS3.append(ristoranti[i].prezzo)
        elif len(ristoranti[i].stelle) == 4:
            prezziS4.append(ristoranti[i].prezzo)
        elif len(ristoranti[i].stelle) == 5:
            prezziS5.append(ristoranti[i].prezzo)
    #se nelle liste ce qualcosa output esiste
    if len(prezziS1) > 0:
        prezziS1 = sum(prezziS1)/len(prezziS1)
        out.value += f'{prezziS1} euro medi'
        print(prezziS1,'euro medi')
    if len(prezziS2) > 0:
        prezziS2 = sum(prezziS2)/len(prezziS2)
        print(prezziS2,'euro medi')
        out.value += f'{prezziS2} euro medi'
    if len(prezziS3) > 0:
        prezziS3 = sum(prezziS3)/len(prezziS3)
        print(prezziS3,'euro medi')
        out.value += f'{prezziS3} euro medi'
    if len(prezziS4) > 0:
        prezziS4 = sum(prezziS4)/len(prezziS4)
        print(prezziS4,'euro medi')
        out.value += f'{prezziS4} euro medi'
    if len(prezziS5) > 0:
        prezziS5 = sum(prezziS5)/len(prezziS5)
        #print(prezziS5,'euro medi')
        out.value += f'{prezziS5} euro medi'
    
    

def punto3(ristoranti):
    out.value = ''
    ristoranti = forma(inputTesto.value)
    
    # for i in range(len(ristoranti)):
    #     ristoranti[i].mostra_rist()
    
    #creazione categoria 5 stelle
    ristoranti5 = {}
    for i in range(len(ristoranti)):
        #print(ristoranti[i].nome)
        if len(ristoranti[i].stelle) == 5:
            ristoranti5[ristoranti[i].nome] = ristoranti[i].pos
    #controllo x e y di ogni componente di ristoranti a 5 stelle
    for i in list(ristoranti5.keys()):
        for j in list(ristoranti5.keys()):
            if i == j:
                pass
            elif (abs(float(ristoranti5[i][0])-float(ristoranti5[j][0])) < 5) or (abs(float(ristoranti5[i][1])-float(ristoranti5[j][1])) < 5):
                out.value += f'{i} e {j}'
    
    
                

def punto4(ristoranti):
    out.value = ''
    ristoranti = forma(inputTesto.value)
    prezziS1 = []
    prezziS2 = []
    prezziS3 = []
    prezziS4 = []
    prezziS5 = []
    #riempimento liste prezzi in base categoria 
    for i in range(len(ristoranti)):
        ristoranti[i].mostra_rist()
        if len(ristoranti[i].stelle) == 1:
            prezziS1.append(ristoranti[i].prezzo)
        elif len(ristoranti[i].stelle) == 2:
            prezziS2.append(ristoranti[i].prezzo)
        elif len(ristoranti[i].stelle) == 3:
            prezziS3.append(ristoranti[i].prezzo)
        elif len(ristoranti[i].stelle) == 4:
            prezziS4.append(ristoranti[i].prezzo)
        elif len(ristoranti[i].stelle) == 5:
            prezziS5.append(ristoranti[i].prezzo)
    
    #se nelle liste ce qualcosa output esiste plus check max e min prezzo nella categoria
    if len(prezziS1) > 0:
        for i in range(len(ristoranti)):
            if max(prezziS1) == ristoranti[i].prezzo:
                out.value += f'categ 1 stelle: piu caro è {ristoranti[i].nome}'
            if min(prezziS1) == ristoranti[i].prezzo:
                out.value += f'categ 1 stelle: meno caro {ristoranti[i].nome} \n'
    if len(prezziS2) > 0:
        for i in range(len(ristoranti)):
            if max(prezziS2) == ristoranti[i].prezzo:
                out.value += f'categ 2 stelle: piu caro è {ristoranti[i].nome}'
            if min(prezziS2) == ristoranti[i].prezzo:
                out.value += f'categ 2 stelle: meno caro {ristoranti[i].nome} \n'
    if len(prezziS3) > 0:
        for i in range(len(ristoranti)):
            if max(prezziS3) == ristoranti[i].prezzo:
                out.value += f'categ 3 stelle: piu caro è {ristoranti[i].nome}'
            if min(prezziS3) == ristoranti[i].prezzo:
                out.value += f'categ 3 stelle: meno caro {ristoranti[i].nome} \n'
    if len(prezziS4) > 0:
        for i in range(len(ristoranti)):
            if max(prezziS4) == ristoranti[i].prezzo:
                out.value += f'categ 4 stelle: piu caro è {ristoranti[i].nome}'
            if min(prezziS4) == ristoranti[i].prezzo:
                out.value += f'categ 4 stelle: meno caro {ristoranti[i].nome} \n'
    if len(prezziS5) > 0:
        for i in range(len(ristoranti)):
            if max(prezziS5) == ristoranti[i].prezzo:
                out.value += f'categ 5 stelle: piu caro è {ristoranti[i].nome}'
            if min(prezziS5) == ristoranti[i].prezzo:
                out.value += f'categ 5 stelle: meno caro {ristoranti[i].nome} \n'
                

inputBase = '''Francescana
XXXXX
200.2 euro
45.5,10.3

Bella Napuli
XXXXX
10 euro
40.5, 77.7

Fre
XXXXX
10 euro
10, 77.7
'''
inputTesto = TextBox(app, text=inputBase, multiline=True, width='fill', height=10)
out = TextBox(app, text='output', multiline=True, width='fill', height=10, enabled=False)
box = Box(app, layout='grid')

PushButton(box, grid=[0,0], text='Punto1', command=punto1, args=[ristoranti])
PushButton(box, grid=[1,0], text='Punto2', command=punto2, args=[ristoranti])
PushButton(box, grid=[2,0], text='Punto3', command=punto3, args=[ristoranti])
PushButton(box, grid=[3,0], text='Punto4', command=punto4, args=[ristoranti])

app.display()