import tkinter as tk
from tkinter import ttk
from sense_emu import SenseHat
import time

# Initialisation du Sense HAT
sense = SenseHat()

# Initialisation de la fenêtre
root = tk.Tk()
root.title("Relevés instantané")

# Variables globales pour suivre les températures minimales et maximales
temperature_min = None
temperature_max = None

# Fonction pour mettre à jour les valeurs de température, d'humidité et de pression
def update_values():
    global temperature_min, temperature_max
    
    # Récupération des valeurs actuelles
    pression = sense.get_pressure()
    humidite = sense.get_humidity()
    temperature = sense.get_temperature()

    # Mise à jour des valeurs dans les labels
    temp_value_label.config(text=f"{temperature:.2f} °C")
    humidity_value_label.config(text=f"{humidite:.2f} %")
    pressure_value_label.config(text=f"{pression:.2f} hPa")
    
    # Mise à jour des températures minimales et maximales
    if temperature_min is None or temperature < temperature_min:
        temperature_min = temperature
        temp_min_label.config(text=f"Min : {temperature_min:.2f} °C")
    
    if temperature_max is None or temperature > temperature_max:
        temperature_max = temperature
        temp_max_label.config(text=f"Max : {temperature_max:.2f} °C")
    
    # Relancer la mise à jour toutes les 2 secondes
    root.after(2000, update_values)

# Création des frames
frame1 = ttk.Frame(root)
frame1.pack(side="top", fill="both", expand=True)
frame2 = ttk.Frame(root)
frame2.pack(side="bottom", fill="both", expand=True)

# Widget pour le titre
title_label = ttk.Label(frame1, text="RELEVES METEO ", font=("Helvetica", 14))
title_label.pack(pady=5)

# Cadre pour les informations de température, humidité et pression
frame_valeurs = ttk.Frame(frame2)
frame_valeurs.pack(pady=10)

# Étiquettes pour les titres
temperature_label = ttk.Label(frame_valeurs, text="TEMPERATURE", font=("Helvetica", 10))
temperature_label.grid(row=0, column=0, padx=20)

humidity_label = ttk.Label(frame_valeurs, text="HUMIDITE", font=("Helvetica", 10))
humidity_label.grid(row=0, column=1, padx=20)

pressure_label = ttk.Label(frame_valeurs, text="PRESSION", font=("Helvetica", 10))
pressure_label.grid(row=0, column=2, padx=20)

# Valeurs actuelles de température, humidité et pression
temp_value_label = ttk.Label(frame_valeurs, text="0.00 °C", font=("Helvetica", 12))
temp_value_label.grid(row=1, column=0, padx=20)

humidity_value_label = ttk.Label(frame_valeurs, text="0.00 %", font=("Helvetica", 12))
humidity_value_label.grid(row=1, column=1, padx=20)

pressure_value_label = ttk.Label(frame_valeurs, text="0.00 hPa", font=("Helvetica", 12))
pressure_value_label.grid(row=1, column=2, padx=20)

# Ajout des températures maximales et minimales enregistrées
temp_min_label = ttk.Label(frame_valeurs, text="Min : - °C", font=("Helvetica", 10))
temp_min_label.grid(row=2, column=0, padx=20)

temp_max_label = ttk.Label(frame_valeurs, text="Max : - °C", font=("Helvetica", 10))
temp_max_label.grid(row=3, column=0, padx=20)

# Lancer la mise à jour initiale des valeurs
update_values()

# Boucle principale
root.mainloop()
