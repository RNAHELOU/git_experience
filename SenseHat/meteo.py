from sense_emu import SenseHat
import time

# Initialize Sense HAT
sense = SenseHat()

def enmarche():
    # Define color variables
    vert = (0, 255, 0)
    rouge = (255, 0, 0)
    bleu = (0, 0, 255)

    # Read sensor values
    pression = sense.get_pressure()
    humidite = sense.get_humidity()
    temperature = sense.get_temperature()

    # Get accelerometer values
    x, y, z = sense.get_accelerometer_raw().values()
    x = abs(x)
    y = abs(y)
    z = abs(z)

    # Determine color based on temperature
    if temperature < 15:
        color = bleu
    elif 15 <= temperature <= 25:
        color = vert
    else:
        color = rouge

    # Display sensor values on LED matrix
    sense.show_message("Temp: %d" % int(temperature), text_colour=color, scroll_speed=0.08)
    sense.show_message("Press: %d" % int(pression), text_colour=color, scroll_speed=0.08)
    sense.show_message("Humid: %d" % int(humidite), text_colour=color, scroll_speed=0.08)

    # Pause to allow message to be read
    time.sleep(5)

# Call the function
enmarche()
