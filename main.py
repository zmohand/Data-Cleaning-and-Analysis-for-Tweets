#imports
import json
import stack
import pandas as pd
import affichage


#zone d'atterissage est un objet de la class Stack qui contient (principalement) une liste de tweets, qui sont des objets de type Tweet
zone_atterissage = stack.Stack("stack")

#On parcourt le fichier ligne par ligne pour pouvoir faire un json.load (on considere donc que chaque ligne du fichier est un fichier json sous forme de dictionnaire)
with open("aitweets.json", "r", encoding="utf-8") as file:
    for line in file:
        data = json.loads(line)
        
        #On charge la data dans la zone d'atterissage 
        zone_atterissage.charger_liste_stack(data)

#Création du nouveau fichier json avec les nouvelles données ordonnées et nettoyées
zone_atterissage.charger_clean_stack()

#création de la DataFrame à partir du fichier json qu'on a créé plus tôt avec les données nettoyées. 

#dtype pour éviter la conversion de l'id en int64 ce qui pourrait le modifier
df = pd.read_json(zone_atterissage.fichier_json, lines = True, dtype={"tweet_id": str})


#création de la fenêtre d'affichage et lancement

aff = affichage.Gui(df)
aff.lancement()