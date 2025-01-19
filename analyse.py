
import pandas as pd
import matplotlib.pyplot as plt
import os


#On vérifie si le dossier est bien présent à la racine, sinon on le crée
newpath = r'.\images' 
if not os.path.exists(newpath):
    os.makedirs(newpath)


def extraire_top_k_hashtags(k, df):
    
    #On vérifie le type de la variable k si c'est bien un entier
    if not isinstance(k, int):
        return None, "Pas de resultats (pensez à vérifier vos inputs)"
    else:
        tous_les_hashtags = [hashtag for liste_hashtags in df['hashtags'] for hashtag in liste_hashtags]

        # Utiliser value_counts pour compter le nombre d'occurrences de chaque hashtag
        top_hashtags = pd.Series(tous_les_hashtags).value_counts()

        top_k_hashtags = top_hashtags.head(k)

        
        plt.pie(top_k_hashtags, labels=top_k_hashtags.index, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')  # Assurer que le diagramme est un cercle

        # Afficher le titre
        plt.title(f"Top {k} Hashtags")

        # Sauvegarder le diagramme comme une image
        plt.savefig("images/topkhashtag.png")

        return "images/topkhashtag.png", None

def top_k_max_indices(k, df):
    #On vérifie le type de la variable k si c'est bien un entier
    if not isinstance(k, int):
        return None, "Pas de resultats (pensez à vérifier vos inputs)"
    

    else:
        # On compte chaque occurence de tweet en fonction de l'ID
        top_users = df.groupby('tweet_id')['retweet_count'].sum()

        # Utiliser sort_values pour trier les utilisateurs en fonction du total des retweets
        top_users_sorted = top_users.sort_values(ascending=False)

        top_k_users = top_users_sorted.head(k)

        # On affiche les résultats dans un diagramme sous forme de cercle

        plt.pie(top_k_users, labels=top_k_users.index, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title(f"Top {k} Users")
        
        plt.savefig("images/topkusers.png")
        
        return "images/topkusers.png", None

def top_k_utilisateur_mentionnes(k, df):
    #On vérifie le type de la variable k si c'est bien un entier
    if not isinstance(k, int):
        return None, "Pas de resultats (pensez à vérifier vos inputs)"
    else:

        #On explode les mentions pour pouvoir les compter
        df_exploded_mentions = df.explode('mentions')

        # Utiliser value_counts pour compter le nombre d'occurrences de chaque utilisateur mentionné
        top_mentions = df_exploded_mentions['mentions'].value_counts()

        # Spécifier le Top K des utilisateurs mentionnés que vous souhaitez obtenir (par exemple, les 5 premiers)
        top_k_mentions = top_mentions.head(k)

        #On crée l'interface
        plt.pie(top_k_mentions, labels=top_k_mentions.index, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title(f"Top {k} utilisateurs mentionnes")
        
        plt.savefig("images/topkusers_mention.png")

        return "images/topkusers_mention.png", None

def top_k_topics(k ,df):
    #On vérifie le type de la variable k si c'est bien un entier
    if not isinstance(k, int):
        return None, "Pas de resultats (pensez à vérifier vos inputs)"
    else:
    # On explode les valeurs
        df_exploded_topics = df.explode('liste_des_sujets')

        # Utiliser value_counts pour compter le nombre d'occurrences de chaque sujet
        top_topics = df_exploded_topics['liste_des_sujets'].value_counts()

        # Spécifier le Top K des sujets que vous souhaitez obtenir (par exemple, les 5 premiers)
        top_k_topics = top_topics.head(k)
        
        # on crée l'image du graph
        plt.figure(figsize=(8, 6))
        top_k_topics.plot(kind='bar', color='skyblue')
        
        # Ajouter des titres et des labels
        plt.title(f'Top {k} Sujets')
        plt.xlabel('Sujets')
        plt.ylabel('Nombre d\'occurrences')
        
        #On fait en sorte que tout puisse être lisible:
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout() 

        #On sauvegarde sous forme d'image
        plt.savefig("images/top_k_topics.png")

        return "images/top_k_topics.png", None

def nb_publi_utilisateur(df):

    tweets_par_utilisateur = df.groupby('tweet_id')['tweet_text'].count()

    #On la transforme en data_frame pour pouvoir l'afficher plus simplement
    tweets_par_utilisateur_df = tweets_par_utilisateur.to_frame(name='Nombre de tweets par utilisateur')

    #On vérifie que la df n'est pas vide
    if tweets_par_utilisateur.empty:
        return "Pas de resultats (pensez à vérifier vos inputs)"
    
    # Utiliser to_string pour pouvoir afficher le résultat sur gradio
    result_string = f"Tweets par user :\n{tweets_par_utilisateur_df.to_string()}"
    
    return result_string


def nb_publi_hashtags(df):

    df_exploded_hashtags = df.explode('hashtags')

    # Utiliser value_counts pour compter le nombre d'occurrences de chaque hashtag
    publications_par_hashtag = df_exploded_hashtags['hashtags'].value_counts()
    publi_hash = publications_par_hashtag.to_frame(name="Nombre de publications par hashtag")

    #Verifier que la df n'est pas vide
    if publi_hash.empty:
        return "Pas de resultats (pensez à vérifier vos inputs)"
    
    
    # Utiliser to_string pour pouvoir afficher le résultat sur gradio
    result_string = f"Nombre de publications par hashtags :\n{publi_hash.to_string()}"
    return result_string


def nb_publi_topics(df):
    #On explode la df pour pouvoir compter le nombre d'occurrences
    df_exploded_topics = df.explode('liste_des_sujets')

    # Utiliser value_counts pour compter le nombre d'occurrences de chaque hashtag
    publications_par_topic = df_exploded_topics['liste_des_sujets'].value_counts()
    publi_topic = publications_par_topic.to_frame(name="Nombre de publications par topics")

    #Verifier que la df n'est pas vide
    if publi_topic.empty:
        return "Pas de resultats (pensez à vérifier vos inputs)"
    
    # Utiliser to_string pour pouvoir afficher le résultat sur gradio
    result_string = f"Nombre de publications par topic :\n{publi_topic.to_string()}"
    return result_string

def liste_tweets_utilisateur(df, utilisateur_id):
    #On extrait les tweets de l'utilisateur (on extrait seulement l'id et le tweet_text)
    tweets_utilisateur_specifique = df[df['tweet_id'] == utilisateur_id][['tweet_id', 'tweet_text']]


    #On crée le plot si ce n'est pas vide, sinon on renvoie un msg d'erreur
    if not(tweets_utilisateur_specifique.empty):
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')
        table = ax.table(cellText=tweets_utilisateur_specifique.values, colLabels=tweets_utilisateur_specifique.columns, loc='center', cellLoc= "center")
        table.scale(3,3.5)
        plt.savefig("images/tableau_tweets_utilisateur.png", dpi=400, bbox_inches='tight') 

        return "images/tableau_tweets_utilisateur.png", None
    
    if tweets_utilisateur_specifique.empty:
        return None, "Pas de resultats (pensez à vérifier vos inputs)"
    
   
def liste_tweets_mention_utilisateur(df, pseudo_utilisateur):
    #On extrait les tweets où l'utilisateur a été mentionné (on extrait seulement l'id et le tweet_text)
    tweets_mentionnant_utilisateur = df[df["mentions"].apply(lambda mentions: pseudo_utilisateur in mentions)][['tweet_id', 'tweet_text']]


    #On crée le plot si ce n'est pas vide, sinon on renvoie un msg d'erreur
    if not(tweets_mentionnant_utilisateur.empty):

        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')
        table = ax.table(cellText=tweets_mentionnant_utilisateur.values, colLabels=tweets_mentionnant_utilisateur.columns, loc='center', cellLoc= "center")
        table.set_fontsize(30)
        table.scale(3,3.5)
        plt.savefig("images/tableau_tweets_mentions.png", dpi=400, bbox_inches='tight')
        return "images/tableau_tweets_mentions.png", None
    
    if tweets_mentionnant_utilisateur.empty:
        return None, "Pas de resultats (pensez à vérifier vos inputs)"
     

def utilisateur_with_hash(df, hashtag):
    #on extrait la liste des utilisateur qui ont utilisé un hashtags spécifique
    user = df[df["hashtags"].apply(lambda hashtags: hashtag in hashtags)][["tweet_id"]]

    #si ce n'est pas vide on affiche le resultat sinon on renvoie une erreur
    if user.empty:
        return None, "Pas de resultats (pensez à vérifier vos inputs)"
    result_string = f"Liste des utilisateurs qui ont utilisé ce hashtag :\n{user.to_string()}"
    return None, result_string
   

def utilisateur_with_mention(df, mention):
    #on extrait la liste des utilisateur qui ont utilisé une mention spécifique
    user = df[df["mentions"].apply(lambda mentions: mention in mentions)][["tweet_id"]]

    #si ce n'est pas vide on affiche le resultat sinon on renvoie une erreur
    if user.empty:
        return None, "Pas de resultats (pensez à vérifier vos inputs)"
    result_string = f"Liste des utilisateurs qui ont utilisé cette mention :\n{user.to_string()}"
    return None, result_string



