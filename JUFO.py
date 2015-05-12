import GPIO.py
import zugriff_auf_sqlite.py
import espeak.py
name="rasp1" #name des Raspeberrys :D

Archiv=False
Standesamt=False

while True:
  Archiv=teste_ob_gedrueckt(Archiv)
  Standesamt=teste_ob_gedrueckt(Standesamt)
  if Archiv=True:
    lese_text(auslesen(name,"Archiv"))
  if Standesamt=True:
    lese_text(auslesen(name,"Archiv"))
