import pygame as pg
import random
import math
from Consts import *
from pygame.image import load


class EnemyAbstract(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.layers[2], game.enemies
        pg.sprite.Sprite.__init__(self, self.groups)
        self.rect = self.image.get_rect()
        self.x, self.y = 0.0, 0.0
        self.set_starting_position()
        self.movement_vector = self.get_movement_vector()
        self.hp_max = 1
        self.hp = int(self.hp_max)
        self.image_animation_counter = 0

    def set_starting_position(self):
        """Sets enemy's position at random point at random edge of the screen"""
        side = random.choice(("left/right", "top/bottom"))
        if side == "left/right":
            self.x = random.choice((0, 1)) * WIDTH
            self.y = random.randint(0, HEIGHT)
        else:
            self.x = random.randint(0, WIDTH)
            self.y = random.choice((0, 1)) * HEIGHT
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x -= self.movement_vector.x
        self.y -= self.movement_vector.y
        self.rect.x, self.rect.y = self.x, self.y

        self.image_animation_counter += 1
        if self.image_animation_counter == 10:
            self.image_animation_counter = 0
        self.image = self.images[self.image_animation_counter // 5]

        if self.hp < 1:
            self.kill()

    def get_movement_vector(self):
        """
        Calculates individual movement vector for each enemy
        :returns: pg.math.Vector2
        """
        rel_x, rel_y = self.rect.x - self.rect.width - WIDTH / 2, self.rect.y - self.rect.height - HEIGHT / 2
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        return pg.math.Vector2(2, 0).rotate(-angle)


class EnemyLevel1(EnemyAbstract):
    def __init__(self, game):
        self.images = [load(r'Images/EnemyBig/enemy-big.png'), load(r'Images/EnemyBig/enemy-big2.png')]
        self.image = self.images[0]
        self.image_animation_counter = 0
        super().__init__(game)
