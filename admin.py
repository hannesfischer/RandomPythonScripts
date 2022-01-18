from re import sub
import subprocess, sys
from os import path
file_path = path.dirname(sys.argv[0])

s = subprocess.Popen(file_path + "/test.bat", shell=True)
s.communicate()
