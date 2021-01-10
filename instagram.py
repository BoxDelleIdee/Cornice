#!/usr/bin/python3
import instaloader
import sys
L = instaloader.Instaloader()
# Utente instagram
user = "boxdelleidee"
# Password utente instagram
password = "1n1z14l3!"
L.login(user, password)
# Richiedo le informazioni
profile = instaloader.Profile.from_username(L.context, user)
# Apro il file dove scrivere i dati
if ( sys.argv[1] == "minuto" ):
    f= open("/home/pi/Cornice/instagram.txt","w+")
if ( sys.argv[1] == "giorno" ):
    f= open("/home/pi/Cornice/instagram_giorno.txt","w+")
if ( sys.argv[1] == "settimana" ):
    f= open("/home/pi/Cornice/instagram_settimana.txt","w+")
# Scrivo solo l'informazione dei followers
f.write(str(profile.followers))
f.close()
