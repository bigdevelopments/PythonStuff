import pygame

# initialise pygame
pygame.init()

from Scenes.GetReadyScene import GetReadyScene

# create our game object
scene = GetReadyScene()

# keep track of frame count in current scene
frame = 0

# create the main window
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption(scene.get_name())

# we need this to regulate the game speed
clock = pygame.time.Clock()

# assume running until we're told otherwise
running = True

while running:
    
    # check for the exit command
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
              running = False

    # clear the screen before we do anything else
    screen.fill((0,0,0))

    # get the game class to do a tick
    next_scene = scene.tick(frame, screen, events)

    frame+=1

    # swap buffers
    pygame.display.flip()

    if scene != next_scene:
        scene = next_scene
        scene.init()
        pygame.display.set_caption(scene.get_name())
        frame = 0
        
    # wait for next tick to be scheduled
    clock.tick(60)

# thank you, that was fun!
pygame.quit()

    