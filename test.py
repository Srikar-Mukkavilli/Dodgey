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

ROADWIDTH = 500
roadMaxX = (DISPLAYWIDTH + ROADWIDTH) * 0.5
roadMinX = (DISPLAYWIDTH - ROADWIDTH) * 0.5
edgeWidth = 9

clock = pygame.time.Clock()
FPS = 60

crashed = False
carImage = pygame.image.load("res/car.png")
(carWidth, carHeight) = (150, 150)
y_offset = 20


def car(x,y):
    displaySurface.blit(carImage, (x,y))

def drawRoad():
    pygame.draw.rect(displaySurface, DARKGREY, (roadMinX, 0, ROADWIDTH, DISPLAYHEIGHT))
    pygame.draw.line(displaySurface, LIGHTGREY, (roadMinX, 0), (roadMinX, DISPLAYHEIGHT), edgeWidth)
    pygame.draw.line(displaySurface, LIGHTGREY, (roadMaxX, 0), (roadMaxX, DISPLAYHEIGHT), edgeWidth)

x = (DISPLAYWIDTH - carWidth) * 0.5
y = DISPLAYHEIGHT - carHeight - y_offset

carVelocity = 250

x_change = 0

clock.tick(FPS)

while not crashed:
    
    clock.tick(FPS)
    
    x_change = 0
    duration = clock.get_time() * 0.001
    dist = duration * carVelocity
    
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

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        x_change -= dist
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        x_change += dist
    
    x += x_change
            
    displaySurface.fill(WHITE)
    x = min(max(x, roadMinX), roadMaxX - carWidth)
    drawRoad()
    car(x,y)
    pygame.display.update()
    

pygame.quit()
quit()
