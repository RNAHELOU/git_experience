import tkinter as tk
from tkinter import ttk
from sense_emu import SenseHat
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

# Initialisation du Sense HAT
sense = SenseHat()

# Initialisation des listes de données pour les courbes
temp_values = []
humidity_values = []
pressure_values = []
timestamps = []

# Fonction pour mettre à jour les valeurs de température, d'humidité et de pression
def update_values():
    # Récupération des valeurs actuelles
    pression = sense.get_pressure()
    humidite = sense.get_humidity()
    temperature = sense.get_temperature()

    # Mise à jour des valeurs dans les labels
    temp_value_label.config(text=f"{temperature:.2f} °C")
    humidity_value_label.config(text=f"{humidite:.2f} %")
    pressure_value_label.config(text=f"{pression:.2f} hPa")

    # Stockage des valeurs pour le graphique
    timestamps.append(time.strftime("%H:%M:%S"))
    temp_values.append(temperature)
    humidity_values.append(humidite)
    pressure_values.append(pression)

    # Limite le nombre de points pour éviter la surcharge du graphique
    if len(timestamps) > 20:
        timestamps.pop(0)
        temp_values.pop(0)
        humidity_values.pop(0)
        pressure_values.pop(0)

    # Mise à jour du graphique
    plot_graph()

    # Relancer la mise à jour toutes les 2 secondes
    root.after(2000, update_values)

# Fonction pour tracer le graphique avec trois sous-graphiques
def plot_graph():
    ax1.clear()
    ax2.clear()
    ax3.clear()

    # Graphique de la température
    ax1.plot(timestamps, temp_values, 'g-', label="Température (°C)")
    ax1.set_title("Température")
    ax1.set_ylabel("°C")
    ax1.legend(loc="upper left")
    ax1.grid(True)

    # Graphique de l'humidité
    ax2.plot(timestamps, humidity_values, 'b-', label="Humidité (%)")
    ax2.set_title("Humidité")
    ax2.set_ylabel("%")
    ax2.legend(loc="upper left")
    ax2.grid(True)

    # Graphique de la pression
    ax3.plot(timestamps, pressure_values, 'r-', label="Pression (hPa)")
    ax3.set_title("Pression")
    ax3.set_ylabel("hPa")
    ax3.legend(loc="upper left")
    ax3.grid(True)

    # Rotation des étiquettes de l'axe x pour une meilleure lisibilité
    for ax in (ax1, ax2, ax3):
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    fig.tight_layout()
    canvas.draw()

# Initialisation de la fenêtre Tkinter
root = tk.Tk()
root.title("Relevés instantané")

# Création des frames
frame1 = ttk.Frame(root)
frame1.pack(side="top", fill="both", expand=True)
frame2 = ttk.Frame(root)
frame2.pack(side="bottom", fill="both", expand=True)

# Widget pour le titre
title_label = ttk.Label(frame1, text="RELEVES METEO", font=("Helvetica", 14))
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

# Création du graphique avec trois sous-graphiques
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6), sharex=True)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

# Lancer la mise à jour initiale des valeurs
update_values()

# Boucle principale Tkinter
root.mainloop()
