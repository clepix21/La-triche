
"""
#Utilisation de la fonction Reader.
import csv # le module pour les fichiers csv

file = open("test.csv" , "r") # ouvrir le fichier

csv_en_liste = csv.reader(file , delimiter = ",") # initialisation d’un lecteur de fichier delimiter est facultatif

for ligne in csv_en_liste : # parcours du lecteur avec une boucle
    print(ligne) # affichage ligne à ligne

file.close () # fermeture du fichier


#Utilisation de la fonction DictReader
import csv # le module pour les fichiers csv

file = open("test.csv" , "r") # ouvrir le fichier
csv_en_dico = csv.DictReader(file , delimiter = ",") # initialisation d’un lecteur de fichier avec création automatique de dictionnaire

for ligne in csv_en_dico : # parcours du lecteur avec une boucle
	print(dict(ligne)) # affichage ligne à ligne

file.close () # fermeture du fichier
"""

import pandas

pays = pandas.read_csv("countries.csv", delimiter = ";", keep_default_na=False)

villes = pandas.read_csv("cities.csv", delimiter=";")

#print(villes.head())
#print(villes.sample(7))
#print(villes.columns)
#print(villes.dtypes)
print(villes.loc[10])