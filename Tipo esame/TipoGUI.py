from guizero import *

app = App(title='Esame')


def parseInput(t):
    pass


def punto1():
    s = ''
    t = parseInput(inp.value)

    out.value = s


def punto2():
    s = ''
    t = parseInput(inp.value)

    out.value = s


def punto3():
    s = ''
    t = parseInput(inp.value)

    out.value = s


def punto4():
    s = ''
    t = parseInput(inp.value)

    out.value = s


testo = '''put your input here'''

inp = TextBox(app, text=testo, multiline=True, width='fill', height=10)
out = TextBox(app, text='output', multiline=True, width='fill', height=10, enabled=False)

box = Box(app, layout='grid')

PushButton(box, grid=[0,0], text='Punto1', command=punto1)
PushButton(box, grid=[1,0], text='Punto2', command=punto2)
PushButton(box, grid=[2,0], text='Punto3', command=punto3)
PushButton(box, grid=[3,0], text='Punto4', command=punto4)


app.display()
