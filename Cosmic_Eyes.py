import turtle
from turtle import *
import math
import random
import time
import winsound

# defines the width and height of the window
WIDTH, HEIGHT = 600, 600

def scene3_2():
    pantalla2 = turtle.Screen() # Create the screen and assign its characteristics
    pantalla2.clear()
    pantalla2.setup(WIDTH, HEIGHT)
    pantalla2.bgcolor("black")
    pantalla2.title("COSMIC EYE") 

    pantalla2.bgpic("Awesome2.gif") 
    pantalla2.update()
    time.sleep(2) # Set the background pic to use as a template 

    frase1 = ["You assembled the INTEGRATED ","SCIENCE INSTRUMENT MODULE!!"]
    frase2 = ["The ISIM is the heart of the James Webb Space ","Telescope, It contains the four main ",
            "instruments that will detect light from ", "distant stars, galaxies, and planets."]
    frase3 = ["The Webb's four science instruments will ","receive the light collected by the telescope ",
            "and use its tools (cameras, spectrographs, ","coronagraphs, etc.) designed to maximize the ",
            "knowledge gained from every observation. Each ","instrument also has a field of view that is ",
            "unique in orientation, shape and area."]

    a = -110
    b = 150 # Assign the x and y values to the paragraphs 
    for frase in frase1: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 16 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = -220
    b = 75
    for frase in frase2:
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 16
        for frase in frase:
            for letter in frase:
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10)

    a = -220
    b = -10
    for frase in frase3:
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 16
        for frase in frase:
            for letter in frase:
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10)
    time.sleep(2)

def scene3_1():
    pantalla2 = turtle.Screen() # Create the screen and assign its characteristics
    pantalla2.clear()
    pantalla2.setup(WIDTH, HEIGHT)
    pantalla2.bgcolor("black")
    pantalla2.title("COSMIC EYE") 

    pantalla2.bgpic("Congrats2.gif")
    pantalla2.update()
    time.sleep(2) # Set the background pic to use as a template 

    frase1 = ["You assembled the","JAMES WEBB SPACE","TELESCOPE!!"] # Create arrays with every line of the sentences
    frase2 = ["This telescope was launched","on December 25th, 2021. To","achieve this, thousands of",
            "scientists, engineers and","technicians from 14 countries","worked together for almost 2",
            "decades."]
    frase3 = ["The James Webb Space Telescope is the largest","most powerful and precise telescope ever",
            "created!"]
    frase4 = ["One of the Webbs goals is to look “back in","time” to when galaxies where young, it will do",
            "this by observing galaxies at over 13 billion","light years away."]

    a = -110
    b = 140 # Assign the x and y values to the paragraphs 

    for frase in frase1: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b) 
        b = b - 18 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = -220
    b = 63 # Assign the x and y values to the paragraphs 
    for frase in frase2: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 18 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = -220
    b = -83 # Assign the x and y values to the paragraphs 
    for frase in frase3: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 18 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase:# Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = -220
    b = -160 # Assign the x and y values to the paragraphs
    for frase in frase4: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 18 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    time.sleep(2)

# Global bools 
isMirror1 = False
isMirror2 = False
isIsim = False
isAntenna = False
isMomentum_flap = False
isSolar_array = False
isSpacecraft_bus_star = False
isSunshield = False

# Function to initialize and define the app window
def screen_turtle():
    screen = turtle.Screen()
    screen.clearscreen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("black")
    screen.title("JWST Puzzle!")
    screen.bgpic("fondoFinal.gif")
    return screen

# Save .gif files as possible options for Turtle objects
def registerShapes():
    # Parts of the JWST
    pTelescope = ["mirror1.gif", "mirror2.gif", "ISIM.gif", "antenna.gif", "momentum_flap.gif", "solar_array.gif", "spacecraft_bus_star.gif", "sunshield.gif"]
    for part in pTelescope:
        turtle.register_shape(part)

    # Assembled by parts
    pArmedTelescope = ["f1JW.gif", "f2JW.gif", "f3JW.gif", "f4JW.gif", "f5JW.gif", "f6JW.gif", "f7JW.gif", "f8JW.gif"]
    for pArmed in pArmedTelescope:
        turtle.register_shape(pArmed)

    # Extra images
    imgExtras = ["jimmybee_happy.gif", "JWST_silueta.gif", "jimmybee_talk.gif"]
    for imgEx in imgExtras:
        turtle.register_shape(imgEx)

