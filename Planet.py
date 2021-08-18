import pygame as pg
from Consts import *
from Functions import *
import math


class Planet(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.layers[1]
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load(r'Images/Planet.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2