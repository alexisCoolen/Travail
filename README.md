# NSI
# Exercice 1
def surface_disque(rayon):
    '''
    Description : Calcul du volume d'un disque
    parametre : rayon (float) du disque
    '''
    from math import pi
    volume = pi*r**2
# EXercice 2
def accueil2020(prénom,nom,annee_de_naissance):
    print ('Bonjour',prénom,nom,'vous''avez',annee_de_naissance,'ans')
    '''
    Description : Accueillir les utilisateurs
    parametre : nom (float) "MARTIN"
    parametre : prénom (float) "Alice"
    parametre  : annee_de_naissance (float) "2004"
    '''
    nom : 'MARTIN'
    prénom : 'Alice'
    annee_de_naissance : 2004
    age : 2020 - annee_de_naissance
#EXercice 3
def tailleFichier(kOctets):
    taille_octets = 1024 * kOctets
    taille_bits = 8 * taille_octets
    print ('Un fichier de taille' ,kOctets, 'kOctets est de' ,octets, 'octets et de',bits, 'bits')

    '''
    Description : Donner la taille de notre fichier
    parametre : koctets (int) la taille en koctets
    parametre : taille_octets (int) taille fichier en kO
    parametre : taille_bits (int) taille fichiers en bits
    '''
    octets : 1024 * 3
    bits : 8192 * 3
#EXercice 12
num_secu_sans_cle = 2690549588157
cle = num_secu_sans_cle % 97
cle = 97 - cle
#Exercice 5
def farenheitToCelsius(tF):
    '''
    Description : Convertit °F en °C
    '''
    tC = (tF - 32)*5/9
    return tC

def calcul_cle(num_secu_sans_cle):
    '''
    Description : calcul la clé d'un numéro de sécurité sociale
    paramètre : num_secu_sans_cle (o,t) le num de sécu sans clé
    '''
    cle = num_secu_sans_cle % 97
    cle = 97 - cle
    return cle

num_secu_sans_cle = 2690549588157
la_cle = calcul_cle(num_secu_sans_cle)
print('')
print('Exercice 6')
print('La clé du numéro de sécu', num_secu_sans_cle, 'a pour clé', cle')
    
def la_moyenne():
    la_note = 14
    if la_note > 10:
        print("IL a eu la moyenne au dernier devoir")
    else:
        print("IL a pas eu la moyenne au dernier devoir")

prenom_fille = 'Lola'
prenom_fille == 'Alice'

age_individu = 12
age_individu > 18

moyenne_bac = 16
moyenne_bac >= 12
def bac():
    '''
    Description : Donnes les résultats et si oui ou non, la personne en question est accepté
    parametre : prenom (float) prenom de la personne
    parametre : nom (float) nom de la personne
    parametre : moyenne (float) la moyenne de la personne
    parametre : resultat (float) phrase pour dire si oui ou non, la personne a son bac
    '''
    prenom = 'Alice'
    nom = 'Dupont'
    moyenne = '12'
    if moyenne < 10:
       "Vous n'avez pas obtenu votre baccaulaur39at"
       else:
           "Vous avez obtenu votre baccaulaur39at, F39licitations!"
bac('Alice','Dupont',12)

def bac2():
    '''
    Description : Donnes les résultats et si oui ou non, la personne en question est accepté
    parametre : prenom (float) prenom de la personne
    parametre : nom (float) nom de la personne
    parametre : moyenne (float) la moyenne de la personne
    parametre : resultat (float) phrase pour dire si oui ou non, la personne a son bac
    '''
    prenom = 'Bob'
    nom = 'Martin'
    moyenne = '9'
    if moyenne < 10:
       print("Vous n'avez pas obtenu votre baccaulaur39at")
       else:
           print("Vous avez obtenu votre baccaulaur39at")
bac2('Bob','Martin',9)           

CORRECTION :
def bac(prenom, nom, moyenne_bac)
if moyenne_bac >= 10 :
   print(prénom, nom, "a obtenu son bac, félicitations!")

def maximum (a,b):
if a >= b:
   return a
   else:
   return b

def minimum (a,b):
if a <= b 
   return a
   else:
   return b

def valeur_absolue(x):
if x >= 0:
   return x
   else:  
   return -1*x

def bowling(boule1, boule2):
    """
    Description de la fonction : Affiche a l'écran les performances d'un joueur de bowling
    boule1 (int) : nombre de quilles renversées avec la première boule
    boule2 (int) : nombre de quilles renversées ave la deuxième boule
    préconditions sur les entrées : boule1 + boule2 <= 10
    """
if boule1 == 10:
    print ("X")
elif boule1 + boule2 == 10:
    print ("/")
    else:
       print(boule1 + boule2)

def fonction1 (a,b,c):
    """
    Description : Nous prove que a est inférieur ou égal a b qui est inférieur ou égal a c
    Vrai / True (float) : Affirme la fonction
    Faux / False (float) : N'affirme pas la fonction
    """
    a = '2'
    b = '69'
    c = '420'
    if a <= b <= c:
        return ("True")
    else:
        return ("False")
def croissant(a,b,c):
    if a <= b :
        if b <= c :
            print ("True")
        else :
            print ("False")

def est bissextile(année):
    if année != (=0):
    return FAlse
    
    else:
        if annee % 100 == 0:
          if annee % 400 == 0:
            return True
        else:
            return False
