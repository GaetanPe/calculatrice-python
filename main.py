from tkinter import *
import math
from tkinter.font import Font as f

def calcule(event):

    chaine.configure(text = "Resultat :" + str(eval(entree.get() )))

fenetre = Tk()
fenetre.title("Calculatrice")
entree = Entry(fenetre,width = 20)
entree.bind("<Return>", calcule)
entree.config(font= f (size=30))
chaine = Label(fenetre, fg= 'green')
chaine.config(font = f(size= 30))
entree.pack()
chaine.pack