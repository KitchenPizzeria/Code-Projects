from tkinter import *
import random

def ReadCSV():
    File = open("DEFINITIONS.csv","r")
    Words = []
    Meanings = []
    for x in File:
        eachLine = x.strip()
        listLine  = eachLine.split(',')
        Words.append(listLine[2])
        Meanings.append(listLine[3])
    return Words, Meanings

Words,Meanings = ReadCSV()

MeaningsGlossary = {} 
for x in range(len(Words)): 
    MeaningsGlossary[Words[x]] = Meanings[x]
        
WordsGlossary = {} 
for x in range(len(Words)):
    WordsGlossary[Words[x]] = Words[x]


def FindRandomWord():   
    if not len(MeaningsGlossary) == 0 :
        SubmitButton.config(state = ACTIVE)
        DisplayResult.set("")
        InputText.set("")
        NextButton.config(text = "Next")
        GlossaryWord = random.choice(list(MeaningsGlossary.keys()))
        GlossaryDef = MeaningsGlossary[GlossaryWord]
        del MeaningsGlossary[GlossaryWord]
        DisplayWord.set(GlossaryWord)
        DisplayDef.set(GlossaryDef)
        NextButton.config(state = DISABLED)
        

def CheckText():
    if TextBox.get() == DisplayWord.get():
        NextButton.config(state = ACTIVE)
        SubmitButton.config(state = DISABLED)
        DisplayResult.set("CORRECT !!")
        DisplayScoreResult.set(int(DisplayScoreResult.get())+1)
    else:
        DisplayResult.set("TRY AGAIN !!")
        InputText.set("")
        
        
        
       
myGui = Tk()
myGui.geometry("500x150")

DisplayWord = StringVar()
DisplayDef = StringVar()
DisplayScoreWord = StringVar()
DisplayScoreResult = StringVar()
DisplayResult = StringVar()
InputText = StringVar()

WordLabel = Label(myGui, textvariable=DisplayWord)
WordLabel.place(x=10,y=10)

DefLabel = Label(myGui, textvariable=DisplayDef)
DefLabel.place(x=10,y=50)

ScoreLabelWord = Label(myGui, textvariable = DisplayScoreWord)
DisplayScoreWord.set("Score:")
ScoreLabelWord.place(x=400,y=10)

Score = Label(myGui, textvariable = DisplayScoreResult)
x = 0
DisplayScoreResult.set(x)
Score.place(x=439,y=10)

ResultLabel = Label(myGui,textvariable = DisplayResult)
DisplayResult.set("")
ResultLabel.place(x=370,y=85)

TextBox = Entry(myGui,textvariable=InputText)
TextBox.place(x=183,y=90)

    
NextButton = Button(myGui, text="Begin !",width=8,command=FindRandomWord)
NextButton.place(x=170,y=120)

SubmitButton = Button(myGui, text="Submit",width=8,command=CheckText,state = DISABLED)
SubmitButton.place(x=250,y=120)

myGui.mainloop()

