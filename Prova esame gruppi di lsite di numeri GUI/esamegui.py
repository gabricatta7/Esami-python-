
from guizero import *

liste = {}
gruppi = {}

def quanti_pari(g):
    cont = 0
    for l in gruppi[g]:
        for x in liste[l]:
            if x % 2 == 0:
                cont += 1
    return cont

def punto4():
    # sg = sorted(gruppi.keys()...... 
    sg = sorted(gruppi.items(), key=lambda kv: quanti_pari(kv[0]))

    output_txt = ''
    for g,v in sg:
        output_txt += f'{g}-->{quanti_pari(g)}\n'
    tout.value = output_txt


#PUNTO 1
def palindromo(x):
    for i in range(len(x)):
        if x[i] != x[-1-i]:
            return False
    return True

def f1():
    txt = tin.value.strip()
    linee = txt.splitlines()
    # print(linee)
    analisi_liste = True
    for l in linee:
        if len(l) == 0:
            analisi_liste = False
            continue
        k,v = l.split(':')
        v = v.split(',')
        if analisi_liste:
            liste[k] = [int(x) for x in v]
        else:
            gruppi[k] = v

    print(liste)
    print(gruppi)
    #SVILUPPO PUNTO 1 A palindromo()
    output_txt = ''
    for k,v in liste.items():
        if palindromo(v):
            output_txt += f'la lista {k}, fatta da {v} è palindroma\n'
    if len(output_txt) == 0:
        output_txt = 'Non ci sono liste palindrome'
    tout.value = output_txt
    #DOPO 5 SECONDI APPARE RISULTATO DI punto5()
    app.after(5000,punto4)


app = App(width=1000,height=800)
Text(app,'INPUT')
input_base = '''
1:1,2,3,2,1
2:3,4,5
3:6,7,8

A:1,2
B:2,3
'''
tin = TextBox(app,multiline=True,width=80,height=20,text=input_base)
Text(app,'OUTPUT')
tout = TextBox(app,multiline=True,width=80,height=20)
PushButton(app,text='run',command=f1)
app.display()