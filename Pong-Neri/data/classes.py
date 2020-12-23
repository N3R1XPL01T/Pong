# @author: Saul Neri

from random import randint
from data.constants import ANCHO
import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hitbox = pygame.Rect(self.pos_x, self.pos_y, 80, 4)
        self.desplaz_x_movement = 35
        self.vidas = 5
        self.puntos = 0

    def MoverseDerecha(self):
        self.hitbox.right += self.desplaz_x_movement
        pygame.display.update()
    def MoverseIzquierda(self):
        self.hitbox.left -= self.desplaz_x_movement
        pygame.display.update()

    def Draw(self, frame):
        pygame.draw.rect(frame, (255, 255, 255), self.hitbox)

