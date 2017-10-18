import pygame 

#Initialising Pygame

pygame.init()


#Setting initial variables and params

DISPLAYWIDTH = 800
DISPLAYHEIGHT = 600

displaySurface = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))

pygame.display.set_caption("Dodgey - The Car")

BLACK = (0, 0, 0)
DARKGREY = (45, 45, 45)
LIGHTGREY = (220, 220, 220)
WHITE = (255, 255, 255)

ROADWIDTH = 600
roadMaxX = (DISPLAYWIDTH + ROADWIDTH) * 0.5
roadMinX = (DISPLAYWIDTH - ROADWIDTH) * 0.5
edgeWidth = 9
stripHeight = 100
stripNumber = DISPLAYHEIGHT / stripHeight

clock = pygame.time.Clock()
FPS = 60

crashed = False

#Getting Sprites ready

carImage = pygame.image.load("res/car.png")
(carWidth, carHeight) = (150, 150)
sideImage = pygame.image.load("res/desert_tex.jpg")
(sideWidth, sideHeight) = (100, 100)
y_offset = 20

#Adding Sprites

def car(x,y):
    displaySurface.blit(carImage, (x,y))

def drawRoad(offset):
    pygame.draw.rect(displaySurface, DARKGREY, (roadMinX, 0, ROADWIDTH, DISPLAYHEIGHT))
    pygame.draw.line(displaySurface, LIGHTGREY, (roadMinX + 15, 0), (roadMinX + 15, DISPLAYHEIGHT), edgeWidth)
    pygame.draw.line(displaySurface, LIGHTGREY, (roadMaxX - 15, 0), (roadMaxX - 15, DISPLAYHEIGHT), edgeWidth)
    for i in range (-1, stripNumber):
        pygame.draw.line(displaySurface, WHITE, (roadMinX + ROADWIDTH/3, i*stripHeight + offset), (roadMinX + ROADWIDTH/3, (i + 0.5)*stripHeight + offset), 7)
        pygame.draw.line(displaySurface, WHITE, (roadMaxX - ROADWIDTH/3, i*stripHeight + offset), (roadMaxX - ROADWIDTH/3, (i + 0.5)*stripHeight + offset), 7)

def drawSide():
    (leftWidth, rightWidth) = (roadMinX, DISPLAYWIDTH - roadMaxX)
    
    #Adding texture images on left
    for i in range(0, int(leftWidth/sideWidth)):
        for j in range(0, int(DISPLAYHEIGHT/sideHeight)):
            displaySurface.blit(sideImage, (i*sideWidth, j*sideHeight))
    
    #Adding texture images on right
    for i in range(0, int(rightWidth/sideWidth)):
        for j in range(0, int(DISPLAYHEIGHT/sideHeight)):
            displaySurface.blit(sideImage, (roadMaxX + i*sideWidth, j*sideHeight))

x = (DISPLAYWIDTH - carWidth) * 0.5
y = DISPLAYHEIGHT - carHeight - y_offset

#Initialising velocity Components0

maxSteerVelocityX = 100
accelY = 200
topSpeedY = 750
prevSpeedY = 0
currentSpeedY = 0

x_change = 0
offset = 0

clock.tick(FPS)

#Game Loop

while not crashed:
    
    clock.tick(FPS)
    
    x_change = 0
    duration = clock.get_time() * 0.001
    
    
    steerVelocityX = currentSpeedY*maxSteerVelocityX/topSpeedY
    dist = duration * steerVelocityX
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_LEFT:
                #x_change = -dist
                #print x_change
            #elif event.key == pygame.K_RIGHT:
                #x_change = dist
        #elif event.type == pygame.KEYUP:
            #if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #x_change = 0
    getPressed = pygame.key.get_pressed()

    if getPressed[pygame.K_LEFT]:
        x_change -= dist
    if getPressed[pygame.K_RIGHT]:
        x_change += dist
    
    if getPressed[pygame.K_SPACE]:
        currentSpeedY = max(prevSpeedY - accelY*duration, 0)
        prevSpeedY = currentSpeedY
    elif currentSpeedY != topSpeedY:
        currentSpeedY = min(prevSpeedY + accelY*duration, topSpeedY)
        prevSpeedY = currentSpeedY
        
    
    x += x_change
    
    offset = (offset + duration*currentSpeedY) % stripHeight 
    
    displaySurface.fill(WHITE)
    x = min(max(x, roadMinX), roadMaxX - carWidth)
    drawRoad(offset)
    drawSide()
    car(x,y)
    pygame.display.update()
    

pygame.quit()
quit()
