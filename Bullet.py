import pygame as pg
from Consts import *
from Functions import *
import math
import random


class Bullet(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.layers[1]
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((10, 10))
        self.image.fill((200, 200, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = game.player.rect.centerx
        self.rect.centery = game.player.rect.centery
        self.angle = game.player.angle + random.randint(-7, 7)

    def update(self):
        self.rect.x += pg.math.Vector2(10, 0).rotate(-self.angle).x
        self.rect.y += pg.math.Vector2(10, 0).rotate(-self.angle).y

        hit = pg.sprite.spritecollide(self, self.game.enemies, False)
        if len(hit) > 0:
            self.kill()

        for enemy in hit:
            enemy.hp -= 1
