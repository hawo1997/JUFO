# auf rasp müssen espeak, mbrola und mbrola-de5 installiert sein
import os

def lese_text(t):
  os.system('espeak -v mb-de5+f1 -s 125 "{0}"'.format(t))
lese_text("Wer möchte heute mit mir Kuchen backen")
