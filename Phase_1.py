from turtle import Turtle
def repeat_shape(demo_1):
    for i in range(15):
        demo_1.forward(50)
        demo_1.left(90)
        demo_1.forward(50)
        demo_1.left(90)
        demo_1.forward(50)
        demo_1.left(90)
        demo_1.forward(50)
        demo_1.left(90)
        demo_1.left(30)



demo_1=Turtle()
repeat_shape(demo_1)
