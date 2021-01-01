import instaloader
L = instaloader.Instaloader()
# Utente instagram
user = "utente"
# Password utente instagram
password = "password"
L.login(user, password)
# Richiedo le informazioni
profile = instaloader.Profile.from_username(L.context, user)
# Apro il file dove scrivere i dati
f= open("instagram.txt","w+")
# Scrivo solo l'informazione dei followers
f.write(str(profile.followers))
f.close()
