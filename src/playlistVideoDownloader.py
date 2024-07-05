import os
import sys
import subprocess
from pytube import Playlist
from fnmatch import fnmatch
from datetime import datetime

# https://www.youtube.com/playlist?list=PL2c5UJq64ZpHeSeD8HPyMSdsj06B5aNKx Marc Rebillet to test
print()
patternMp4 = "*.mp4"

global howManyPointBehindLoadingTotal
global howManyPointBehindLoading
global typeOfPoint
global lastSizeOfVideo
global lastTime

howManyPointBehindLoadingTotal= 30
howManyPointBehindLoading = 0
typeOfPoint="."
lastSizeOfVideo=0
lastTime = datetime.now()

def on_progress(stream, chunk, bytes_remaining):

    global howManyPointBehindLoadingTotal
    global howManyPointBehindLoading
    global typeOfPoint
    global lastSizeOfVideo
    global lastTime

    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    
    timenow = datetime.now()
    actualVideoSize = bytes_downloaded
    try:
        speed= str(round(((actualVideoSize - lastSizeOfVideo) /(timenow - lastTime).total_seconds())/1000000, 2))
    except:
        speed = "0"

    pointBehindLoading = typeOfPoint * howManyPointBehindLoading + (howManyPointBehindLoadingTotal - howManyPointBehindLoading) * len(typeOfPoint) * " "
    print(str(round(percentage_of_completion, 2)) + " percents downloaded at " + speed + "Mb/s" + pointBehindLoading, end="\r")
    howManyPointBehindLoading = (howManyPointBehindLoading + 1) % howManyPointBehindLoadingTotal
    lastSizeOfVideo = actualVideoSize

try:
    playlistName = sys.argv[1]
except:
    print("Please specify an url for the playlist")
    sys.exit(1)

if (len(playlistName) == 0):
    print("Please specify an url for the playlist")
    sys.exit(1)

videoDirectory = "Video/"
defaultVideoDirectory= "Default/"
targetDirectory="target/Video"

defaultDirectory = videoDirectory + defaultVideoDirectory
newDirectory = False

try:
    os.mkdir(videoDirectory)
    os.mkdir(defaultDirectory)
except Exception as e:
    print("\nFound Download Directory\n")

try:
    directoryName = videoDirectory + sys.argv[2] + "/"
    newDirectory = True
except:
    directoryName = defaultDirectory

if (len(directoryName) == 0):
    directoryName = defaultDirectory


playlist = Playlist(playlistName)

try:
    print("Downloading playlist named: " + playlist.title)
except:
    print("Could not retrieve playlist please verify the given url")
    sys.exit(1)

i = 1

for video in playlist.videos:
    
    try:
        video.register_on_progress_callback(on_progress)
        print(str(i) + ". " + video.title)
        # .filter(progressive=True)
        video.streams.get_highest_resolution().download(defaultDirectory)
    except Exception as error:
        print("Could not download a video because : "+ error)
    i = i + 1

print("The playlist is downloaded !")
print("\nMoving them into a better place")

if newDirectory:
    try:
        os.mkdir(directoryName)
    except:
        print("Directory allready exist")

for path, subdirs, files in os.walk(defaultDirectory):
    for name in files:
        if fnmatch(name, patternMp4):
            try:
                os.rename(os.path.join(path, name), os.path.join(directoryName, name))
            except Exception as e:
                print(e)
                print("File allready exist")

print("Done, you can retrieve them into " + directoryName)
print("Enjoy your viewing !")