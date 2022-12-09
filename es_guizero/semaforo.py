from guizero import *
app = App(title='traffic HAT controller', layout='grid')

#funzione accendi colori
def f1(but):
    if but == 'off':
        slider_red.value = 100
        slider_amber.value = 0 
        slider_green.value = 0
    elif but == 'beep':
        slider_red.value = 0
        slider_amber.value = 100
        slider_green.value = 0
    elif but == 'on':
        slider_red.value = 0
        slider_amber.value = 0
        slider_green.value = 100
#------------------------Scritte Colori------------------------------------------------------------------
lights=Text(app, text='Lights', grid =[0,0])
lights.size= 12
lights.text_color = 'white'

red = Text(app, text='Red', grid =[1,0])
red.size= 12
red.text_color = 'red'

amber = Text(app, text='Amber', grid=[2,0])
amber.size= 12
amber.text_color = 'yellow'

green = Text(app, text='Green', grid =[3,0])
green.size= 12
green.text_color = 'green'
#-----------------------------slider associato al colore-----------------------------------------------------------------------------
slider_red= Slider(app, horizontal=False, grid=[1,1], height=150,start=100, end=0)
slider_amber= Slider(app, horizontal=False, grid=[2,1], height=150, start=100, end=0)
slider_green= Slider(app, horizontal=False, grid=[3,1], height=150, start=100,end=0)
#-----------------------------------------------------------buzzer--------------------------------------------------------------------------------------------------
buzzer=Text(app, text='Buzzer', grid =[0,2])
buzzer.size= 12
buzzer.text_color = 'white'
#------------------------------------buttons buzzer-----------------------------------------------------------------------------------------------
button_red=PushButton(app, text='off', grid=[1,2], command=f1, args=['off'])
button_amber=PushButton(app, text='beep', grid=[2,2], command=f1, args=['beep'])
button_green=PushButton(app, text='on', grid=[3,2], command=f1, args=['on'])
#--------------------------------------------------------scritta button--------------------------------------------------------------------------------------------
button=Text(app, text='Button', grid =[0,3])
button.size= 12
button.text_color = 'white'
#---------------------------checkboxs pushed and held----------------------------------------------------------------------------------------
checkbox_pushed=CheckBox(app, text='Pushed', grid=[1,3])
checkbox_help=CheckBox(app, text='Held', grid=[2,3])
app.display()

