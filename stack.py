import tweet
import json
import nltk
import re
from textblob import TextBlob
#la classe stack hérite des attributs de la class tweet (non utilisé pour le moment)
class Stack(tweet.Tweet):

    def __init__(self, file_name):
        #On crée une liste de tweets, on pourrait mettre dans le constructeur une autre liste de tweet si l'on veut
        #Créer un stack avec déjà un autre stack ayant des tweets à l'interieur
        self.fichier_json = f"{file_name}.json"
        self.tweet_list = []

        #Fichier à télécharger pour pouvoir utiliser textblob pour trouver le topic d'un tweet
        nltk.download("brown")
        nltk.download("punkt")
        

    def extraire_mots_mentions_hashtags(self, chaine):
        # rechercher les mots après "@" et "#"
        mentions = re.findall(r'@(\w+)', chaine)
        hashtags = re.findall(r'#(\w+)', chaine)
        
        return mentions, hashtags        

    def extraire_sujets(self, texte):
        blob = TextBlob(texte)
        sujets = blob.noun_phrases  # Extrait les groupes de mots qui représentent des sujets
        return sujets

    def analyser_sentiment(self, texte):
        #Fonction qui analyse les sentiments d'un tweet utilisant 
        blob = TextBlob(texte)

        polarite = blob.sentiment.polarity
        #Retourne le sentiment du tweet en fonction de la polarite
        if polarite > 0:
            sentiment = "positif"
        elif polarite < 0:
            sentiment = "négatif"
        else:
            sentiment = "neutre"

        return sentiment

    #méthode qui permet de charger le stack à partir de tweets sous forme de dictionnaire que l'on mettra dans l'objet tweet
    def charger_liste_stack(self, tweet_to_add):

        new_tweet = tweet.Tweet()

        #On peut remplacer cette étape par une méthode dans la class tweet
        for cle, s_cle in zip(new_tweet.dictionnaire_tweet.keys(), tweet_to_add.keys()):
            new_tweet.dictionnaire_tweet[cle] = tweet_to_add[s_cle]  

        new_tweet.nettoyer_tweet() #On nettoie le tweet (on enleve les caractères spéciaux)

        mentions, hashtags = self.extraire_mots_mentions_hashtags(new_tweet.dictionnaire_tweet["tweet_text"])
        sentiment = self.analyser_sentiment(new_tweet.dictionnaire_tweet["tweet_text"])
        liste_des_sujets = self.extraire_sujets(new_tweet.dictionnaire_tweet["tweet_text"])


        new_tweet.dictionnaire_tweet["mentions"] = mentions
        new_tweet.dictionnaire_tweet["hashtags"] = hashtags
        new_tweet.dictionnaire_tweet["sentiment"] = sentiment
        new_tweet.dictionnaire_tweet["liste_des_sujets"] = liste_des_sujets

        self.tweet_list.append(new_tweet)

    def charger_clean_stack(self):
        with open(self.fichier_json, 'w') as fichier_json:
            for i in range (len(self.tweet_list)):
                json.dump(self.tweet_list[i].dictionnaire_tweet, fichier_json)
                fichier_json.write("\n")
