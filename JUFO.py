import GPIO
import zugriff_auf_sqlite
import espeak
name="rasp1" #name des Raspeberrys :D

r1=False #Raum Nummer 1, hier im Beispiel Archiv
r2=False #Standesamt

while True:
  r1=teste_ob_gedrueckt("r1")
  r2=teste_ob_gedrueckt("r2")
  if r1=True:
    lese_text(auslesen(1,name))
  if r2=True:
    lese_text(auslesen(2,name))
