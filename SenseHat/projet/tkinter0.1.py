import tkinter as tk
from tkinter import ttk

# init fenetre
root = tk.Tk()
root.title("Aquisition instantané")

# Création des frames
frame1 = ttk.Frame(root)
frame1.pack(side="top", fill="both", expand=True)
frame2 = ttk.Frame(root)
frame2.pack(side="bottom", fill="both", expand=True)

# Variables des bouton radio
selection = tk.StringVar()



# Fonction de calcul
def graph():
    try:
        if selection.get() == "+":
            label['text'] = v1 + v2
        elif selection.get() == "-":
            label['text'] = v1 - v2
        elif selection.get() == "*":
            label['text'] = v1 * v2
        elif selection.get() == "/":
            if v2 != 0:
                label['text'] = v1 / v2
            else:
                label['text'] = f"{v1} ne peut pas être divisible par 0 !!!"
        else:
            label['text'] = "Sélectionnez une opération."
    except ValueError:
        label['text'] = "Entrée invalide."


# Widgets 
label_v1 = tk.Label(frame1, text="Variable 1 : ")
label_v1.pack(side="left")

entry_valeur1 = ttk.Entry(frame1, width=15)
entry_valeur1.pack(side="left")
entry_valeur1.focus()

label_v2 = tk.Label(frame1, text="Variable 2 : ")
label_v2.pack(side="left")

entry_valeur2 = ttk.Entry(frame1, width=15)
entry_valeur2.pack(side="left")

# Widgets Boutton radio
rad1 = ttk.Radiobutton(frame2, text="+", variable=selection, value="+")
rad2 = ttk.Radiobutton(frame2, text="-", variable=selection, value="-")
rad3 = ttk.Radiobutton(frame2, text="*", variable=selection, value="*")
rad4 = ttk.Radiobutton(frame2, text="/", variable=selection, value="/")

rad1.pack(side='left')
rad2.pack(side='left')
rad3.pack(side='left')
rad4.pack(side='left')

# Bouton de calcul
bouton_graph = ttk.Button(root, text="Graphique instantanné", command=graph)
bouton_graph.pack(side="bottom")



# Boucle principale
root.mainloop()
