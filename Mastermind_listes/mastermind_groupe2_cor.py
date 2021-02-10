##################
## Mastermind ####
##################
# correction pour le groupe 2

from random import randint

#### Phase A ####
# fonction 1
def creer_liste(n,p):
    return [randint(1,p) for i in range(n)]

# fonction 2
def elements_identiques(L1,L2):
    nb = 0
    for i in range(len(L1)):
        if L1[i] == L2[i]:
            nb = nb + 1
    return nb
assert elements_identiques([2,3,5,7],[2,5,7,9]) == 1

# fonction 3
def demander_niveau():
    num = int(input("Entrer le niveau désiré (de 1 à 4) : "))
    while num not in [1,2,3,4]:
        print("Veillez à respecter la consigne.")
        num = int(input("Entrer le niveau désiré (de 1 à 4) : "))
    return num

#### Phase B ####
# fonction 1
def creer_liste_sans_doublons(n,p):
    liste=[]
    while len(liste) < n:
        num = randint(1,p)
        if num not in liste:
            liste.append(num)
    return liste

# fonction 2
def elements_communs(L1,L2):
    nb = 0
    liste_temp = L2[:]
    for element in L1:
        if element in liste_temp:
            nb = nb + min(L1.count(element),liste_temp.count(element))
            while element in liste_temp:
                liste_temp.remove(element)
    return nb
assert elements_communs([2,3,5,7,7],[2,5,7,9,2]) == 3

# fonction 3
def demander_liste(n,p):
    liste=[]
    print("Vous avez ",n," nombres à choisir")
    while len(liste) < n:
        num = int(input("Entrer un nombre compris entre 1 et "+ str(p)+" : "))
        if 1 <= num <= p:
            liste.append(num)
        else:
            print("Veillez à respecter la consigne.")
    return liste


### Phase C ###

def partie_mastermind():
    niveau = demander_niveau()
    if niveau in [1,2] :
        n = 4
        p = 6
    else:
        n = 5
        p = 8
    if niveau in [1,3]:
        liste_a_trouver = creer_liste_sans_doublons(n,p)
    else:
        liste_a_trouver = creer_liste(n,p)
    mal_place = 0
    bien_place = 0
    nb_tours = 10
    print("Vous avez 10 tours pour trouver la solution.")
    while bien_place < n and nb_tours > 0:
        print("Il vous reste ",nb_tours," essais.")
        liste_proposee = demander_liste(n,p)
        bien_place = elements_identiques(liste_a_trouver,liste_proposee)
        communs = elements_communs(liste_a_trouver,liste_proposee)
        mal_place = communs - bien_place
        print("Vous avez ",bien_place," éléments bien placés et ",mal_place," éléments mal placés.")
        nb_tours = nb_tours - 1
    if bien_place == n:
        print("Bravo ! Vous avez gagné en ",(10 - nb_tours)," essais.")
    else:
        print("Perdu ! Retentez une nouvelle partie.")
        print("La combinaison à trouver était ",liste_a_trouver)



partie_mastermind()