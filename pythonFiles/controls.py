import pygame

class Car:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.speed = 0
        self.acceleration = 0.2
        self.max_speed = 3
        self.friction = 0.5

        self.controls = Controls()

    def update(self):
        if self.controls.forward:
            self.speed += self.acceleration
        if self.controls.reverse:
            self.speed -= self.acceleration
        if self.speed > self.max_speed:
            self.speed = self.max_speed

        self.y -= self.speed

    def draw(self, canvas):
        pygame.draw.rect(
            canvas,
            (255, 255, 255),  # color
            pygame.Rect(
                self.x - self.width / 2,
                self.y - self.height / 2,
                self.width,
                self.height
            )
        )