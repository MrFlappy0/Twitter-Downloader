import subprocess

modules_to_install = ['tweepy', 'requests', 'wget']

def check_and_install_modules():
    for module in modules_to_install:
        try:                                  #installation des modules necessaires pour le code    
            __import__(module)
        except ImportError:
            subprocess.call(['pip', 'install', module])

check_and_install_modules()

#----------------------------------------------------------------------------------------------------

#importer les bibliothèques nécessaires
import tweepy
from tweepy import OAuthHandler
import wget
import os

#authentification
consumer_key = "PWunYWB8pmHgKQoSlHMn6KLHQ"
consumer_secret = "NxOKjljYFu02w0BBVF4XqawFu65xkhd39XpUiDsYGXZ41IdDVM"
access_token = "3336315365-lwXrlMcXVp716HR1O3IXzv8QeQYmxkiTo46B52t"
access_token_secret = "hmphoEK6Fu84y0uQyzAcfPdFEqiAbd2EyVE1r5IbmJHnY"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# créer un objet api
api = tweepy.API(auth)

#prendre le nom d'utilisateur de l'utilisateur
username = input("Veuillez entrer le nom d'utilisateur Twitter :")

#prenez le nombre d'images à télécharger de l'utilisateur
num_images = int(input("Veuillez entrer le nombre d'images que vous souhaitez télécharger (conseil ne dépassé pas 80 ):"))

# obtenir les tweets de l'utilisateur
tweets = api.user_timeline(screen_name=username,count=100)

# créer un dossier avec le nom de l'utilisateur
folder_path = "Downloads/Twitter/" + username
os.makedirs(folder_path, exist_ok=True)

# aller dans le dossier
os.chdir(folder_path)

# télécharger les images
count = 0
for status in tweets:
    media = status.entities.get('media',[])
    if(len(media) > 0 and count < num_images):
        wget.download(media[0]['media_url'])
        count += 1

print("{} images ont été téléchargées avec succès".format(num_images))