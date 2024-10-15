from sense_emu import SenseHat
import time

sense = SenseHat()

def affichage(event):
    get(event.direction)
    sense.show_message("test", text_colour=(255, 0, 0), scroll_speed=0.08)


hat.stick.direction_right = affichage
get(event.direction)