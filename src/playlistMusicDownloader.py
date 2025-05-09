import os
import sys
import subprocess
from pytubefix import Playlist
from fnmatch import fnmatch

# https://www.youtube.com/playlist?list=PL2c5UJq64ZpHeSeD8HPyMSdsj06B5aNKx Marc Rebillet to test
print()
patternMp4 = "*.mp4"
patternMp3 = "*.mp3"
patternMp4a = "*.m4a"

try:
    playlistName = sys.argv[1]
except:
    print("Please specify an url for the playlist")
    sys.exit(1)

if (len(playlistName) == 0):
    print("Please specify an url for the playlist")
    sys.exit(1)


defaultDirectory = "./Musiques/Default/"
newDirectory = False
targetDirectory="target/Musiques"

try:
    directoryName = "./Musiques/" + sys.argv[2] + "/"
    newDirectory = True
except:
    directoryName = "./Musiques/Default/"

if (len(directoryName) == 0):
    directoryName = "./Musiques/Default/"


playlist = Playlist(playlistName)

try:
    os.mkdir("Musiques")
    os.mkdir("Musiques/Default")
except Exception as e:
    print("\nFound Download Directory\n")


try:
    print("Downloading playlist named: " + playlist.title)
except:
    print("Could not retrieve playlist please verify the given url")
    sys.exit(1)

i = 1
for video in playlist.videos:
    
    try:
        print(str(i) + ". " + video.title)
        video.streams.get_audio_only().download('./Musiques/Default')
    except Exception as e:
        print("Could not download a video")
        print(e)
    i = i + 1

print("The playlist is downloaded !")
# print("\nConverting playlist to mp3")
# 
# for path, subdirs, files in os.walk('./'):
#     for name in files:
#         if fnmatch(name, patternMp4):
#             oldName = name
#             name = name.split(".")
#             name = name[0] + ".mp3"
#             os.rename(os.path.join(path, oldName), os.path.join(path, name))
# 
# print("Audio files converted !")
# print("\nFormating name of audio files")
# 
# try:
#     subprocess.run(["python", "Verify.py"])
# except:
#     print("The video could not be formated. They will remain in Musiques/Default directory")
#     print("Poor little video :(")
#     sys.exit(1)
# 
# # subprocess.run(["python", "Sort.py"])
# 
# print("\nAudio files has been formated")
print("\nMoving them into a better place")


if newDirectory:
    try:
        os.mkdir(directoryName)
    except Exception as e:
        print(e)
        print("Directory already exist")



for path, subdirs, files in os.walk('Musiques/Default'):
    for name in files:
        if fnmatch(name, patternMp4a):
            try:
                os.rename(os.path.join(path, name), os.path.join(directoryName, name))
            except Exception as e:
                print(e)
                print("File already exist")

print("Done, you can retrieve them into " + directoryName)
print("Enjoy mixing !")
sys.exit(0)