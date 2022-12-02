
import pygame

class ProgressBar(pygame.sprite.Sprite):

    def __init__(self, posc, amplada, alçada, color, color_fons):
        super().__init__()
        self.image = pygame.Surface((amplada, alçada))
        self.rect = self.image.get_rect()
        self.rect.center = posc
        self.image.fill(color)
        self.percent = 100.0
        self.color1 = color
        self.color2 = color_fons 

    def update(self):
        self.image.fill(self.color2)
        ple = (self.percent/100.0) * self.rect.width
        r = pygame.Rect((0,0), (ple, self.rect.height))
        self.image.fill(self.color1, r)
        

