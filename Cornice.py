#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import requests,json
#aggiunta del path per la libreria del display
sys.path.insert(1, '/home/pi/Cornice/lib')
import logging
from waveshare_epd import epd7in5b_HD
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from datetime import datetime
from datetime import date
#Preparazione della data da mostrare
date_time = datetime.now()
today = str(date.today())
today = date_time.strftime("%d %B, %Y") 

#Definizione dei font da utilizzare
font12 = ImageFont.truetype('font/Font.ttc', 12)
font24 = ImageFont.truetype('font/Font.ttc', 24)
font32 = ImageFont.truetype('font/Font.ttc', 32)
font_12 = ImageFont.truetype('font/Phosphate.ttc', 12)
font_24 = ImageFont.truetype('font/Phosphate.ttc', 24)
font_32 = ImageFont.truetype('font/Phosphate.ttc', 32)
font_36 = ImageFont.truetype('font/Phosphate.ttc', 36)

try:

    #Configurazione dell'acquisizione delle previsioni del tempo
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Ladispoli"
    #API_KEY è la chiave da registrare sul sito di openweathermap
    API_KEY = "API KEY DA OTTENERE"
    # crea la url per la richiesta delle previsioni
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=metric&lang=it"
    # richiesta HTTP 
    response = requests.get(URL)
    # esegue il controllo della risposta alla richiesta
    if response.status_code == 200:
        # acquisizione della risposta in formato json
        data = response.json()
        # acquisizione del blocco principale
        main = data['main']
        # acquisizione della temperatura
        temperature = main['temp']
        # acquisizione dell'umidità
        humidity = main['humidity']
        # acquisizione della pressione atmosferica
        pressure = main['pressure']
        # acquisizione della situazione meteo
        report = data['weather']
        temperatura=str(temperature)
        umidita=str(humidity)
        pressione=str(pressure)
        cielo=str(report[0]['description'])
    else:
        # stampa in console dell'eventuale errore
        print("Error in the HTTP request")

    # Acquisizione dei dati dell'account di Youtube
    URL = "https://www.googleapis.com/youtube/v3/channels"
    type = "statistics"
    # ID del canale di Youtube che vogliano acquisire
    channelid = "IDENTIFICATO DEL CANALE YOUTUBE"
    # API che bisogna di attivare per poter eseguire la richiesta del dato
    apikey = "API KEY DA OTTENERE DALLA DASHBOARD DI GOOGLE"
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

    # Esecuzione del programma in python3 per l'acquisizione del numero degli iscritti al canale    
    instagram_exe=os.system("python3 instagram.py")

    # Apertura del file dove instagram.py ha salvato il numero degli iscritti al canale
    f=open("instagram.txt", "r")
    instagram=f.read()
    f.close()
    
    epd = epd7in5b_HD.EPD()
    # Inizializzazione del monitor
    epd.init()
    # Pulizia del monitor
    epd.Clear()

    # Acquisizione del numero totale degli utenti e delle visite sul sito di interesse
    url = 'https://www.boxdelleidee.it'
    r = requests.get(url, allow_redirects=True)
    Indice_Total_User = r.content.find("Total Users : ")
    Indice_Total_User_Fine = r.content.find("</div>",Indice_Total_User)
    utenti=(r.content[Indice_Total_User+14:Indice_Total_User_Fine])
    Indice_Total_User = r.content.find("Total views : ")
    Indice_Total_User_Fine = r.content.find("</div>",Indice_Total_User)
    visite=(r.content[Indice_Total_User+14:Indice_Total_User_Fine])

    # Creazione dell'immagine con colore nero
    blackImage = Image.new('1', (epd.width, epd.height), 255)
    # Creazione dell'immagine con colore rosso 
    redImage = Image.new('1', (epd.width, epd.height), 255)
    draw_blackImage = ImageDraw.Draw(blackImage)
    draw_redImage = ImageDraw.Draw(redImage)
    # Caricamento delle immagini da utilizzare su vari oggetti
    griglia= Image.open('bmp/880_528.bmp')
    logo_youtube= Image.open('bmp/youtubeIcon.bmp')
    scritta_youtube= Image.open('bmp/Q2-2.bmp')
    logo_instagram= Image.open('bmp/Q3.bmp')
    scritte_youtube= Image.open('bmp/Q2-3.bmp')
    scritte_instagram= Image.open('bmp/Q3-2.bmp')
    logo_facebook= Image.open('bmp/Q3-3.bmp')
    logo_datario= Image.open('bmp/Q4-1.bmp')
    logo_tempo= Image.open('bmp/Q4-2.bmp')
    logo_web= Image.open('bmp/Q4-3.bmp')
    logo = Image.open('bmp/Q1.bmp')
    # Inserimento delle scritte sul layer nero e rosso
    draw_blackImage.text((550, 295), today, font = font32, fill = 0)
    draw_blackImage.text((550, 355), CITY+" temp. "+temperatura, font = font32, fill = 0)
    draw_blackImage.text((550, 390), cielo, font = font24, fill = 0)
    draw_blackImage.text((480, 130), "Iscritti: ", font = font_32, fill = 0)
    draw_blackImage.text((480, 170), "Visite Totali: ", font = font_32, fill = 0)
    draw_blackImage.text((480, 210), "Video Totali: ", font = font_32, fill = 0)
    draw_blackImage.text((30, 354), "Iscritti: ", font = font_32, fill = 0)
    draw_blackImage.text((30, 474), "Utenti: ", font = font_32, fill = 0)
    draw_blackImage.text((240, 474), "Visite: ", font = font_32, fill = 0)
    # Inserimento delle immagini sul layer nero e rosso
    blackImage.paste(logo, (0,0))
    redImage.paste(griglia, (0,0))
    redImage.paste(logo_youtube, (500,30))
    redImage.paste(logo_instagram, (120,264+20))
    redImage.paste(logo_web, (180,264+130))
    blackImage.paste(logo_datario, (450,270))
    blackImage.paste(logo_tempo, (450,350))
    blackImage.paste(scritta_youtube, (630,40))
    draw_redImage.text((160, 350), str(instagram), font = font_36, fill = 0)
    draw_redImage.text((610, 127), str(iscritti), font = font_36, fill = 0)
    draw_redImage.text((690, 167), str(visite_totali), font = font_36, fill = 0)
    draw_redImage.text((690, 209), str(video_totali), font = font_36, fill = 0)
    draw_redImage.text((140, 474), str(utenti), font = font_36, fill = 0)
    draw_redImage.text((340, 474), str(visite), font = font_36, fill = 0)
    draw_redImage.text((450, 435), "www.boxdelleidee.it", font = font_36, fill = 0)
    draw_blackImage.text((450, 485), "Versione 0.9 Beta ", font = font24, fill = 0)
    draw_redImage.text((700, 485), "JOB 0001", font = font24, fill = 0)
    epd.display(epd.getbuffer(blackImage),epd.getbuffer(redImage))

    epd.Dev_exit()
   


except IOError as e:
    logging.info(e)

except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5b_HD.epdconfig.module_exit()
    exit()

