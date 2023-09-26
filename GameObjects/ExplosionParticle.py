import math
import random
import pygame
from GameObjects.GameObject import GameObject


class ExplosionParticle(GameObject):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = 0
        self.life_delta =  4+ random.random()*7
        self.angle = random.random() * 2* math.pi
        self.speed = 1 + random.random() * 8

    def tick(self):

        self.dx = math.sin(self.angle) * self.speed
        self.dy = math.cos(self.angle) * self.speed

        self.x += self.dx
        self.y += self.dy
        self.speed *= 0.99
        self.life+=self.life_delta


    def draw(self, screen):

        red = 255-self.life/4
        if red < 0:
            red =0

        green = 255-self.life/3
        if green < 0:
            green =0

        blue = 255-self.life
        if blue < 0:
            blue = 0

        size = 6 - self.life/85
        if size < 0:
            size = 0


        # Drawing Rectangle
        pygame.draw.rect(screen, (red, green, blue), pygame.Rect(self.x, self.y, size, size))