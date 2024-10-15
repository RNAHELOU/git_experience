from sense_emu import SenseHat
import time

sense = SenseHat()

# Get initial sensor data
def get_sensor_data():
    temperature = sense.get_temperature()
    pression = sense.get_pressure()
    humidite = sense.get_humidity()
    return temperature, pression, humidite

tuple_names = ("temp", "pression", "humid")

def affichage(event):
    # Get the latest sensor data
    tuple_data = get_sensor_data()
    
    if event.direction == 'left':
        sense.show_message(f"{tuple_names[1]}: {int(tuple_data[1])}", text_colour=(255, 0, 0), scroll_speed=0.08)

sense.stick.direction_left = affichage
sense.stick.direction_rifght = affichage
    

# Keep the program running