# Code for scene three
def third_scene():
    # Ghost Turtle (helps create dialog boxes and text)
    ghost = turtle.Turtle()
    ghost.hideturtle()

    # Draw the box above
    ghost.penup()
    ghost.setpos(-300, 260)
    ghost.pendown()
    ghost.pencolor("grey")
    ghost.pensize(80)
    ghost.speed(0)
    ghost.forward(600)

# The following functions allow us to drag and drop each element individually --

def mirror1_fxn(x, y): 
    mirror1.ondrag(None)
    mirror1.setheading(mirror1.towards(x, y)) # Rotates and moves forward mouse direction
    mirror1.goto(x, y) # Moves the object to the new coords
    mirror1.ondrag(mirror1_fxn) 

def mirror2_fxn(x, y): 
    mirror2.ondrag(None)  
    mirror2.setheading(mirror2.towards(x, y)) 
    mirror2.goto(x, y) 
    mirror2.ondrag(mirror2_fxn)

def isim_fxn(x, y): 
    isim.ondrag(None)  
    isim.setheading(isim.towards(x, y)) 
    isim.goto(x, y) 
    isim.ondrag(isim_fxn)

def antenna_fxn(x, y): 
    antenna.ondrag(None)  
    antenna.setheading(antenna.towards(x, y)) 
    antenna.goto(x, y) 
    antenna.ondrag(antenna_fxn)

def momentum_flap_fxn(x, y): 
    momentum_flap.ondrag(None)  
    momentum_flap.setheading(momentum_flap.towards(x, y)) 
    momentum_flap.goto(x, y) 
    momentum_flap.ondrag(momentum_flap_fxn)

def solar_array_fxn(x, y): 
    solar_array.ondrag(None)  
    solar_array.setheading(solar_array.towards(x, y)) 
    solar_array.goto(x, y) 
    solar_array.ondrag(solar_array_fxn)

def spacecraft_bus_star_fxn(x, y): 
    spacecraft_bus_star.ondrag(None)  
    spacecraft_bus_star.setheading(spacecraft_bus_star.towards(x, y)) 
    spacecraft_bus_star.goto(x, y) 
    spacecraft_bus_star.ondrag(spacecraft_bus_star_fxn)

def sunshield_fxn(x, y): 
    sunshield.ondrag(None)  
    sunshield.setheading(sunshield.towards(x, y)) 
    sunshield.goto(x, y) 
    sunshield.ondrag(sunshield_fxn)

# --------------------------------------------------------------------------

# Does the comparison to determine if the object is within the range to be placed
def posi(turtle):
    return (turtle.xcor() >= -159 and turtle.xcor() <= 159) and (turtle.ycor() >= -101 and turtle.ycor() <= 101)

# In each click, the app will check y there is any item inside the area to be placed
def checkPos(x, y):
    global isMirror1
    global isMirror2
    global isIsim
    global isAntenna
    global isMomentum_flap
    global isSolar_array
    global isSpacecraft_bus_star
    global isSunshield 

    # If an items is in place, the proper part of the JWST will appear as filled on screen 
    if(posi(mirror1)):
        isMirror1 = True
        mirror1.clear()
        mirror1.setpos(300, 300)
        mirror1.hideturtle()
        jwst_figure.shape("f1JW.gif")
        part_Info(1) # The app will display que info of this part of the telescope and their characteristics by calling the function part_Info

    if(isMirror1 and posi(mirror2)):
        isMirror2 = True
        mirror2.clear()
        mirror2.setpos(300, 300)
        mirror2.hideturtle()
        jwst_figure.shape("f2JW.gif")
        part_Info(2)

    if(isMirror2 and posi(isim)):
        isIsim = True
        isim.clear()
        isim.setpos(300, 300)
        isim.hideturtle()
        jwst_figure.shape("f3JW.gif")
        part_Info(3)

    if(isIsim and posi(antenna)):
        isAntenna = True
        antenna.clear()
        antenna.setpos(300, 300)
        antenna.hideturtle()
        jwst_figure.shape("f4JW.gif")
        part_Info(4)

    if(isAntenna and posi(momentum_flap)):
        isMomentum_flap = True
        momentum_flap.clear()
        momentum_flap.setpos(300, 300)
        momentum_flap.hideturtle()
        jwst_figure.shape("f5JW.gif")
        part_Info(5)

    if(isMomentum_flap and posi(solar_array)):
        isSolar_array = True
        solar_array.clear()
        solar_array.setpos(300, 300)
        solar_array.hideturtle()
        jwst_figure.shape("f6JW.gif")
        part_Info(6)

    if(isSolar_array and posi(spacecraft_bus_star)):
        isSpacecraft_bus_star = True
        spacecraft_bus_star.clear()
        spacecraft_bus_star.setpos(300, 300)
        spacecraft_bus_star.hideturtle()
        jwst_figure.shape("f7JW.gif")
        part_Info(7)

    if(isSpacecraft_bus_star and posi(sunshield)):
        isSunshield = True # END
        sunshield.clear()
        sunshield.setpos(300, 300)
        sunshield.hideturtle()
        jwst_figure.shape("f8JW.gif")
        part_Info(8)
        scene3_1()
        time.sleep(5)
        scene3_2()
    # Once the game is completed, isSunshield will be set as True, which means that the game is finished and will display que next part    

