'''Realizzare un programma Python che elabori un file di testo che contiene informazioni relative a un insieme di ricette.
Torta di Mele,Mele,4,Zucchero,5,Farina,6,Uova,2

Spaghetti in Bianco,Spaghetti,100
Ogni ricetta è su una linea e ci possono essere linee vuote. Separati da "," sono nome della ricetta, ingredienti e quantità
Il programma deve funzionare per ogni file di ingresso che rispetti la sintassi descritta
Il programma deve calcolare le informazioni richieste nei punti seguenti. Per ogni punto il programma crea un file di testo chiamato rispettivamente 1.txt,2.txt,3.txt,4.txt,5.txt in cui scrivere la risposta
I punti da calcolare sono (Ogni punto vale 6 punti all'esame.):

Scrivere la composizione di ogni ricetta in percentuale (es. Torta di Mele: 20% Farina, 60% Mele, 20% Zucchero)
Per ogni ricetta stampare quanti sono i suoi ingredienti
Trovare le ricette che condividono almeno 2 ingredienti
Trovare l'ingrediente associato al maggior numero di ricette
Scrivere una tabella ricetta-ingrediente che associa le ricette agli ingredienti con valore true/false a seconda che la ricetta sia associata o meno a tale ingrediente.'''

from guizero import *
import math

app = App(title='rciette',height=600, width=900)

inputBase = '''Torta di Mele,Mele,4,Zucchero,5,Farina,6,Uova,2

Spaghetti in Bianco,Spaghetti,100,Farina,6,Uova,2'''

input = Text(app,text='INPUT')
inputBox = TextBox(app, text=inputBase, multiline=True, height=10,width=200)
output = Text(app,text='OUTPUT')
outputBox = TextBox(app,text='', multiline=True,height=10,width=200)

def ris():
    #CREAIONE STRUTTURA DATI
    ricette = {}
    txt = inputBox.value
    linee = txt.splitlines()

    for linea in linee:
        linea = linea.split(',') 
        if len(linea)>1:
            ricetta = linea[0]
            ricette[ricetta]= {}

            for i in range(len(linea)):
                if list(linea[i])[0] == str(0) or list(linea[i])[0] == str(1) or list(linea[i])[0] == str(2) or list(linea[i])[0] == str(3) or list(linea[i])[0] == str(4) or list(linea[i])[0] == str(5) or list(linea[i])[0] == str(6) or list(linea[i])[0] == str(7) or list(linea[i])[0] == str(8) or list(linea[i])[0] == str(9):
                    linea[i] = int(linea[i])
                if type(linea[i]) != int and linea[i] != ricetta:
                    Ingr = linea[i]
                    ricette[ricetta][Ingr] = 0
                if type(linea[i]) == int:
                    QuantitaIngr =  linea[i]
                    ricette[ricetta][linea[i-1]] = QuantitaIngr

    #.------------------------PUNTO 1----------------------.
    def punto1(ricette):
        outputTesto = ''
        for t in ricette:
            #print(list(ricette[t].values())) 
            totaleIngr = sum(list(ricette[t].values()))
            #print(totaleIngr)
            #percentuale singolo ingrediente
            outputTesto += f"{t}:"
            for i in ricette[t]:
                percIngr = ricette[t][i] * 100 / totaleIngr
                #arrotondo a una cifra 
                percIngr = round(percIngr,1)
                if i == list(ricette[t].keys())[-1]:
                    outputTesto += f'{percIngr}% di {i}. '
                else:
                    outputTesto += f'{percIngr}% di {i}, '

                outputBox.value = outputTesto
            outputTesto += "\n"
        
            
    #.------------------------PUNTO 2----------------------.
    def punto2():
        outputTesto = ''
        for t in ricette:
            #print(len(list(ricette[t])))
            outputTesto += f'{t} ha {len(list(ricette[t]))} ingredienti \n'
        outputBox.value = outputTesto
        app.after(2000,punto3)

    #.------------------------PUNTO 3----------------------.
    def punto3():
        
        listaRicetteIngrComuni= []
        for t in ricette:
            listaIngrUnici = []
            for j in ricette:
                contoIngredientiincomune = 0
                if t == j or j == t:
                    pass
                
                else:
                    for i in ricette[t]:
                        if i in ricette[j]:
                            contoIngredientiincomune += 1
                            if contoIngredientiincomune >= 2:
                                listaRicetteIngrComuni.append(f'{t} con {j}')
        
        if len(listaRicetteIngrComuni)>0:
            outputBox.value = listaRicetteIngrComuni
        else: 
            outputBox.value = 'non ci sono ricette con ingredienti comuni'

    #CHIEDERE AGLI ALTRI PUNTO 4


                        

    punto1(ricette)

    app.after(2000,punto2)

    


    print(ricette)
    
        
button = PushButton(app,text='run',command=ris)
app.display()