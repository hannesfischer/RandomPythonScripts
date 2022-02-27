import subprocess, sys
from os import path
file_path = path.dirname(__file__)

print(file_path)
exit()
s = subprocess.Popen(file_path + "/test.bat", shell=True)
s.communicate()