# Creates the objects 
def createObjects():
    # Generate and place the jwst_figure in its pos
    jwst_figure.shape("JWST_silueta.gif")
    jwst_figure.penup()
    jwst_figure.setpos(0,0)

    # Generate and place the mirror1 in its pos
    mirror1.shape("mirror1.gif")
    mirror1.left(90)
    mirror1.penup()
    mirror1.setpos(-233.34, 260) # -233.34
    mirror1.speed(0)

    # Generate and place the mirror2 in its pos
    mirror2.shape("mirror2.gif")
    mirror2.left(90)
    mirror2.penup()
    mirror2.setpos(-166.68, 260)
    mirror2.speed(0)

    # Generate and place the isim in its pos
    isim.shape("ISIM.gif")
    isim.left(90)
    isim.penup()
    isim.setpos(-100.02, 260)
    isim.speed(0)
    
    # Generate and place the antenna in its pos
    antenna.shape("antenna.gif")
    antenna.left(90)
    antenna.penup()
    antenna.setpos(-33.36, 260)
    antenna.speed(0)

    # Generate and place the momentum_flap in its pos
    momentum_flap.shape("momentum_flap.gif")
    momentum_flap.left(90)
    momentum_flap.penup()
    momentum_flap.setpos(33.36, 260)
    momentum_flap.speed(0)

    # Generate and place the solar_array in its pos
    solar_array.shape("solar_array.gif")
    solar_array.left(90)
    solar_array.penup()
    solar_array.setpos(100.02, 260)
    solar_array.speed(0)

    # Generate and place the spacecraft_bus_star in its pos
    spacecraft_bus_star.shape("spacecraft_bus_star.gif")
    spacecraft_bus_star.left(90)
    spacecraft_bus_star.penup()
    spacecraft_bus_star.setpos(166.68, 260)
    spacecraft_bus_star.speed(0)

    # Generate and place the sunshield in its pos
    sunshield.shape("sunshield.gif")
    sunshield.left(90)
    sunshield.penup()
    sunshield.setpos(233.34, 260)
    sunshield.speed(0)

    checking = turtle.Turtle()
    checking.hideturtle()
    checking.shape('circle')
    checking.fillcolor("blue")
    checking.penup()
    checking.speed(0)
    checking.setpos(-250, -150)
    checking.pencolor("white")
    checking.write("Check", align="center", font=("Pixelmix", 12, "bold"))
    checking.onclick(checkPos)
    checking.showturtle()

