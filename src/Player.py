import pygame as pg


class Player(pg.sprite.Sprite):

    speed = 10
    images = []
    screen = 0

    def __init__(self, screen_rect):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen_rect
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=self.screen.midbottom)

    def move(self, direction):
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(self.screen)
