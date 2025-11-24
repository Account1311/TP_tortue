import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(0) # maximum speed

def equilateral(longueur, ajout=0, deviation=0):
    """
    longueur(int) : la longueur du côté du triangle
    Dessine un triangle équilatéral de côté <longueur>
    """
    polygone(longueur, 3)
    

#equilateral(100)

def carre(longueur, ajout=0, deviation=0):
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
        
#polygone(100, 4,deviation = -10)

def figure1(longueur, nb_tours):
    for _ in range(nb_tours):
        polygone(longueur, 4, 2, 1)
        longueur += 10

#figure1(20, 1000)


def figure2(longueur, nb_cotes, ajout=0, deviation =0 ):

    for _ in range(100):
        polygone(longueur, 4, 1, 1)
        longueur += 4
        
figure2(20, 4)





def figure3(longueur):

    for _ in range(100):
        carre(longueur)
        t.up()
        t.forward(longueur)
        t.left(60)
        t.down()
        longueur = longueur + 20
        
def figure4(longueur):

    for i in range(8):
        carre(longueur)
        t.up()
        t.forward(longueur)
        t.right(90)
        t.forward(longueur)
        t.right(90)
        t.down()
        longueur = longueur*1.2
        if i%2==0:
            t.left(180)
        
        

#figure4(10)


turtle.exitonclick()


