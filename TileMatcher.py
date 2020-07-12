import random
import time
import winsound
from tkinter import *
from tkinter import Tk,Button,DISABLED
from tkinter import font as tkFont

def show_symbol(x,y):
        global first
        global previousx,previousy
      
        buttons[x,y]['text']=button_symbols[x,y]
        buttons[x,y].update_idletasks()
        

        if first:
            previousx=x
            previousy=y
            first=False
        elif previousx != x or previousy != y:
            if buttons[previousx,previousy]['text'] != buttons[x,y]['text']:
                time.sleep(0.5)
                buttons[previousx,previousy]['text']= ' '
                buttons[x,y]['text']= ' '

            else:
                buttons[previousx,previousy]['command']=DISABLED
                buttons[x,y]['command']=DISABLED
              
            first=True
win=Tk()
winsound.PlaySound('Little_Jam.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
win.title("TileMatcher")
win.resizable(width=False,height=True)
first=True
previousx=0
previousy=0
buttons={}
button_symbols={}
symbol=[u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270B',u'\u270A',u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728', u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270B',u'\u270A',u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']

random.shuffle(symbol)
hel = tkFont.Font(size=22, weight='bold')
for x in range(6):
    for y in range(4):
        button=Button(command= lambda x=x,y=y: show_symbol(x,y),width=8,height=4,bg='#000',fg='#fff',borderwidth="2px")
        button['font'] = hel
        button.config(relief=GROOVE)
        button.grid(column=x,row=y)
        buttons[x,y]=button
        button_symbols[x,y]=symbol.pop()
win.mainloop()
