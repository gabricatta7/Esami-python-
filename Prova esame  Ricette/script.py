from guizero import *


app = App(title='ricette')



inputBase = '''Ricetta:Torta di Mele
Ingrediente:Mele,4
Ricetta:Torta di Mele
Ingrediente:Zucchero,5
Ricetta:Spaghetti in Bianco
Ingrediente:Spaghetti,100
Ricetta:Torta di Mele
Ingrediente:Farina,6
Ricetta:Torta di Mele
Ingrediente:Uova,2'''


input = Text(app,text='INPUT')
inputBox = TextBox(app, text=inputBase, multiline=True, height=10,width=30)
output = Text(app,text='OUTPUT')
outputBox = TextBox(app,text='', multiline=True,height=10,width=30)
    



def ris():
    ricette = {}
    txt = inputBox.value
    linee = txt.splitlines()
    print(linee)
    for i in range(len(linee)):
        if linee[i].startswith('R'):
            #creo chiavi
            ricetta = linee[i].split(':')[1]
            #creo izionario e dizionario interno
            if ricetta not in ricette.keys():
                ricette[ricetta] = {}
        if linee[i].startswith('I'):
            ListIngredienteFalsa = linee[i].split(':')
            ListIngredienteVera = ListIngredienteFalsa[1].split(',')
            chiave = linee[i-1].split(':')[1]
            ricette[chiave][ListIngredienteVera[0]] = ListIngredienteVera[1]
    # for j in:
    # valori = ricette[chiave]
    # print(valori)
    print(ricette)

    

    outputTesto = ''
    for j in ricette:
        maxIngrValore = 0
        maxIngr = ''
        for k in ricette[j]:
            if int(ricette[j][k])>= int(maxIngrValore):
                maxIngrValore = ricette[j][k]
                maxIngr = k
        outputTesto += f"{maxIngr} : {maxIngrValore}\n"
        outputBox.value = outputTesto
    for t in ricette:
        
        for j in ricette:
            for k in ricette[j]:
                
                if k in ricette[t]:
                    count += 1

button = PushButton(app,text='run',command=ris)


app.display()


