import sqlite3
from datetime import datetime

# Connexion à la base de données
connect = sqlite3.connect("test_tesmp.db")
cursor = connect.cursor()

# Création de la table avec un champ DATETIME
cursor.execute('''
               CREATE TABLE IF NOT EXISTS bdd(
               date DATETIME DEFAULT CURRENT_TIMESTAMP
               )
               ''')

# Vérifier la structure de la table
cursor.execute("PRAGMA table_info(bdd)")
table_info = cursor.fetchall()
print("Structure de la table:", table_info)

# Obtenir la date actuelle
date_actuel = datetime.now()
print("Date actuelle:", date_actuel)

# Insertion des données dans la base de données
try:
    cursor.execute('''INSERT INTO bdd (date) 
                      VALUES (?)''', (date_actuel,))
    connect.commit()
    print("Insertion réussie")
except Exception as e:
    print("Erreur lors de l'insertion:", e)

# Vérifier les données insérées
cursor.execute("SELECT * FROM bdd")
data = cursor.fetchall()
print("Données dans la base:", data)

