from importlib.metadata import requires
import subprocess
import socket

from os import path

try:
    #get path of python file:
    import sys
    file_path = path.dirname(sys.argv[0])
    print(file_path)
    
    #check admin:
    import ctypes, sys
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            print("Bitte als Administrator ausführen!")
            exit()

    #end check admin


    #prüfen ob Pfad vorhanden?
    res = path.isdir("Path/to/check") 
    print(res)

    #IP Addresse auslesen:
    # import sockets
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()

    #subprocess öffnen
    proc = subprocess.Popen("diskmgmt.msc", shell=True)
    proc.communicate()
    print("finish")

    #diskpart skript ausführen:
    proc = subprocess.Popen(["diskpart.exe", "/s scriptname.txt"], shell=True)
    proc.communicate()

    #user input
    userinput = input("Prompt Text: ")


#exception abfangen:
except Exception as e:
    print("Something went wrong: ")
    print(e)
    pass