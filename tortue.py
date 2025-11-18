import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(0) # maximum speed

def equilateral(longueur):
    """
    longueur(int) : la longueur du côté du triangle
    Dessine un triangle équilatéral de côté <longueur>
    """
    for _ in range(3):
        t.forward(longueur)
        t.right(180-60)

#equilateral(100)

def carre(longueur):
    """
    longueur(int) : la longueur du côté du carré
    Dessine un carré de côté <longueur>
    """
    for _ in range(4):
        t.forward(longueur)
        t.right(90)
#carre(100)

def polygone(longueur, nb_cotes):
    """
    longueur(int) : la longueur du côté du polygone
    nb_cotes : le nombre de côtés du polygone
    dessine un polygone de longueur de côtés <longueur> et de nombre de côtés <nb_cotes>
    """
    for _ in range(nb_cotes):
        t.forward(longueur)
        t.right(360/nb_cotes)
polygone(100, 6)

turtle.exitonclick()


