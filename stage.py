import pygame
 
class Stage(pygame.sprite.Sprite):
 
    def __init__(self, pos, img):
        super().__init__() # constructor de classe Sprite
        #self.image = pygame.image.load(img).convert_alpha()
        self.image=img
        self.rect = self.image.get_rect().move(pos)  # rectangle de la imatge
        
 
    #def update(self): # Actualitza posició i la velocitat de la pilota 
        
