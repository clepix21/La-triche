def importation(fichier):
    
    
    fichier = open(fichier , "r" ,encoding='utf-8' )    
    
    ligne_descripteurs = fichier.readline()    
    liste_descripteurs = ligne_descripteurs.rstrip().split(";")
        
    lignes = fichier.readlines()    
    data = []    
    for ligne in lignes :        
        lg = ligne.rstrip().split(";")
        lg[0] = int(lg[0])
        lg[6] = int(lg[6])
        lg[8] = int(lg[8])
       
        data.append(lg)
    
    fichier.close()

    
    
    print(liste_descripteurs)
    print(data)
    return liste_descripteurs , data





importation("velo.csv")
def recherche(descripteurs, tbl) :
    numero_descripteurs = [descripteurs.index('Tempsenseconde'), descripteurs.index('Nom')]
    table_recherche = []
    for ligne in tbl :
        if ligne[numero_descripteurs[1]]< 3800 :
            table_recherche.append( ligne[numero_descripteurs[0]])
    return table_recherche




