#!/user/bin/python 
# coding: utf-8

#Créer environnement virtuel et ajouter modules manquants
import csv
import requests
from bs4 import BeautifulSoup


# Ce script de moissonnage servira à recueillir les données concernant 
# les subventions accordées par le ministère des Ressources naturelles du Canada 
# pour le 1er trimestre de l'année 2016-2017

# Les informations que l'on cherche s'étendent en fait sur trois apges web différentes
# Donc 3 URL qui auront chacun leur propre variable

url1 = "http://www2.nrcan-rncan.gc.ca/dgc-dposc/index.cfm?fuseaction=r.g&lang=fra&fisc=2016-2017&qrt=01"
url2 = "http://www2.nrcan-rncan.gc.ca/dgc-dposc/index.cfm?fuseaction=r.g&lang=fra&fisc=2016-2017&qrt=01&strt=11"
url3 = "http://www2.nrcan-rncan.gc.ca/dgc-dposc/index.cfm?fuseaction=r.g&lang=fra&fisc=2016-2017&qrt=01&strt=21"

# Il faut ensuite créer un fichier csv dans lequel on compilera toutes les données
fichier = "subventions-RNCan.csv"

# ON crée ensuite une entête avant de se connecter au site afin de s'identifier
entetes = {
	"User-Agent":"Dominique Degré - Requête envoyée dans le cadre d'un cours de journalisme informatique à l'UQAM (EDM5240)",
	"From":"d.degre95@gmail.com"
}

# On établit ensuite la connection avec les différents URL, touut en créant 
# diverses variables où iront les données récoltées
subventions1 = requests.get(url1, headers = entetes)
subventions2 = requests.get(url2, headers = entetes)
subventions3 = requests.get(url3, headers = entetes)

# Vient maintenant le temps d'analyser l'info et de mettre les résultats dans de nouvelles variables.
page1 = BeautifulSoup(subventions1.text,"html.parser")
page2 = BeautifulSoup(subventions2.text,"html.parser")
page3 = BeautifulSoup(subventions3.text,"html.parser")

#print(page1)
#print(page2)
#print(page3)

i=0

# La prochaine étape consiste à créer des variables qui regroupent les URL complets de chacune
# des pages des subventions détaillées.

# Il faut d'abord aller chercher le contenu de chacune des lignes
# Ensuite, il faut isoler le lien de chacune des lignes qui mène à la page avec tous les détails d'une subvention donnée
# Finalement, on ajoute l'adresse de la page mère de Ressources naturelles Canada devant chacun
# des liens obtenus à l'étape précédente pour avoir des URL complets.

# Pour le premier URL 
for ligne1 in page1.find_all("tr"):
    #print(ligne1)
    if i!= 0:
        lien1 = ligne1.a.get("href")
        #print(lien1)
        hyperlien1 = "http://www2.nrcan-rncan.gc.ca/dgc-dposc/" + lien1
        #print(hyperlien1)
        
        # On va maintenant "parser" à nouveau les données de chacun de nos nouveaux hyperliens précis
        # en créant de nouvelles variables
        contenu1 = requests.get(hyperlien1, headers=entetes)
        pageA = BeautifulSoup(contenu1.text,"html.parser")
        
        # Par la suite, on crée une liste où iront nos informations relatives
        # à chacune de nos subventions précises
        subventionsI = []
        #Dans cette liste, on met l'hyperlien en premier
        subventionsI.append(hyperlien1)
        
        # On fait une boucle pour aller chercher tous les éléments du tableau de notre premier hyperlien
        for item in pageA.find_all("tr"):  
            print(item)
            # On met cette condition pour enlever les cases qui seraient vides
            if item.td is not None:
                subventionsI.append(item.td.text)
            else:
                subventionsI.append(None)
        #print(subventionsI)      
    
    #On ajoute finalement le tout à notre fichier CSV
        poutine = open(fichier,"a")    
        sauce = csv.writer(poutine)
        sauce.writerow(subventionsI)
    
    # Pour ce qui est des autres URL, il faut réécricre les scripts  comme à partir de la ligne 56 
    #dans un nouveau fichier sur Cloud9,
    # sinon, on obtient un message d'erreur: AttributeError: 'NoneType' object has no attribute 'get'
    # Les données des deux autres URL seront néanmoins dans le même CSV
    i = i+1
