import csv
import os
import tweepy
os.chdir("C:\\Users\\Ridha\\Desktop\\Vues fusionnées")


def Colonne(Numero_Colonne):
    Numero_Colonne-=1
    L=[]
    file = open("1_informations_generales.csv" , "r",encoding='utf8')
    reader = csv.reader(file , delimiter = ";")
    for elt in reader:
        if elt[Numero_Colonne]!='':
            L.append(elt[Numero_Colonne])
    L.pop(0)
    return L

def Tri(Colonne):
    Tri=[]
    for elt in Colonne:
        if elt not in Tri:
            Tri.append(elt)
    return Tri


class Twitter:
    def __init__(self):
        self.data=Colonne(13)
        self.ListeTrie=Tri(self.data)
        self.Listes_des_Comptes=[]
        self.Liste_Subs=[]
        self.Moyenne_Subs=0

    def Comptes(self):
        for i in self.ListeTrie:
            if "https://twitter.com/" in i:
                compte=i.split("https://twitter.com/")[1]
                if '?lang=fr' in compte:
                    compte=compte.split("?")[0]
            self.Listes_des_Comptes.append(compte)


    def Nombre_Subs_Moyenne(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        for i in self.Listes_des_Comptes:
            try:
                user = api.get_user(i)
                self.Liste_Subs.append(user.followers_count)
            except:
                pass
        somme=sum(self.Liste_Subs)
        self.Moyenne_Subs=round(somme/len(self.Liste_Subs))


