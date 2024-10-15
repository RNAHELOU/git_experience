from sense_emu import SenseHat
hat = SenseHat()

############INIT##############
temp = 24
pression = 1024
humid = 50

tuple_data = (temp, pression, humid)
tuple_names = ("temp", "pression", "humid")

i = 0

while True:
    print(f"Variable actuelle : {tuple_names[i]} = {tuple_data[i]}")
    direction = input("Entrez 'droite' ou 'gauche' : ").lower()
    if direction == 'gauche':
        # Si on va à gauche, on décrémente l'i
        if i > 0:
            i -= 1
        else:
            print("Vous êtes déjà au début du tuple.")
    elif direction == 'droite':
        # Si on va à droite, on incrémente l'i
        if i < len(tuple_data) - 1:
            i += 1
        else:
            print("Vous êtes déjà à la fin du tuple.")
