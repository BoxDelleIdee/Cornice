#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import time
import os
from datetime import datetime
from datetime import date
#Preparazione della data da mostrare
date_time = datetime.now()
print(date_time.minute)
variable = int(date_time.minute)
if variable >=0 and variable <= 10:
    risultato=os.system("cp /home/pi/Cornice/bmp/Q1-1.bmp /home/pi/Cornice/bmp/Q1.bmp")
if variable >=11 and variable <= 20:
    risultato=os.system("cp /home/pi/Cornice/bmp/Q1-2.bmp /home/pi/Cornice/bmp/Q1.bmp")
if variable >=21 and variable <= 30:
    risultato=os.system("cp /home/pi/Cornice/bmp/Q1-3.bmp /home/pi/Cornice/bmp/Q1.bmp")
if variable >=31 and variable <= 40:
    risultato=os.system("cp /home/pi/Cornice/bmp/Q1-4.bmp /home/pi/Cornice/bmp/Q1.bmp")
if variable >=41 and variable <= 50:
    risultato=os.system("cp /home/pi/Cornice/bmp/Q1-5.bmp /home/pi/Cornice/bmp/Q1.bmp")
if variable >=51 and variable <= 59:
    risultato=os.system("cp /home/pi/Cornice/bmp/Q1-6.bmp /home/pi/Cornice/bmp/Q1.bmp")

