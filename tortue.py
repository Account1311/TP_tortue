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
        
equilateral(100)

turtle.exitonclick()


    