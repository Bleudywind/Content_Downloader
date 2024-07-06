import subprocess
from colorama import Fore, Back, Style

success = False
while (not success):
    print()
    print("What do we do today ?")
    print("1. Download music")
    print("2. Download video")
    print("3. Quit")
    choice = input()
    print()

    if choice != "1" and choice != "2" and choice != "3":
        print(Fore.RED + "Wrong answer !")
        print(Style.RESET_ALL)
        print()
    else :
        if choice == "3":
            print(Fore.GREEN + "Have a nice day !")
            break
        print("Give me an url to download: ")
        url = input()
        print()
        print("Optionnaly you can give a name of directory otherwise it be put in default folder: ")
        directoryname = input()
        if choice == "1":
            tests = subprocess.run(["python", "playlistMusicDownloader.py", url, directoryname])
            print(tests)
            print(Fore.GREEN + "Success")
            print(Style.RESET_ALL)
        elif choice == "2":
            subprocess.run(["python", "playlistVideoDownloader.py", url, directoryname])
            print(Fore.GREEN + "Success")
            print(Style.RESET_ALL)
print(Style.RESET_ALL)