def drawMessage(txt):
    # Ghost Turtle (helps create dialog boxes in this case)
    
    # Draw the box at the bottom
    ghost = turtle.Turtle()
    ghost.hideturtle()
    ghost.penup()
    ghost.setpos(-300, -250)
    ghost.pendown()
    ghost.pencolor("black")
    ghost.pensize(80)
    ghost.speed(0)
    ghost.forward(600)

    # We draw the all mighty jimmy Bee
    jimmyBee = turtle.Turtle()
    jimmyBee.hideturtle()
    jimmyBee.penup()
    jimmyBee.setpos(-250, -250)
    jimmyBee.shape("jimmybee_happy.gif")
    jimmyBee.showturtle()

    # Show the Jimmy Bee text
    ghost_INFO = turtle.Turtle()
    ghost_INFO.hideturtle()
    ghost_INFO.penup()
    ghost_INFO.setpos(-210, -235)
    ghost_INFO.pendown()
    ghost_INFO.pencolor("white")
    ghost_INFO.penup()

    # This FOR loop allows us to write letter by letter
    for letter in txt:
        
        jimmyBee.shape("jimmybee_talk.gif")
        if ghost_INFO.xcor() < 290: # As long as the letters do not reach 290 pixels of the window (right limit)
            ghost_INFO.write(letter, align="left", font=("Pixelmix", 8, "bold"))
            jimmyBee.shape("jimmybee_happy.gif")
            ghost_INFO.fd(10)

        else: # When it reaches it, start writing on the bottom line
            ghost_INFO.setpos(-210, ghost_INFO.ycor() - 18)
            ghost_INFO.write(letter, align="left", font=("Pixelmix", 8, "bold"))
            jimmyBee.shape("jimmybee_happy.gif")
            ghost_INFO.fd(10)

        # In case we encounter a dot, the system will erase que previous text written after a second and continue writing on a fixed position
        if letter == '.':
            time.sleep(1)
            ghost_INFO.clear()
            ghost_INFO.setpos(-210, -235)
    time.sleep(3)

# This function allow us to manage the different texts that will be displayed during the playthrough
def part_Info(num):

    txtMirror1 = "The primary mirror consists of 18 hexagonal segments made of beryllium, which is both strong and light. IT has the function to intercept red and infrared light traveling through space, this light is then reflected and then analyzed to obtain the images. The detail it can see is directly related to the size of the surface area that collects the light of the objects observed in this case the hexagons are extremely big (1,32 meters of diameter)"
    txtMirror2 = "The second mirror is where the cosmos light hits the telescope. It is supported by three 25 feet long struts that are extended from the primary mirror. This mirror is perfectly rounded and  convex so the reflective surface bulges toward a light source."
    txtISIM = "The Integrated Science Instrument Module, also known as the ISIM contains the four main instruments that will detect light from galaxies, distant stars, and planets. These four instruments are extremely sensitive and precise.  It can be said that the ISIM “It's the heart of the Telescope”."
    txtAntenna = "The high gain antenna is the main data antenna and main mean of communication between the telescope and the controllers on Earth. Also, the Webbs science data and imagery is transmitted to Earth from this antenna."
    txtMomentum = "The momentum trim flap helps balance pressure from solar radiation on Webb's sunshield, much like a trim tab helps stabilize a boat or plane!"
    txtSolarArray = "The solar panels effectively ensure the production of electrical energy for the telescope, this way all the systems are always running. The role of the solar panels is to power the scientific instruments and enable the communication systems."
    txtBusStar = "The data from the star tracker helps to point the telescope towards the target so that it appears in the field of view of the intended analysis instrument. The spacecraft bus contains six subsystems: Electrical Power Subsystem, Altitude Control Subsystem, Communication Subsystem, Command and Data Handing Subsystem, Propulsion Subsystem, and the Thermal Control Subsystem."
    txtSunshield = "The sun shield is a set of 5 layers that work together to reduce the temperatures by 570 degrees Fahrenheit. The reason for this structure  is to radiate the heat between the layers that are made of Kapton, aluminum and silicons; this combination provides tolerance to extreme temperature variations."
    
    # Each num corresponds to an object on the screen and it also has a unique text message
    if num == 1:
        drawMessage(txtMirror1)

    elif num == 2:
        drawMessage(txtMirror2)

    elif num == 3:
        drawMessage(txtISIM)

    elif num == 4:
        drawMessage(txtAntenna)

    elif num == 5:
        drawMessage(txtMomentum)
    
    elif num == 6:
        drawMessage(txtSolarArray)

    elif num == 7:
        drawMessage(txtBusStar)

    elif num == 8:
        drawMessage(txtSunshield)

def scene3():
    txtStart = "Hello there Commander, in order to assemble this you need to place in order each element, don't forget to click in check to confirm your progress!"

    # Call functions in order to be performed
    screen = screen_turtle() # Creates and initializes the app window
    registerShapes() # Saves que .gif into shapes

    drawMessage(txtStart)
    third_scene() # Calls the third_scene to create the top Menu
    createObjects()

    # Calls to the function that drag and drop the items
    mirror1.ondrag(mirror1_fxn)
    mirror2.ondrag(mirror2_fxn)
    isim.ondrag(isim_fxn)
    antenna.ondrag(antenna_fxn)
    momentum_flap.ondrag(momentum_flap_fxn)
    solar_array.ondrag(solar_array_fxn)
    spacecraft_bus_star.ondrag(spacecraft_bus_star_fxn)
    sunshield.ondrag(sunshield_fxn)
    screen.mainloop()

