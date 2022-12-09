from guizero import *
app = App(title='regisstro', layout='grid')
elenco = {}

    
def op1():
    def check_studente(x,y):        #check se studente è in elenco e se non lo è lo aggiungo
        nome_cognome = x.value+' '+y.value
        if nome_cognome not in elenco:
            elenco[nome_cognome] = []
            app2.destroy()
        else:
            app2.destroy()   
    app2 = Window(app, layout='grid')
    nome = Text(app2, text='nome:', grid=[0,0])
    cognome = Text(app2, text='cognome:', grid=[0,1])
    nome_box = TextBox(app2, grid = [1,0])
    cognome_box = TextBox(app2, grid = [1,1])
    b = PushButton(app2, text='invio', grid=[1,2], command=check_studente, args=[nome_box,cognome_box])

def op2():
    def check_insvoto(x,y,z):   #check se studente è in elenco e se c'è gli aggiungo un voto
        nome_cognome = x.value+' '+y.value
        voto = z.value
        if nome_cognome in elenco:
            elenco[nome_cognome].append(float(voto))
            app3.destroy()
        else:
            error = Text(app3, text='studente non trovato!!!', grid=[3,4])
            app3.destroy()

    app3 = Window(app, layout='grid')
    nome = Text(app3, text='nome:', grid=[0,0])
    cognome = Text(app3, text='cognome:', grid=[0,1])
    voto = Text(app3, text='voto:', grid=[0,2])
    nome_box = TextBox(app3, grid = [1,0])
    cognome_box = TextBox(app3, grid = [1,1])
    voto_box = TextBox(app3, grid = [1,2])
    b = PushButton(app3, text='invio', grid=[1,3], command=check_insvoto, args=[nome_box,cognome_box,voto_box])

def op3():
    app4 = Window(app, layout='grid')
    i = 1 
    for key, value in elenco.items():   #ciclo per stampe di ogni key (e i suoi valori) presente in elenco
        stampa_nome = Text(app4, text=key, grid=[0,i])
        stampa_freccia = Text(app4, text= '----->', grid=[1,i])
        stampa_voti = Text(app4, text=str(sorted(value)), grid=[2,i])
        i += 1

def op4():
    app5 = Window(app, layout='grid')
    medie = []
    for key, value in elenco.items():   #ciclo per calcolo medie di ogni singolo studente
        m = sum(value)/len(value)
        medie.append(m)
    media_classe = sum(medie)/len(medie)    #calcolo media di tutta la classe
    media_classe_stampa=Text(app5, text='La media della classe è:  ', grid=[0,0])
    media_classe_valore = Text(app5, text=str(media_classe), grid=[1,0]) 

def op5():
    app.destroy()


#bottoni per chiamare le varie funzioni
button_student = PushButton(app, text='inerisci studente', grid=[0,0],command=op1)
button_checkvote = PushButton(app, text='inserisci voto', grid=[0,1],command=op2)
button_print = PushButton(app, text='stampa tutto', grid=[0,2],command=op3)
button_aritm = PushButton(app, text='calcola media', grid=[0,3], command=op4)
button_exit = PushButton(app,text='esci', grid=[0,4], command=op5)

app.display()
