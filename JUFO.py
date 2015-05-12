import GPIO.py
import zugriff_auf_sqlite.py
import espeak.py
name="rasp1" #name des Raspeberrys :D

r1=False #Raum Nummer 1
r2=False

while True:
  r1=teste_ob_gedrueckt(r1)
  r2=teste_ob_gedrueckt(r2)
  if r1=True:
    lese_text(auslesen(1,name))
  if r2=True:
    lese_text(auslesen(2,name))
