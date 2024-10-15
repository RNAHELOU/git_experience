import sqlite3
from sense_emu import SenseHat
import time

# Initialize Sense HAT
sense = SenseHat()

# Create or connect to an SQLite database
conn = sqlite3.connect('sense_hat_data.db')
cursor = conn.cursor()

# Create a table if it doesn't exist (only storing temperature, pressure, and humidity)
cursor.execute('''
CREATE TABLE IF NOT EXISTS sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature REAL,
    pressure REAL,
    humidity REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

def log_sensor_data():
    # Define color variables
    vert = (0, 255, 0)
    rouge = (255, 0, 0)
    bleu = (0, 0, 255)

    while True:
        # Read sensor values
        pression = sense.get_pressure()
        humidite = sense.get_humidity()
        temperature = sense.get_temperature()

        # Insert temperature, pressure, and humidity data into the database
        cursor.execute('''
        INSERT INTO sensor_data (temperature, pressure, humidity) 
        VALUES (?, ?, ?)
        ''', (temperature, pression, humidite))
        
        # Commit the transaction
        conn.commit()

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

        # Wait for 1 minute before taking the next measurement
        time.sleep(60)


