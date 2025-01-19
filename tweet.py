import re

class Tweet:
    #Constructeur qui contient le dictionnaire tweet qui contient la structure du tweet
    
    def __init__(self):
        self.dictionnaire_tweet = {
            "tweet_id": "",
            "author_location": "",
            "created_at": "",
            "retweet_count": "",
            "tweet_language": "",
            "tweet_text": ""
        }

    #méthode qui permet de nettoyer la chaine en elevant tous les caractères non essentiels, comme les smileys par exemple
    def nettoyer_chaine(self,chaine):
        chaine_nettoyee = re.sub(r"[^a-zA-Z0-9/_,-.@# ]", "", chaine)
        return chaine_nettoyee
    
    #methode qui nettoie tout le tweet (donc tout le dictionnaire)
    def nettoyer_tweet(self):
        for key in self.dictionnaire_tweet.keys():
            self.dictionnaire_tweet[key] = self.nettoyer_chaine(self.dictionnaire_tweet[key])
