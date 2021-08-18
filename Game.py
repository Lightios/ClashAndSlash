import pygame as pg
import sys
from Player import *
from Consts import *
from Enemies import *
from Planet import *


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.is_running = True
        self.clock = pg.time.Clock()

        # creating layers and main group
        self.layers = [pg.sprite.Group() for _ in range(3)]
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()

        # creating the starting objects
        self.player = Player(self)
        self.planet = Planet(self)

        # creating variables for game
        self.enemies_spawner = 0

        # loading images
        self.background_image = pg.image.load(r'Images\Background2.png').convert()

    def mainloop(self):
        """Main loop for the game"""
        while self.is_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()

            self.update()
            self.draw()
            self.clock.tick(FPS)

    @staticmethod
    def quit():
        """Closes the whole game"""
        pg.quit()
        sys.exit()

    def update(self):
        """Updates every sprite in the game, spawns enemies"""
        for sprite in self.all_sprites:
            sprite.update()

        if self.enemies_spawner == 0:
            self.spawn_enemy()
            self.enemies_spawner = 50
        else:
            self.enemies_spawner -= 1

    def draw(self):
        """Draws every sprite in the game on the screen"""
        self.screen.blit(self.background_image, (0, 0))
        for layer in self.layers:
            for sprite in layer:
                self.screen.blit(sprite.image, sprite.rect)
        # pg.draw.line(self.screen, (255, 255, 0), (self.player.rect.centerx, self.player.rect.centery), (WIDTH/2, HEIGHT/2))
        # pg.draw.rect(self.screen, (255, 0, 0), self.player.rect)
        pg.display.update()

    def spawn_enemy(self):
        """Creates enemy"""
        enemy = EnemyLevel1(self)

