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
font12 = ImageFont.truetype('/home/pi/Cornice/font/Font.ttc', 12)
font24 = ImageFont.truetype('/home/pi/Cornice/font/Font.ttc', 24)
font32 = ImageFont.truetype('/home/pi/Cornice/font/Font.ttc', 32)
font_12 = ImageFont.truetype('/home/pi/Cornice/font/Phosphate.ttc', 12)
font_24 = ImageFont.truetype('/home/pi/Cornice/font/Phosphate.ttc', 24)
font_32 = ImageFont.truetype('/home/pi/Cornice/font/Phosphate.ttc', 32)
font_36 = ImageFont.truetype('/home/pi/Cornice/font/Phosphate.ttc', 36)


try:
    
    #Configurazione dell'acquisizione delle previsioni del tempo
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Ladispoli"
    #API_KEY è la chiave da registrare sul sito di openweathermap
    API_KEY = "aab268254923f4729ae63b3183fa73cd"
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

    # Esecuzione del programma in python3 per l'acquisizione del numero degli iscritti al canale
    instagram_exe=os.system("python3 instagram.py minuto")

    # Apertura del file dove instagram.py ha salvato il numero degli iscritti al canale
    f=open("/home/pi/Cornice/instagram.txt", "r")
    instagram=f.read()
    f.close()
    f=open("/home/pi/Cornice/instagram_giorno.txt", "r")
    instagram_giorno=f.read()
    f.close()
    f=open("/home/pi/Cornice/instagram_settimana.txt", "r")
    instagram_settimana=f.read()
    f.close()
    f=open("/home/pi/Cornice/youtube_day.txt", "r")
    youtube_day=f.read()
    f.close()
    f=open("/home/pi/Cornice/youtube_week.txt", "r")
    youtube_week=f.read()
    f.close()
    f=open("/home/pi/Cornice/site_day.txt", "r")
    site_day=f.read()
    f.close()
    f=open("/home/pi/Cornice/site_week.txt", "r")
    site_week=f.read()
    f.close()

    # Acquisizione del numero totale degli utenti e delle visite sul sito di interesse
    url = 'https://www.boxdelleidee.it'
    r = requests.get(url, allow_redirects=True)
    Indice_Total_User = r.content.find("Total Users : ")
    Indice_Total_User_Fine = r.content.find("</div>",Indice_Total_User)
    utenti=(r.content[Indice_Total_User+14:Indice_Total_User_Fine])
    Indice_Total_User = r.content.find("Total views : ")
    Indice_Total_User_Fine = r.content.find("</div>",Indice_Total_User)
    visite=(r.content[Indice_Total_User+14:Indice_Total_User_Fine])

    epd = epd7in5b_HD.EPD()
    # Inizializzazione del monitor
    epd.init()
    # Pulizia del monitor
    epd.Clear()

    # Creazione dell'immagine con colore nero
    blackImage = Image.new('1', (epd.width, epd.height), 255)
    # Creazione dell'immagine con colore rosso
    redImage = Image.new('1', (epd.width, epd.height), 255)
    draw_blackImage = ImageDraw.Draw(blackImage)
    draw_redImage = ImageDraw.Draw(redImage)
    # Caricamento delle immagini da utilizzare su vari oggetti
    griglia= Image.open('/home/pi/Cornice/bmp/880_528.bmp')
    logo_youtube= Image.open('/home/pi/Cornice/bmp/youtubeIcon.bmp')
    scritta_youtube= Image.open('/home/pi/Cornice/bmp/Q2-2.bmp')
    logo_instagram= Image.open('/home/pi/Cornice/bmp/Q3.bmp')
    scritte_youtube= Image.open('/home/pi/Cornice/bmp/Q2-3.bmp')
    scritte_instagram= Image.open('/home/pi/Cornice/bmp/Q3-2.bmp')
    logo_facebook= Image.open('/home/pi/Cornice/bmp/Q3-3.bmp')
    logo_datario= Image.open('/home/pi/Cornice/bmp/Q4-1.bmp')
    logo_tempo= Image.open('/home/pi/Cornice/bmp/Q4-2.bmp')
    logo_web= Image.open('/home/pi/Cornice/bmp/Q4-3.bmp')
    logo = Image.open('/home/pi/Cornice/bmp/Q1.bmp')

   # Inserimento delle scritte sul layer nero e rosso
    draw_blackImage.text((550, 295), today, font = font32, fill = 0)
    draw_blackImage.text((550, 355), CITY+" temp. "+temperatura, font = font32, fill = 0)
    draw_blackImage.text((550, 390), cielo, font = font24, fill = 0)
    draw_blackImage.text((480, 130), "Iscritti: ", font = font_32, fill = 0)
    draw_blackImage.text((480, 170), "Visite: ", font = font_32, fill = 0)
    draw_blackImage.text((480, 210), "Video: ", font = font_32, fill = 0)
    draw_blackImage.text((30, 354), "Iscritti: ", font = font_32, fill = 0)
    draw_blackImage.text((240, 354), "D:+ ", font = font_32, fill = 0)
    draw_blackImage.text((340, 354), "W:+ ", font = font_32, fill = 0)
    draw_blackImage.text((680, 130), "D:+ ", font = font_32, fill = 0)
    draw_blackImage.text((780, 130), "W:+ ", font = font_32, fill = 0)
    draw_blackImage.text((680, 170), "D:+ ", font = font_32, fill = 0)
    draw_blackImage.text((780, 170), "W:+ ", font = font_32, fill = 0)
    draw_blackImage.text((15, 470), "D:+ ", font = font_32, fill = 0)
    draw_blackImage.text((110, 470), "W:+ ", font = font_32, fill = 0)
    draw_blackImage.text((240, 470), "D:+ ", font = font_32, fill = 0)
    draw_blackImage.text((340, 470), "W:+ ", font = font_32, fill = 0)
    draw_blackImage.text((15, 430), "Utenti: ", font = font_32, fill = 0)
    draw_blackImage.text((260, 430), "Visite: ", font = font_32, fill = 0)

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
    draw_redImage.text((285, 350), str(int(instagram)-int(instagram_giorno)), font = font_36, fill = 0)
    draw_redImage.text((395, 350), str(int(instagram)-int(instagram_settimana)), font = font_36, fill = 0)
    draw_redImage.text((610, 127), str(iscritti), font = font_36, fill = 0)
    day=youtube_day.split("-")
    week=youtube_week.split("-")
    days=site_day.split("-")
    weeks=site_week.split("-")
    draw_redImage.text((725, 130), str(int(iscritti)-int(day[0])), font = font_36, fill = 0)
    draw_redImage.text((835, 130), str(int(iscritti)-int(week[0])), font = font_36, fill = 0)
    draw_redImage.text((725, 170), str(int(visite_totali)-int(day[1])), font = font_36, fill = 0)
    draw_redImage.text((835, 170), str(int(visite_totali)-int(week[1])), font = font_36, fill = 0)
    draw_redImage.text((590, 167), str(visite_totali), font = font_36, fill = 0)
    draw_redImage.text((590, 209), str(video_totali), font = font_36, fill = 0)
    draw_redImage.text((125, 430), str(utenti), font = font_36, fill = 0)
    draw_redImage.text((355, 430), str(visite), font = font_36, fill = 0)
    draw_redImage.text((60, 470), str(int(utenti)-int(days[0])), font = font_32, fill = 0)
    draw_redImage.text((165, 470), str(int(utenti)-int(weeks[0])), font = font_32, fill = 0)
    draw_redImage.text((285, 470), str(int(visite)-int(days[1])), font = font_32, fill = 0)
    draw_redImage.text((395, 470), str(int(visite)-int(weeks[1])), font = font_32, fill = 0)
    draw_redImage.text((450, 435), "www.boxdelleidee.it", font = font_36, fill = 0)
    draw_blackImage.text((450, 485), "Versione 1.0 ", font = font24, fill = 0)
    draw_redImage.text((700, 485), "JOB 0001", font = font24, fill = 0)
    epd.display(epd.getbuffer(blackImage),epd.getbuffer(redImage))

    epd.Dev_exit()


except IOError as e:
    logging.info(e)

except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5b_HD.epdconfig.module_exit()
    exit()
