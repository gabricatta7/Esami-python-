'''Le righe che non iniziano con la stringa "-->" sono da considerarsi strade "di partenza"
Le righe che iniziano con la stringa "-->" sono da considerarsi strade "di arrivo".
Quindi ad esempio Da Via Emilia posso andare in Via Amendola. Mentre da Via Amendola posso andare in Via Botti e in Via Castello.
Il programma deve funzionare per ogni file di ingresso che rispetti la sintassi descritta

Il programma deve calcolare le informazioni richieste nei punti seguenti. Per ogni punto il programma crea un file di testo chiamato rispettivamente 1.txt,2.txt,3.txt,4.txt,5.txt in cui scrivere la risposta
I punti da calcolare sono (Ogni punto vale 6 punti all'esame.):

    Per ogni via stampare il numero di vie che portano ad essa (es., Via Emilia=0, Via Amendola=1, Via Botti=1, Via Castello=1)
    Stampare tutte le vie senza ripetizioni (anche quelle solo a destra delle freccia – es., via Botti)
    Trovate la via dalla quale si possono raggiungere più altre vie (cioè la via che compare più spesso a sinistra delle frecce)
    Partendo da Via Emilia si può arrivare in Via Botti? Stampare una delle strade possibili. (si può assumere di poter passare al massimo per 10 vie)
    Scrivere una tabella che mostra il grafo delle vie.
    Da\A Via Emilia Via Amendola Via Botti ...
    Via Emilia    false        true     false ...
    Via Amendola    false        false     true ...
    Via Botti false false false ...
    ...     ...     ...     ... ...'''

#struttura dati 
Navigazione = {}
with open ('input.txt') as file:
    linee = file.readlines()
    for linea in range(len(linee)):
        strLinea = linee[linea].strip()         
        if linee[linea].strip()[0] == "V":
            viaPartenza = strLinea[4:]
            Navigazione[viaPartenza] = []
                        
        if linee[linea].strip()[0] == "-":
            vieArrivo = []
            x = True
            i = 0 
            while x:
                i += 1
                if linee[linea-i].strip()[0] == 'V':
                    viaArrivo = strLinea[8:]
                    chiave = str(linee[linea-i].strip()[4:])
                    Navigazione[chiave].append(viaArrivo)
                    x = False
                elif linee[linea-i].strip()[0] == '-':
                    vieArrivo.append(str(linee[linea].strip()[6:]))
                    continue
print(Navigazione)
   
#punto 1 
count = {}
p1 = open('1.txt','w')
for viaPart in list(Navigazione.keys()):
    for viaArr in list(Navigazione[viaPart]):
        count[viaArr] = 0
        if viaPart not in count:
            count[viaPart] = 0
for viaPart in list(Navigazione.keys()):
    for via in list(count.keys()):
        if via in Navigazione[viaPart]:
            count[via] += 1       
for key in list(count.keys()):
    p1.write(key+'='+str(count[key])+'\n')
p1.close()




#punto due
p2 = open('2.txt','w')
for key in list(count.keys()):
    p2.write(key+'\n')
p2.close()


    
#punto 3
maxVieRagg = 0
viaMax = 0 
for key in list(Navigazione.keys()):
    vieRagg = len(Navigazione[key])
    if maxVieRagg < vieRagg:
        maxVieRagg = vieRagg
        viaMax = key
p3 = open('3.txt','w')
p3.write('la via connessa a più vie è: '+viaMax)
p3.close()


#punto 4
p4 = open('4.txt','w')
def VaiBotti(viaArg):
    if 'Botti' in Navigazione[viaArg]:
        p4.write('Prendi Via Botti')    
    else:
        for via in Navigazione[viaArg]:
            if via in list(Navigazione.keys()):
                
                if 'Botti' in Navigazione[via]:
                    p4.write(viaArg+'->'+via+'->'+'Via Botti') 
                else:
                    p4.write('non ci puoi arrivare')
            else:
                p4.write('non ci puoi arrivare')
VaiBotti('Emilia')



 


