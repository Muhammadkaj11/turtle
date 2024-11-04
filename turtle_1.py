import turtle
turtle.Screen().bgcolor("red")
sc=turtle.Screen()
sc.setup(400,300)

turtle.title("polygon on a canvas")
board=turtle.Turtle()
for i in range(6):
    board.forward(100)
    board.right(60)
    i+=1
turtle.done()