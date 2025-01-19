import gradio as gr
import analyse



class Gui:

    def __init__(self, df):

        #la dataframe liée
        self.df = df


    def lancement(self):
        #création de l'affichage avec les inputs, les outputs, et la liste des choix qui vont executer une fonction en conséquences
        #et cela renverra le résultat soit dans un output image, ou alors un output text
        
        self.iface_multiple_choices = gr.Interface(
            fn=self.map_choice,  
            inputs=[gr.Radio(["extraire top k hashtags", "extraire top k utilisateurs mentionnees", "extraire top k utilisateurs", "extraire top k topics",
                              "nombre publications par utilisateurs", "nombre de publications par hashtags", 
                              "nombre de publications par topics", "liste tweets avec utilisateur spécifique", "liste des tweets où l'utilisateur x a été mentionné", "liste des utilisateur qui ont utilisé un hashtags spécifique", "liste des utilisateurs qui ont utilisé une mention spécifique"], label="Choisissez une action"),
                    gr.Number(precision=0, value=1, minimum=1, label="Donnez la valeur de k pour les traitements necessaires"),
                    gr.Textbox(label="Donnez un id, ou le pseudo pour les mentions, ou alors un hashtags (en fonction de ce que vous voulez faire)")],
             outputs=[
            gr.Image(label="Graphique de données"),  
            gr.Textbox(label="Données brutes")  
            ],
            live=True,
            title="InPoDa"
        )
        
        # Ouvre automatiquement le navigateur avec l'adresse du serveur local

        self.iface_multiple_choices.launch(inbrowser=True)

        
        
    #fonction avec la liste des choix et qui appelle la fonction correspondante
    def map_choice(self, choice, k, txt):
        if choice == "extraire top k hashtags":
            return analyse.extraire_top_k_hashtags(k, self.df)
        if choice == "extraire top k utilisateurs mentionnees":
            return analyse.top_k_utilisateur_mentionnes(k, self.df)
        if choice == "extraire top k utilisateurs":
            return analyse.top_k_max_indices(k, self.df)
        if choice == "extraire top k topics":
            return analyse.top_k_topics(k, self.df)
        if choice == "nombre publications par utilisateurs":
            return None, analyse.nb_publi_utilisateur(self.df)
        if choice == "nombre de publications par hashtags":
            return None, analyse.nb_publi_hashtags(self.df)
        if choice == "nombre de publications par topics":
            return None, analyse.nb_publi_topics(self.df)
        if choice == "liste tweets avec utilisateur spécifique":
            return analyse.liste_tweets_utilisateur(self.df, txt)
        if choice == "liste des tweets où l'utilisateur x a été mentionné":
            return analyse.liste_tweets_mention_utilisateur(self.df, txt)
        if choice == "liste des utilisateur qui ont utilisé un hashtags spécifique":
            return analyse.utilisateur_with_hash(self.df, txt)
        if choice == "liste des utilisateurs qui ont utilisé une mention spécifique":
            return analyse.utilisateur_with_mention(self.df, txt)