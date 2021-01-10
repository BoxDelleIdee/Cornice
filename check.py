#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import requests,json
#aggiunta del path per la libreria del display
# Acquisizione dei dati dell'account di Youtube
URL = "https://www.googleapis.com/youtube/v3/channels"
type = "statistics"
# ID del canale di Youtube che vogliano acquisire
channelid = "UCUM4XNBvSlpDVgc92bx_B5g"
# API che bisogna di attivare per poter eseguire la richiesta del dato
apikey = "AIzaSyDSQD0q_k6v0T_njfxnONBuJ-J-r7eFdfM"
PARAMS = {('part', type), ('id',channelid), ('key',apikey)}
# invio della richiesta del dato
r = requests.get(url = URL, params = PARAMS)
data = r.json()
# Acquisiione del numero degli iscritti
iscritti = int(data['items'][0]['statistics']['subscriberCount'])
# Acquisizione del numero totale delle visite
visite_totali= int(data['items'][0]['statistics']['viewCount'])
# Acquisizione del numero dei video pubblicati
video_totali= int(data['items'][0]['statistics']['videoCount'])

if ( sys.argv[1] == "giorno"):
    f=open("/home/pi/Cornice/youtube_day.txt", "w+")
if ( sys.argv[1] == "settimana"):
    f=open("/home/pi/Cornice/youtube_week.txt", "w+")
f.write(str(iscritti)+"-"+str(visite_totali))
f.close()

url = 'https://www.boxdelleidee.it'
r = requests.get(url, allow_redirects=True)
Indice_Total_User = r.content.find("Total Users : ")
Indice_Total_User_Fine = r.content.find("</div>",Indice_Total_User)
utenti=(r.content[Indice_Total_User+14:Indice_Total_User_Fine])
Indice_Total_User = r.content.find("Total views : ")
Indice_Total_User_Fine = r.content.find("</div>",Indice_Total_User)
visite=(r.content[Indice_Total_User+14:Indice_Total_User_Fine])
if ( sys.argv[1] == "giorno"):
    f=open("/home/pi/Cornice/site_day.txt", "w+")
if ( sys.argv[1] == "settimana"):
    f=open("/home/pi/Cornice/site_week.txt", "w+")
f.write(utenti+"-"+visite)
f.close()



