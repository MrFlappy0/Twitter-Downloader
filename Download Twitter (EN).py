import subprocess

modules_to_install = ['tweepy', 'requests', 'wget']

def check_and_install_modules():
    for module in modules_to_install:
        try:                                  ##installation of the necessary modules for the code    
            __import__(module)
        except ImportError:
            subprocess.call(['pip', 'install', module])

check_and_install_modules()

#----------------------------------------------------------------------------------------------------

#import necessary libraries
import tweepy
from tweepy import OAuthHandler
import wget
import os

# authentication
consumer_key = "PWunYWB8pmHgKQoSlHMn6KLHQ"
consumer_secret = "NxOKjljYFu02w0BBVF4XqawFu65xkhd39XpUiDsYGXZ41IdDVM"
access_token = "3336315365-lwXrlMcXVp716HR1O3IXzv8QeQYmxkiTo46B52t"
access_token_secret = "hmphoEK6Fu84y0uQyzAcfPdFEqiAbd2EyVE1r5IbmJHnY"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# make api object
api = tweepy.API(auth)

#take user name from user 
username = input("Please enter the twitter username of the account:")

#take the number of images to download from user
num_images = int(input("Please enter the number of images you wish to upload (tip not to exceed 80 ):"))

# get the tweets of the user
tweets = api.user_timeline(screen_name=username,count=100)

# create a folder with the name of the user
folder_path = "Downloads/Twitter/" + username
os.makedirs(folder_path, exist_ok=True)

# go to the folder
os.chdir(folder_path)

# download the images
count = 0
for status in tweets:
    media = status.entities.get('media',[])
    if(len(media) > 0 and count < num_images):
        wget.download(media[0]['media_url'])
        count += 1

print("{} images have been downloaded successfully".format(num_images))