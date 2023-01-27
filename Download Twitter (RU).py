import subprocess

modules_to_install = ['tweepy', 'requests', 'wget']

def check_and_install_modules():
    for module in modules_to_install:
        try:                                  #установка модулей, необходимых для работы кода 
            __import__(module)
        except ImportError:
            subprocess.call(['pip', 'install', module])

check_and_install_modules()

#----------------------------------------------------------------------------------------------------

#импорт необходимых библиотек
import tweepy
from tweepy import OAuthHandler
import wget
import os

# аутентификация
consumer_key = "PWunYWB8pmHgKQoSlHMn6KLHQ"
consumer_secret = "NxOKjljYFu02w0BBVF4XqawFu65xkhd39XpUiDsYGXZ41IdDVM"
access_token = "3336315365-lwXrlMcXVp716HR1O3IXzv8QeQYmxkiTo46B52t"
access_token_secret = "hmphoEK6Fu84y0uQyzAcfPdFEqiAbd2EyVE1r5IbmJHnY"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# создать объект api
api = tweepy.API(auth)

# получить имя пользователя от пользователя
username = input("Пожалуйста, введите имя пользователя Twitter учетной записи:")

# получить количество изображений для загрузки от пользователя
num_images = int(input("Пожалуйста, введите количество изображений, которые вы хотите загрузить:"))

# получить твиты пользователя
tweets = api.user_timeline(screen_name=username,count=200)

# создать папку с именем пользователя
folder_path = "Downloads/Twitter/" + username
os.makedirs(folder_path, exist_ok=True)

# перейти в папку
os.chdir(folder_path)

# загрузить изображения
count = 0
for status in tweets:
    media = status.entities.get('media',[])
    if(len(media) > 0 and count < num_images):
        wget.download(media[0]['media_url'])
        count += 1

print("{} изображения были успешно загружены".format(num_images))