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
    if moyenne =< 10:
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

#Exercice 3
def maximum ():
    '''
    Description : Démontre que a > b
    paramètre : a (float) nombre n inconnu
    paramètre : b (float) autre nombre n inconnu
    paramètre : > (float) définit quel nombre n est supérieur
    '''
    A = '5'
    B = '2'
    maximum = 'A >= B'
    if maximum (A >= B):
        print('A est supérieur a B')
        else:
            print('B est supérieur a A')


#Exercice 4
def inférieur ():
    '''
    Description : Démontre que a < b
    paramètre : a (float) nombre n inconnu
    paramètre : b (float) autre nombre n inconnu
    paramètre : < (float) définit quel nombre n est inférieur
    '''
    A = '2'
    B = '5'
    maximum = 'A =< B'
    if maximum (A =< B):
        print('A est inférieur a B')
        else:
            print('B est inférieur a A')
