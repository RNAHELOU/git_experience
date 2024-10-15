from sense_emu import SenseHat
import sqlite3
from datetime import datetime
import time
# Initialisation du Sense HAT
sense = SenseHat()

# Connexion à la base de données SQLite
connect = sqlite3.connect("bdd_stationmeteo.db")
cursor = connect.cursor()

# Création de la table si elle n'existe pas déjà
cursor.execute('''
               CREATE TABLE IF NOT EXISTS bdd(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               temperature REAL,
               pression REAL,
               humidite REAL,
               date DATETIME DEFAULT date_actuel
               )
               ''')

def enmarche():
    # Définir les variables de couleur
    vert = (0, 255, 0)
    rouge = (255, 0, 0)
    bleu = (0, 0, 255)
    gris = (128,128,128)

    while True:
        # Lire les valeurs des capteurs
        pression = sense.get_pressure()
        humidite = sense.get_humidity()
        temperature = sense.get_temperature()
        date_actuel = datetime.now()
        print("Date actuelle:", date_actuel)
         
        data_tuple = (temperature , pression , humidite)

        cursor.execute('''
        INSERT INTO bdd (temperature, pression, humidite , date) 
        VALUES (?, ?, ?, ?)
        ''', (temperature, pression, humidite, date_actuel))

        connect.commit()
        # Obtenir les valeurs de l'accéléromètre
        x, y, z = sense.get_accelerometer_raw().values()
        x = abs(x)
        y = abs(y)
        z = abs(z)

        # Déterminer la couleur en fonction de la température
        if temperature < 15:
            color = bleu
        elif 15 <= temperature <= 25:
            color = vert
        else:
            color = rouge



        # Afficher les valeurs des capteurs sur la matrice LED
        # sense.show_message(f"Temp: {int(temperature)}", text_colour=color, scroll_speed=0.08)
        # sense.show_message(f"Press: {int(pression)}", text_colour=bleu, scroll_speed=0.08)
        # sense.show_message(f"Humid: {int(humidite)}", text_colour=gris, scroll_speed=0.08)

        # Pause pour permettre de lire le message
        time.sleep(60)
def defillement(event):
    if event.direction in ('pressed','held'):
        sense.show_message(f" {nom_tuple[i]} : {data_tuple[i]}")

sense.stick.direction_left = defillement
# Lancer la fonction
enmarche()
