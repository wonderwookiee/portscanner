#!usr/bin/python3

import sys 
import socket
from datetime import datetime

#Define Target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  #Translate Hostname to IPV4
else:
    print("invalid amount of arguments.")  
    print("Syntax: portscanner.py")
# Banner 
print("-------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------")
print("$$$$$$$\   $$$$$$\  $$$$$$$\ $$$$$$$$\        $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$\   $$\ $$$$$$$$\ $$$$$$$\"")  
print("$$   _$$\ $$   _$$\ $$  __$$\\__$$  __|       $$  __$$\ $$  __$$\ $$  __$$\ $$$\  $$ |$$$\  $$ |$$  _____|$$  __$$\"") 
print("$$ |  $$ |$$ /  $$ |$$ |  $$ |  $$ |         $$ /  \__|$$ /  \__|$$ /  $$ |$$$$\ $$ |$$$$\ $$ |$$ |      $$ |  $$ |")
print("$$$$$$$  |$$ |  $$ |$$$$$$$  |  $$ |         \$$$$$$\  $$ |      $$$$$$$$ |$$ $$\$$ |$$ $$\$$ |$$$$$\    $$$$$$$  |")
print("$$  ____/ $$ |  $$ |$$  __$$<   $$ |          \____$$\ $$ |      $$  __$$ |$$ \$$$$ |$$ \$$$$ |$$  __|   $$  __$$< ")
print("$$ |      $$ |  $$ |$$ |  $$ |  $$ |         $$\   $$ |$$ |  $$\ $$ |  $$ |$$ |\$$$ |$$ |\$$$ |$$ |      $$ |  $$ |")
print("$$ |       $$$$$$  |$$ |  $$ |  $$ |         \$$$$$$  |\$$$$$$  |$$ |  $$ |$$ | \$$ |$$ | \$$ |$$$$$$$$\ $$ |  $$ |")
print("\__|       \______/ \__|  \__|  \__|          \______/  \______/ \__|  \__|\__|  \__|\__|  \__|\________|\__|  \__|")
print("-------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------Created by Marc Peacock For educational Purposes.--")
print("Scanning Target ")
print("Time Sarted: "+str(datetime.now()))
print("-------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------")

try:
    for port in range(1,500):
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       socket.setdefaulttimeout(1)
       result = s.connect_ex((target,port))     #returns an error indacator
       if result == 0:
          print("port {} is open".format(port))
    s.close()

        
except KeyboardInterrupt:
    print ("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved!")
except socket.error:
    print("coludnt connect to server!")   