# Create our turtle Objects (outside and before scene3) that we will use
jwst_figure = turtle.Turtle()
mirror1 = turtle.Turtle()
mirror2 = turtle.Turtle()
isim = turtle.Turtle()
antenna = turtle.Turtle()
momentum_flap = turtle.Turtle()
solar_array = turtle.Turtle()
spacecraft_bus_star = turtle.Turtle()
sunshield = turtle.Turtle()

def scene2():

    listaimagenes = ["F1_5_9intro.gif","F2_4intro.gif","F3intro.gif","F2_4intro.gif","F1_5_9intro.gif","F6_8intro.gif","F7intro.gif","F6_8intro.gif",
                "F1_5_9intro.gif","F11intro.gif","F12intro.gif","F13intro.gif","F14intro.gif","F15intro.gif","F16intro.gif","F17intro.gif","F18intro.gif",
                "F19intro.gif","F20intro.gif","F21intro.gif","F22intro.gif","F23intro.gif","F24intro.gif","F25intro.gif","F26intro.gif","F27intro.gif",
                "F28intro.gif","F29intro.gif","F30intro.gif","F31intro.gif","F32intro.gif","F33intro.gif","F34intro.gif","F35intro.gif","F36intro.gif",
                "F37intro.gif","F38intro.gif","F39intro.gif","F40intro.gif","F41intro.gif","F42intro.gif","F43intro.gif","F44intro.gif"]

    # creates an array with the images that we will use througout the code

    pantalla2 = turtle.Screen() # create a window with its characteristics
    pantalla2.clearscreen()
    pantalla2.setup(WIDTH, HEIGHT)
    pantalla2.bgcolor("black")
    pantalla2.title("COSMIC EYE") 

    for i in listaimagenes: # shows the images from the array in order, using a loop
        pantalla2.bgpic(i)
        pantalla2.update()
        time.sleep(0.25)

    fantasma = turtle.Turtle()
    fantasma.hideturtle()
    fantasma.penup()
    fantasma.setpos(-300, -250)
    fantasma.pendown()
    fantasma.pencolor("black")
    fantasma.pensize(80) 
    fantasma.forward(600) # creates the text rectangle that will be displayed in the window

    score_pen = turtle.Turtle()
    score_pen2 = turtle.Turtle()
    score_pen.speed(0)
    score_pen2.speed(0)
    score_pen.color("white")
    score_pen2.color("white")
    score_pen.penup()
    score_pen2.penup()
    score_pen.setposition(-270, -250)
    score_pen2.setposition(-270, -270)
    scorestring = "HELP!! A micrometeorite just hit us and all the pieces"
    scorestring2 = "are flying away, please help me get them back."
    score_pen.write(scorestring, False, align="left", font=("PixelMix", 11, "normal"))
    score_pen2.write(scorestring2, False, align="left", font=("PixelMix", 11, "normal"))
    score_pen.hideturtle()
    score_pen2.hideturtle()

    turtle.onkey(scene3, 'a') # adds an atribute so that when 'a' is pressed, we move to the next scene of the game
    time.sleep(5)

def main():
    # creates menu backgound and size
    menu = turtle.Screen()
    menu.setup(WIDTH, HEIGHT)
    menu.bgcolor("black")
    menu.title("Cosmic Eyes")
    menu.bgpic("MENU.gif")
    menu.update()

    # writes title and text
    titulo = turtle.Turtle()
    titulo.hideturtle()
    titulo.penup()
    titulo.setpos(-145, -200)
    titulo.pendown()
    titulo.pencolor("white")
    texto1 = "COSMIC EYES"
    texto2 = "*Press 'A' to start"
    titulo.penup()

    
    for letter1 in texto1:
        titulo.write(letter1, align="center", font=("Pixelmix", 30, "bold"))
        titulo.fd(30)

    titulo.setpos(-90, -240)
    for letter2 in texto2:
        titulo.write(letter2, align="center", font=("Pixelmix", 12, "bold"))
        titulo.fd(10)

    # press 'a' to start the game
    menu.listen()
    menu.onkey(scene2,'a')
    menu.mainloop()

main()