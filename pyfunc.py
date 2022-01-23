from importlib.metadata import requires
import subprocess
import socket

from os import path

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


try:
    #setExecution Policy:
    run("Set-ExecutionPolicy (Un)restricted") #--> def run():

    #get path of python file:
    import sys
    file_path = path.dirname(sys.argv[0])
    print(file_path)
    #raise SystemError("Errormessage")

    #json lesen

    import json
    json_file = open(file_path + "/options.json").read()    #lese json Daten
    json_data = json.loads(json_file)                       #lese json Daten
    
    json_data["option2"] = "banane"                         #schreibe json Daten
    json_file = open(file_path + "/options.json", "w")      #schreibe json Daten
    json_file.write(json.dumps(json_data, indent=4))        #schreibe json Daten
    json_file.close()   
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
except SystemError as e:
    print(e)
