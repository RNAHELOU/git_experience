def minigrille():
    for x in range(380, 400 , 20):
        cadrillage = graphique.create_line(x, 0, x, 100, fill="gray")
    for y in range(380, 400 , 20):
        cadrillage = graphique.create_line(y, 0, y, 100, fill="gray")