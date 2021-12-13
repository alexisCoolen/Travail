#Exercice 1

import turtle
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

#Exercice 2

import turtle
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
    
#Exercice 3
    
import turtle
def carre(pas):
    """
    Description de la fonction : Déplace la tortue de sorte qu'elle dessine un carré
                                 et revienne au point de départ (même position et orientation)
    pas(int) : côté du carré
    return : None
    """
    
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
    
#Exercice 4
def carreEmboite(pas,nb):
    """
    Description de la fonction : Déplace la tortue de sorte qu'elle dessine une succession
                                de carrés emboîtés régulièrement espacés
    pas(int) : côté du plus petit carré
    nb(int): nombre total de carrés
    return : None
    """
import turtle
range(nb)
for i in range(4):
        turtle.forward(100)
        turtle.left(90)

#Exercice 5

def carreTournant(cote,nb):
    """
    Description de la fonction : Déplace la tortue de sorte qu'elle dessine une succession
                                de carrés tournants régulièrement espacés
    pas(int) : côté du plus petit carré
    nb(int): nombre total de carrés
    return : None
    """
    
import turtle
for i in range(10):
    for j in range(10):
        turtle.forward(100+cote)
        turtle.left(90+cote)
        
#Exercice 6
def ligne2carre(nb,cote,espacement):
    """
    Description de la fonction : Déplace la tortue de sorte qu'elle dessine une ligne de carré
    nb(int) : nombre de carrés dessinés
    cote(int): côté du carré
    espacement(int) : espacement entre 2 carrés successifs
    return : None
    """

for i in range(nb):
        carre(cote)
        turtle.up()
        turtle.forward(espacement+cote)
        turtle.down()
        
#Exercice 7

def damier(longueur,hauteur,cote,espacement):
    """
    Description de la fonction : Déplace la tortue de sorte qu'elle dessine un damier
    longueur(int) : nombre de carrés par ligne
    hauteur(int) : nombre de carrés par colonne
    cote(int): côté du carré
    espacement(int) : espacement entre 2 carrés successifs
    return : None
    """
    turtle.up()
    turtle.goto(-espacement,-espacement)
    turtle.down()
    turtle.forward(longueur*(cote+espacement)+espacement)
    turtle.left(90)
    turtle.forward(hauteur*(cote+espacement)+espacement)
    turtle.left(90)
    turtle.forward(longueur*(cote+espacement)+espacement)
    turtle.left(90)
    turtle.forward(hauteur*(cote+espacement)+espacement)
    turtle.left(90)
    turtle.up()
    turtle.goto(0,0)
    turtle.down()
    y = 0
    for i in range(hauteur):
        ligne2carre(longueur, cote, espacement)
        y=y+cote+espacement
        turtle.up()
        turtle.goto(0,y)
        turtle.down()
