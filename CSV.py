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
        self.Followers_List=[]
        self.Following_List=[]
        self.Average_Followers=0
        self.Average_Following=0


    def Comptes(self):
        for i in self.ListeTrie:
            if "https://twitter.com/" in i:
                compte=i.split("https://twitter.com/")[1]
                if '?lang=fr' in compte:
                    compte=compte.split("?")[0]
            self.Listes_des_Comptes.append(compte)


    def Subs_And_Followings_Average(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        for i in self.Listes_des_Comptes:
            try:
                user = api.get_user(i)

                self.Following_List.append(user.friends_count)
                self.Followers_List.append(user.followers_count)
            except:
                pass

        self.Average_Followers = round(sum(self.Followers_List)/len(self.Followers_List))
        self.Average_Following = round(sum(self.Following_List)/len(self.Following_List))