#########################################
# Voici les 2 autres scripts pour les deux autres URL (à ouvrir dans un autre fichier sur Cloud9)
#!/user/bin/python 
# coding: utf-8

# J'ai réimporté tous les modules pour commenrcer
import csv
import requests
from bs4 import BeautifulSoup

entetes = {
	"User-Agent":"Dominique Degré - Requête envoyée dans le cadre d'un cours de journalisme informatique à l'UQAM (EDM5240)",
	"From":"d.degre95@gmail.com"
}

url2 = "http://www2.nrcan-rncan.gc.ca/dgc-dposc/index.cfm?fuseaction=r.g&lang=fra&fisc=2016-2017&qrt=01&strt=11"
subventions2 = requests.get(url2, headers = entetes)
page2 = BeautifulSoup(subventions2.text,"html.parser")

fichier = "subventions-RNCan.csv"

i = 0

# Le second
for ligne2 in page2.find_all("tr"):
    #print(ligne2)
    if i!= 0:
        lien2 = ligne2.a.get("href")
        #print(lien2)
        hyperlien2 = "http://www2.nrcan-rncan.gc.ca/dgc-dposc/" + lien2
        print(hyperlien2)
        
        contenu2 = requests.get(hyperlien2, headers=entetes)
        pageB = BeautifulSoup(contenu2.text,"html.parser")
        
        subventionsII = []
        #Dans cette liste, on met l'hyperlien en premier
        subventionsII.append(hyperlien2)
        
        # On fait une boucle pour aller chercher tous les éléments du tableau de notre premier hyperlien
        for item in pageB.find_all("tr"):  
            #print(item)
            # On met cette condition pour enlever les cases qui seraient vides
            if item.td is not None:
                subventionsII.append(item.td.text)
            else:
                subventionsII.append(None)
        #print(subventionsII)      
    
    #On encore ajoute au fichier CSV
        viking = open(fichier,"a")    
        drakkar = csv.writer(viking)
        drakkar.writerow(subventionsII)
        
    i = i+1
#####################################################
#!/user/bin/python 
# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

entetes = {
	"User-Agent":"Dominique Degré - Requête envoyée dans le cadre d'un cours de journalisme informatique à l'UQAM (EDM5240)",
	"From":"d.degre95@gmail.com"
}

url3 = "http://www2.nrcan-rncan.gc.ca/dgc-dposc/index.cfm?fuseaction=r.g&lang=fra&fisc=2016-2017&qrt=01&strt=21"
subventions3 = requests.get(url3, headers = entetes)
page3 = BeautifulSoup(subventions3.text,"html.parser")

fichier = "subventions-RNCan.csv"

i = 0

# Le troisième:
for ligne3 in page3.find_all("tr"):
    #print(ligne3)
    if i!= 0:
        lien3 = ligne3.a.get("href")
        #print(lien3)
        hyperlien3 = "http://www2.nrcan-rncan.gc.ca/dgc-dposc/" + lien3
        print(hyperlien3)
        
        contenu3 = requests.get(hyperlien3, headers=entetes)
        pageC = BeautifulSoup(contenu3.text,"html.parser")
        
        subventionsIII = []
        #Dans cette liste, on met l'hyperlien en premier
        subventionsIII.append(hyperlien3)
        
        # On fait une boucle pour aller chercher tous les éléments du tableau de notre premier hyperlien
        for item in pageC.find_all("tr"):  
            #print(item)
            # On met cette condition pour enlever les cases qui seraient vides
            if item.td is not None:
                subventionsIII.append(item.td.text)
            else:
                subventionsIII.append(None)
        #print(subventionsII)      
    
    #On ajoute une dernière fois au fichier CSV
        brownie = open(fichier,"a")    
        choco = csv.writer(brownie)
        choco.writerow(subventionsIII)
        
    i = i+1
