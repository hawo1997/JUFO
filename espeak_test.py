# auf rasp müssen espeak,  installiert sein
import os

def lese_text(t):
  os.system('espeak -v de+f2 -s 115 "{0}"'.format(t))
lese_text("Die Amateurastronomie wird als Hobby von Liebhaberastronomen betrieben, die im Unterschied zu professionellen Astronomen keine beruflichen Interessen mit ihrer Tätigkeit verfolgen. Intensive Naturerlebnisse unter dem Sternhimmel werden dabei mit dem Einsatz sehr unterschiedlicher optischer und astronomischer Instrumente verbunden. Das Spektrum reicht von einfachen Ferngläsern bis zu hoch entwickelten Teleskopen und Kameras und selbst entwickelten elektronischen Steuerungen. Lange Jahre von einer verschwindend kleinen Minderheit von Begeisterten betrieben, hat sich die Amateurastronomie seit Anfang des 20. Jahrhunderts vor allem in den USA zu einem verbreiteten Hobby entwickelt und seit 1950 auch in Europa.")

