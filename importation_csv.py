def importation(fichier):
    
    
    fichier = open(fichier , "r" ,encoding='utf-8' )    
    
    ligne_descripteurs = fichier.readline()    
    liste_descripteurs = ligne_descripteurs.rstrip().split(";")
        
    lignes = fichier.readlines()    
    data = []    
    for ligne in lignes :        
        lg = ligne.rstrip().split(";")
        lg[4] = int(lg[4])
        lg[5] = int(lg[5])
        lg[6] = int(lg[6])
        lg[7] = int(lg[7])
        lg[8] = int(lg[8])
       
        data.append(lg)
    
    fichier.close()
    
    
    print(liste_descripteurs)
    print(data)
    return liste_descripteurs , data
importation('population.csv')

def recherche(descripteurs, tbl) :
    numero_descripteurs = [descripteurs.index('Nom du département'), descripteurs.index('Population totale')]
    table_recherche = []
    for ligne in tbl :
        if ligne[numero_descripteurs[1]]< 300000 :
                table_recherche.append( ligne[numero_descripteurs[0]])
    return table_recherche


descripteurs , donnees = importation('population.csv')
resultat = recherche(descripteurs, donnees)
print(resultat)

from operator import itemgetter
def tri(descripteurs, tbl) :
    ind_desc = [descripteurs.index('Nom de la région'),
                descripteurs.index('Nom du département'),
                descripteurs.index('Population totale')]
    
    tri = sorted(tbl , key=itemgetter(ind_desc[0],ind_desc[2]))
    res = []
    for l in tri :
        res.append([l[ind_desc[0]], l[ind_desc[1]],l[ind_desc[2]]])
    return res

champs, donnees = importation("population.csv")
resultat = tri(champs, donnees)
print(resultat)