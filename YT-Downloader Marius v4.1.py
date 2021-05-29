from logging import addLevelName
import urllib.request
import re
from emoji.core import emojize
from pytube import YouTube
import os
import time
import emoji



def my_start():

    linkPattern = "www.youtube.com"
    helpPattern = "help"
    userSearch = (input("What are you looking for? \n>> ")).replace(" ", "+")

    if linkPattern in userSearch:
        yt = YouTube(userSearch)
    elif helpPattern == userSearch:
        print("Commands: \n1.Type help for help \n2.Insert a YouTube link to download that video \n3.Enter any word for youtube search + Download")
        my_start()
    else: 

        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + userSearch)
        video_ids = re.findall(r"watch\?v(\S{12})", html.read().decode())

        yt = YouTube("https://www.youtube.com/watch?v" + video_ids[0])

    

    userContinue = (input("Is: " + yt.title + " the Video you want to download? (yes/no) \n>> ")).lower()
    if(userContinue == "yes"):
        my_download(yt)
    elif(userContinue == "no"):
        my_start()



def my_download(yt):

    
      

    userType = (input("What format do you convert in? (mp3/mp4) \n>> ")).lower()

    if(userType == "mp3"):  
        ys = yt.streams.filter(only_audio=True).first()


    elif(userType == "mp4"):
        ys = yt.streams.get_highest_resolution()

    print(ys.title + " is downloading...")

    #ys = yt.streams.get_highest_resolution()

    time.sleep(5)

    destination = './Downloads'

    # download the file
    out_file = ys.download(output_path=destination)

    if(userType == "mp3"): 
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)


    #ys.download()
    print(emoji.emojize("Download complete :beaming_face_with_smiling_eyes:"))

    userOpen = (input("Do you want to open the file? (yes/no) ")).lower()

    if (userOpen == "yes"):
        if(userType == "mp3"):
            os.startfile(new_file)
        elif(userType == "mp4"):
            os.startfile(out_file)

    print("\n\nThank you for using this application.")
    print("----------------------------------")
    print("This window will close automatically in 5 seconds...")

    time.sleep(5)

    #print("https://www.youtube.com/watch?v" + video_ids[0])
    #print("https://www.youtube.com/watch?v" + video_ids[1])
    #print("https://www.youtube.com/watch?v" + video_ids[2])
    #print("https://www.youtube.com/watch?v" + video_ids[3])
    #print("https://www.youtube.com/watch?v" + video_ids[4])

print("-------- [YT-Downloader] by Marius --------")


linkPattern = "www.youtube.com"
helpPattern = "help"
userSearch = (input("What are you looking for? \n>> ")).replace(" ", "+")

if linkPattern in userSearch:
    yt = YouTube(userSearch)
elif helpPattern == userSearch:
    print("Commands: \n1.Type help for help \n2.Insert a YouTube link to download that video \n3.Enter any word for youtube search + Download")
    my_start()
else: 

    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + userSearch)
    video_ids = re.findall(r"watch\?v(\S{12})", html.read().decode())
    yt = YouTube("https://www.youtube.com/watch?v" + video_ids[0])

    

    userContinue = (input("Is: " + yt.title + " the Video you want to download? (yes/no) \n>> ")).lower()
    if(userContinue == "yes"):
        my_download(yt)
    elif(userContinue == "no"):
        my_start()





userSearch = (input("What are you looking for? \n>> ")).replace(" ", "+")
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + userSearch)
video_ids = re.findall(r"watch\?v(\S{12})", html.read().decode())

yt = YouTube("https://www.youtube.com/watch?v" + video_ids[0])

userContinue = (input("Is: " + yt.title + " the Video you want to download? (yes/no) \n>> ")).lower()

if(userContinue == "yes"):
    my_download(yt)
elif(userContinue == "no"):
    my_start()

