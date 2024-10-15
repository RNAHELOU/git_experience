from sense_emu import SenseHat
import time

# Initialisation
hat = SenseHat()
sense = SenseHat()
hat.clear()

tuple_names = ("temp", "pression", "humid")
i = 0  # Index global pour suivre la variable actuelle

# Fonction d'affichage
def affichage(event):
    global i  # Permet de modifier 'i' dans la fonction

    if event.action in ('pressed', 'held'):
        # Gestion du mouvement vers la gauche
        if event.direction == 'left':
            if i > 0:
                i -= 1
            else:
                print("Vous êtes déjà au début du tuple.")

        # Gestion du mouvement vers la droite
        elif event.direction == 'right':
            if i < len(tuple_names) - 1:
                i += 1
            else:
                print("Vous êtes déjà à la fin du tuple.")

        # Affichage après la mise à jour de l'index
        sense.show_message(f"{tuple_names[i]} : {int(get_data()[i])}", text_colour=(255, 0, 0), scroll_speed=0.08)

def get_data():
    # Récupération des données de capteur
    temperature = sense.get_temperature()
    pression = sense.get_pressure()
    humidite = sense.get_humidity()
    return (temperature, pression, humidite)

# Assigner les événements de joystick à la fonction 'affichage'
hat.stick.direction_left = affichage
hat.stick.direction_right = affichage

# Boucle infinie pour que le programme continue à répondre aux événements du joystick
while True:
    time.sleep(0.1)  # Petite pause pour ne pas surcharger le CPU
