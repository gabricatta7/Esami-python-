elenco={}

op = 0

Chiedi = True

while Chiedi:
    print('-------------------------')
    print('1. inserisci studente')
    print('2. inserisci voto/i dello studente')
    print('3. stampa tutto')
    print('4. stampa media voti classe')
    print('5. esci')
    print('-------------------------')
    #chiedo operazione
    op = int(input('Che operazione vuoi fare: '))
    
    #valuto operazione
    if op == 1:     
        #inserisco studente in lista e abbino 0 come media
        nome = input('nome: ')
        cognome = input('cognome: ')
        nome_cognome = nome+' '+cognome
        elenco[nome_cognome] = []
    
    elif op == 2:
        #verifico se studente è in lista e se si aggiungo un voto
        nome = input('nome da cercare: ')
        cognome = input('cognome da cercare: ')
        nome_cognome = nome+' '+cognome
        if nome_cognome in elenco:
            elenco[nome_cognome].append(float(input("------>"+"Che voti dare a "+nome_cognome+"?")))
        else:
            print("nome non trovato")


    elif op == 3:
        #stampa nome e voto in ordine crescente tra gli studenti
        for key, value in elenco.items():
            print (key, "---->", sorted(value))
        


    elif op == 4:
        medie = []
        #faccio media classe
        for key, value in elenco.items():
            m = sum(value)/len(value)
            print(key, '---->', value)
            medie.append(m)
        print("media classe è ----> ",sum(medie)/len(medie))

    #se 5 esci
    elif op == 5:
        Chiedi = False
   
    else:
        print("op non valida")
        continue







    