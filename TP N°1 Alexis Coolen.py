# Bowling

def bowling(boule1, boule2):
    """
    Description de la fonction : Affiche a l'écran les performances d'un joueur de bowling
    boule1 (int) : nombre de quilles renversées avec la première boule
    boule2 (int) : nombre de quilles renversées avec la deuxième boule
    préconditions sur les entrées : boule1 + boule2 <= 10
    """
    if boule1 == 10:
        print('X')
    elif boule1 + boule2 == 10:
        print('/')
    else:
        print(boule1 + boule2)

# Jeu du Mölkky

def molkky (score, gain):
    """
    Description de la fonction : Affiche le score et le gain des joueurs
    score (str) : score du joueur avant son lancer (score = score + gain)
    gain (str) : nombre de points que le joueur obtient avec son lancer
    préconditions sur les entrées : score <= 50
    """
    if score + gain == 50:
        print("Victoire !!")
    elif score + gain >= 50:
        print("25")
    else:
        print(score + gain)
    
def molkky_v2 (score, gain, nb_zeros):
    """
    Description de la fonction : Affiche le score et le gain des joueurs
    score (str) : score du joueur avant son lancer (score = score + gain)
    gain (str) : nombre de points que le joueur obtient avec son lancer
    préconditions sur les entrées : score <= 50
    """
    if score + gain == 50:
        print("Victoire !!")
    elif score + gain >= 50:
        print("25")
    elif nb_zeros >= 2:
        print ("Perdu !")
    else:
        print(score + gain)