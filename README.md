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

def triangle(c1,c2,c3):
    """
    description de la fonction : affiche une des caractéristiques du triangle suivante : équilatéral, isocèle ou scalène
    c1, c2, c3 (int ou float) : trois côtés du triangle
    précondition sur les entrées : on considère que les valeurs de c1, c2 et c3 doivent permettre de construire un triangle
    return (None)
    """#Exercice 1

liste_alexis = [4,7,3,4,6,9,13,2]

#Exercice 2
liste_de_prenom = ['Alice', 'Bob', 'Tom']
liste_de_prenom.insert(2, 'Marc')

#Exercice 3
t = [0,4,16,36,64]
for i in range(0):
    t.append(i**2)

#Exercice 4
t = [0]*10

for i in range(len(t)):
    t[i] = 10 - i

#Exercice 5
    
def longueurNomV1(liste_nom):
    liste_longueur=[]
    for nom in liste_nom:
        long=len(nom)
        liste_longueur.append(long)
        
    print(liste_longueur)
    
if triangle == c1:
    print(équilatéral)
elif triangle == c2:
    print(isocèle)
else:
    print(scalène)

for i in range (2,9):
    print (i)

for j in range (0,25,4):
    print (j)
    
for maChaine in "informatique":
    print ("On affiche la lettre", maChaine)

for i in range (10):
    print("Pour progresser en programmation, la pratique est le plus important")

for i in range (1,11):
    k=7*i
    print(k)
    
for i in range (1,11):
    k=7*i
    print(7,i,"=",k)
    
for tableMultiplication in range (1,11):
    k=9*tableMultiplication
    print(9,"*",tableMultiplication,"=",k)
    
for plusieursTablesMultiplication in range (1,11):
    k=3*plusieursTablesMultiplication
    print(3,"*",plusieursTablesMultiplication,"=",k)

#Exercice 4
def nombreCaracteres(chaine):
    compteur = 0
    for lettre in chaine:
            compteur = compteur+1
    return compteur

#Exercice 5
def compterOccurence(chaine,c):
    compteur = 0
    for caractere in chaine:
        if caractere == c:
            compteur +=1
    return compteur
   
#Exercice 6
On passe dans la boucle for 2 fois, et 0 fois dans la seconde fonction
Nous n'avons pas le meme résultat car dans Stallmann, nous avons deux a existant, et dans Richard, aucun B est présent (a cause du if du code si c'est une lettre "c" dans la fonction est présente)

def rechercheIndice(chaine, c):
    """
    Description de la fonction : renvoie l'indice de la première occurence du caractère c dans chaine
    chaine (str) : chaine de caractère dans laquelle la recherche s'effectue
    c (str) : caractère recherché
    return (int ou None) : indice du caractère c danc chaine (None si le caractère c n'apparaît pas dans chaine)
    """
    compteur = 0
    for lettre in chaine:
        if lettre == c:
            compteur +=1
    return compteur
