import turtle

sc = turtle.Screen()
sc.colormode(255)
sc.bgcolor('black')
    

def spiral_rose(obj):
    """create a rose-like shape, in spiraling form."""
    obj.speed(30)
    for i in range(1,101,3):
        for c in ['red','maroon','pink']:
            obj.pencolor(c)
            obj.forward(i)
            obj.right(55)

    obj.forward(40)



def peacock(o1,o2,o3,o4):
    """creates a shape resembling feathers of a peacock."""
    o1.speed(200)
    o2.speed(200)
    o3.speed(200)
    o4.speed(200)
    
    l=15
    o1.pencolor('blue')
    o1.left(120)
    for i in range(70):
        o1.forward(i)
        o1.left(l)
        l-=1
    o1.teleport(0,0)
    l=15
    o1.pencolor('blue')
    o1.right(135)
    for i in range(70):
        o1.forward(i)
        o1.right(l)
        l-=1

    l=15
    o2.pencolor('cyan')
    o2.left(90)
    for i in range(70):
        o2.forward(i)
        o2.left(l)
        l-=1
    o2.teleport(0,0)
    l=15
    o2.pencolor('cyan')
    o2.right(75)
    for i in range(70):
        o2.forward(i)
        o2.right(l)
        l-=1
    
    l=15
    o3.pencolor('green')
    o3.left(50)
    for i in range(70):
        o3.forward(i)
        o3.left(l)
        l-=1
    o3.teleport(0,0)
    l=15
    o3.pencolor('green')
    o3.right(-5)
    for i in range(70):
        o3.forward(i)
        o3.right(l)
        l-=1

    l=15
    o4.pencolor('white')
    o4.left(30)
    for i in range(70):
        o4.forward(i)
        o4.left(l)
        l-=1
    o4.teleport(0,0)
    l=15
    o4.pencolor('white')
    o4.right(-45)
    for i in range(70):
        o4.forward(i)
        o4.right(l)
        l-=1

    
    
def spiral(obj):
    """creates a spiral with 6 different colors."""
    obj.speed(100)

    obj.width(2)
    c=['red','maroon','pink','white','yellow','orange']
    for i in range(1,256):
        obj.pencolor(c[i%6])
        obj.forward(i)
        obj.left(62)
    obj.forward(70)



def dragon_scale(obj):
    """creates a dragon-scale-like pattern."""
    obj.speed(100)
   
    obj.width(1)
    #c=['red','maroon','pink','white','yellow','orange']
    for i in range(1,36):

        obj.color(i*6,150+i*3,i*3)
        obj.left(10)
        obj.begin_fill()
        for j in range(9):
            obj.forward(300)
            obj.left(200)
        obj.end_fill()
    
    



def flower(obj):
    """creates a flower pattern."""
    obj.speed(100)
    k=100
    for i in range(1,26):

        obj.color(200+i*2,i*3,100+i*2)
        obj.right(75)
        obj.begin_fill()
        for j in range(10):
            obj.forward(k)
            obj.right(70)
        obj.end_fill()
        k-=2


def shell(obj):
    """creates a shell pattern."""
    obj.speed(100)   
    obj.width(1)
    c=['red','white','yellow','orange']
    j=0
    for i in reversed(range(2,201,4)):
        obj.color(c[j])
        obj.begin_fill()
        obj.left(12)
        obj.circle(i)
        obj.end_fill()
        j+=1
        if j==4:
            j=0


def snowflake(obj):
    """creates a snowflake patterm."""
    obj.speed(100)
    for i in range(11,41):

        obj.color(0,i*4,i*6)
        obj.right(85)
        obj.begin_fill()
        for j in range(15):
            obj.forward(150)
            obj.right(145)
        obj.end_fill()



if __name__ == "__main__":
    def sketch():
        t=turtle.Turtle()
        t2=turtle.Turtle()
        t3=turtle.Turtle()
        t4=turtle.Turtle()
        spiral_rose(t)
        sc.resetscreen()
        peacock(t,t2,t3,t4)
        sc.resetscreen()
        spiral(t)
        sc.resetscreen()
        dragon_scale(t)
        sc.resetscreen()
        flower(t)
        sc.resetscreen()
        shell(t)
        sc.resetscreen()
        snowflake(t)
        
        
        sc.exitonclick()

sketch()
