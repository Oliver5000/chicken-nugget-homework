import pgzrun

WIDTH = 500
HEIGHT = 600
nugget = Actor("oip")
nugget.x = 250
nugget.y = 300
def draw():
    screen.fill("White")
    nugget.draw()
    screen.draw.text("this is a chicken nugget!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",(50,300),color = "black")
    
pgzrun.go()