#Exercice 1 :

#1 test

#2 int pas sur

#3 int pas sur

#4 20

#Exercice 2 :

#1

def calcul_depart(capital_depart, n) :
    capital = capital_depart 
    for i in range(n) :
        capital = capital * 1.05
    return capital



#2

def depasse_500(calcul_depart2) :
    capital = calcul_depart2
    annee = 0
    while capital < 500 :
        capital = capital * 1.05
        annee = annee + 1
    return annee


#Exercice 3

#1

# 1 étage = 2 carte
# 2 étages = 7 cartes
# 6 étages = 57 cartes


#2 
# Le type de la valeur de retour de cette fonction est int



#4

def nombre_de_cartes(n) :
    som = 0
    for etage in range(1,n+1) :
        som = som + etage * 3 - 1
    return som

print(nombre_de_cartes(6))

#3

assert nombre_de_cartes(5) == 40
assert nombre_de_cartes(10) == 155

#5 
# Les 52 cartes pourront faire un chateau de 5 étages maximum

#6
"""
nom  : etages_max
param : n un entier positif
resultat : Nombres d'étages max avec le nombres de cartes n

"""


#8
def chateau(nombre) :
    etage = 0
    while nombre_de_cartes(etage + 1) <= nombre :
        etage = etage + 1
    return etage

#7

assert chateau(50) == 5
assert chateau(100) == 8


#Exercice 4

#Partie 1

#1 a.

# 5 * 3 = 15            
# 15 * 3 = 45           
# 45 * 3 = 135           
# Nous répétons l'opérations jusqu'au 8 Mai
#
# 5 + 15 + 45 + 135 + 405 + 1 215 + 3 645 + 10 935 = 16 400  

#b. 
# 3 + 9 + 27 + 81 + 243 + 729 + 2 187 + 6 561 = 9 840

#2 

def nombre_glacieres(nombre_amis) :
    nombre_invitations = nombre_amis
    nombre = nombre_amis
    for jour in range(7) :
        nombre_invitations = nombre_invitations * 3
        nombre = nombre + nombre_invitations
    return nombre 

#Partie 2

#1

#nombre_glacieres2(15,16) 1er mai -> 17 mai = 16 jours pour inviter des amis

#2

def nombre_glacieres2(nb_amis, nb_jours) :
    nombre_invitations = nb_amis
    nombre = nb_amis
    for jours in range(nb_jours) :
        nombre_invitations = nombre_invitations * 3
        nombre = nombre + nombre_invitations
    return nombre

#Partie 3

def nombre_jours(nombre_amis) :
    jour  = 0
    nombre_invitations = nombre_amis
    nombre = nombre_amis
    while nombre < 1000000000 :
        jour = jour + 1
        nombre_invitations = nombre_invitations * 3
        nombre = nombre + nombre_invitations
    return jour

