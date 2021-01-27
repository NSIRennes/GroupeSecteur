def bissextile(a):
    """ Prend en paramètre un entier (une année)
        et renvoie un booléen (True si l'année est bissextile)"""
    return a%4 == 0 and not a%100 == 0 or a%400 == 0

def nbjoursannee(a):
    """ A compléter"""
    if bissextile(a):
        return 366
    else:
        return 365
    
def nbjoursmois(a,m):
    """ Prend en paramètres l'année a, le mois m
        et renvoie le nombre de jours dans le mois """
    A compléter

def nbjours(jn, mn, an, j, m, a):
    """ Prend en paramètres  le jour jn, le mois mn ,l'année an de naissance
        le jour j, le mois m ,l'année a de la date actuelle
        et renvoie le nombre de jours  """
    r = 0       # résultat
    #On commence par ajouter le nombre de jours
    # pour les années entières
    A compléter
    # On ajoute le nombre de jours pour les mois complets
    # de l'année de naissance
    A compléter
    # On ajoute le nombre de jours pour les mois complets
    # de l'année actuelle
    A compléter
    # On ajoute les jours du mois de naissance
    A compléter
    # on ajoute les jours du mois actuel
    A compléter
    return r

#print(nbjoursmois(2020, 1))
#print(nbjoursmois(2020, 2))
#print(nbjoursmois(2020, 6))
print(nbjours(10 , 10 , 2005, 13, 10, 2020))