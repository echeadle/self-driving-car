import pygame
pygame.init()

# Create a display surface
canvas = pygame.display.set_mode((200, pygame.display.Info().current_h))

# Create a car object
car = Car(100, 100, 30, 50)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the car and draw it on the canvas
    car.update()
    car.draw(canvas)

    # Update the display
    pygame.display.flip()

pygame.quit()