"""⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣔⢧⣓⢖⡮⣎⢮⢣⡫⡂⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⢠⡺⣧⣳⢵⡳⡝⡎⣎⢇⢏⢎⢲⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡠⡄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⡀⡧⣫⡳⡳⡓⡝⢚⢻⢽⢺⢼⢼⢼⡁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⣀⢀⠄⠄⣠⢪⢣⠊⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⢀⢠⡪⣞⣝⣞⢮⡳⡱⢌⢂⠢⡑⡸⡸⡹⣝⡾⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⡱⡀⠈⠄⡀⡮⡪⠊⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⢠⢞⣜⢮⢮⢺⢜⢷⢽⢮⢇⢇⢕⢵⡧⣇⢇⢗⡿⡻⠄⠄⠄⠄⠄⠄⢠⠄⢄⠈⠂⠄⢀⢖⢝⠜⠄⠄⡀⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⡠⢯⢯⡺⡧⣳⡱⢍⠇⡏⢎⠫⡢⢊⠜⢜⢕⠝⠁⠄⠄⠄⠄⠄⠄⣀⢄⠈⠢⠜⠄⢀⢔⢇⡯⣢⢆⡶⡤⣄⡀⡐⠄⠁⠄⠐⠄⠄
⠄⢠⣝⢵⡫⡿⣝⢮⡪⡣⡓⠜⢔⢑⠌⢔⠨⢂⠢⠡⠄⠄⠄⠄⠄⠄⠄⠙⢆⠅⠄⠄⡆⡧⣫⡺⡼⡪⢷⢽⢯⣗⢯⡆⡄⠄⠄⠄⠄⠄
⠄⣞⢾⢵⡫⡯⣗⣝⢮⢢⠪⡘⡐⢅⢊⠔⡨⠢⡑⡅⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⢮⣺⢽⢳⡹⡰⡨⠪⡽⣕⢯⡳⣝⡦⡀⠄⠄⡀⠄
⠄⣞⢽⣝⢮⢯⣺⢮⣳⡳⡵⡸⡨⡢⣑⢑⢌⢎⠪⡢⠄⠄⠄⠄⠄⠄⠄⠄⢠⠪⣳⣟⢮⢳⢕⣽⢪⢘⢜⢜⢮⡳⡽⣕⡯⣖⠄⠄⠄⠄
⠄⠘⣝⢮⢯⣳⣳⣻⣺⡪⣳⢱⢱⢸⢰⢵⡕⡔⡑⡌⡀⠄⠄⠄⠄⠄⢀⠦⠃⠁⢻⣽⢕⣗⡽⡳⡱⡐⢕⢕⡳⡽⣝⡮⣯⡺⣕⡀⠄⠄
⠄⠄⠈⠹⢳⣳⣻⣞⡧⣏⢮⢪⠪⡪⡪⡳⡽⣰⢨⢊⠪⠪⠢⡢⢄⢔⠍⠄⠄⠄⠈⠈⢑⢗⠝⢜⠰⡘⣜⢼⣝⣞⣗⢯⡳⣝⢮⢆⠄⠄
⠄⠄⠄⠄⠄⠈⠘⠷⢟⢮⡳⡱⣑⢌⠪⠨⠪⠺⠸⡨⡢⢄⣀⢰⠍⠄⠄⠄⠄⠄⠄⡀⢘⢌⢎⠪⡪⡪⡮⣗⢗⣗⢽⢕⢯⢮⡳⣯⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⡮⡣⡁⠄⠄⠄⠄⠄⠄⠈⠨⡢⡪⠢⠋⠄⠄⠄⠄⠄⠁⠄⠨⡢⡑⡅⢕⠕⣕⢳⢹⢸⢪⢳⡹⡮⡯⡷⡅⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢯⢎⢆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠁⠄⠄⠄⠄⠈⠄⠄⠄⠈⠂⠑⠘⠐⠑⠘⠘⠘⠘⠘⠊⠙⠙⠙⠋⠃⠄
               _,........__
            ,-'            "`-.
          ,'                   `-.
        ,'                        \
      ,'                           .
      .'\               ,"".       `
     ._.'|             / |  `       \
     |   |            `-.'  ||       `.
     |   |            '-._,'||       | \
     .`.,'             `..,'.'       , |`-.
     l                       .'`.  _/  |   `.
     `-.._'-   ,          _ _'   -" \  .     `
`."""""'-.`-...,---------','         `. `....__.
.'        `"-..___      __,'\          \  \     \
\_ .          |   `""""'    `.           . \     \
  `.          |              `.          |  .     L
    `.        |`--...________.'.        j   |     |
      `._    .'      |          `.     .|   ,     |
         `--,\       .            `7""' |  ,      |
            ` `      `            /     |  |      |    _,-'"""`-.
             \ `.     .          /      |  '      |  ,'          `.
              \  v.__  .        '       .   \    /| /              \
               \/    `""\"""""""`.       \   \  /.''                |
                `        .        `._ ___,j.  `/ .-       ,---.     |
                ,`-.      \         ."     `.  |/        j     `    |
               /    `.     \       /         \ /         |     /    j
              |       `-.   7-.._ .          |"          '         /
              |          `./_    `|          |            .     _,'
              `.           / `----|          |-............`---'
                \          \      |          |
               ,'           )     `.         |
                7____,,..--'      /          |
                                  `---.__,--.'mh
"""
