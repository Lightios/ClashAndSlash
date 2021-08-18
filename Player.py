import pygame as pg
from Consts import *
from Functions import *
import math
from Bullet import *


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.layers[1]
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.original_image = pg.image.load(r'Images\Player.png')
        self.original_rect = self.original_image.get_rect()
        self.rect = self.original_image.get_rect()
        self.angle = 0

        self.shoot_coldown = 0
        self.shoot_coldown_max = 12

    def update(self):
        self.update_position()
        self.image, self.rect = rot_image_around_center(self.original_image, self.angle - 90, self.rect.x, self.rect.y)

        if pg.mouse.get_pressed()[0] and self.shoot_coldown < 1:
            Bullet(self.game)
            self.shoot_coldown = int(self.shoot_coldown_max)
        elif self.shoot_coldown > 0:
            self.shoot_coldown -= 1

    def update_position(self):
        """Updates player's poistion basing on mouse's position"""
        mouse_x, mouse_y = pg.mouse.get_pos()
        rel_x, rel_y = mouse_x - WIDTH / 2, mouse_y - HEIGHT / 2
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.rect.x, self.rect.y = pg.math.Vector2(self.game.planet.image.get_width()/2 + self.original_image.get_width()/2, 0).rotate(-self.angle) + pg.math.Vector2(WIDTH / 2,
                                                                                                 HEIGHT / 2)
