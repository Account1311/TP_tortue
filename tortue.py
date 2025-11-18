import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(0) # maximum speed

def equilateral(longueur):
    """
    longueur(int) : la longueur du côté du triangle
    Dessine un triangle équilatéral de côté <longueur>
    """
    polygone(longueur, 3)
    

#equilateral(100)

def carre(longueur):
    """
    longueur(int) : la longueur du côté du carré
    Dessine un carré de côté <longueur>
    """
    polygone(longueur, 4)
    

def polygone(longueur, nb_cotes, ajout=0, deviation=0):
    """
    longueur(int) : la longueur du côté du polygone
    nb_cotes : le nombre de côtés du polygone
    ajout : 
    dessine un polygone de longueur de côtés <longueur> et de nombre de côtés <nb_cotes>
    """
    total_dev = 0
    for _ in range(nb_cotes):
        longueur += ajout
        t.forward(longueur)
        t.right(360/nb_cotes + total_dev)
        total_dev = total_dev + deviation
        
polygone(100, 4,deviation = -10)





turtle.exitonclick()


