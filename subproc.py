import subprocess
import socket

from os import path

try:
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



except:
    pass