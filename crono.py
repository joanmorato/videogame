import pygame
import conf
import datetime

class Cronòmetre(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.font = pygame.font.Font(conf.font_crono_filename, conf.font_crono_size)
        self.center = pos
        self.seconds = 0 # segons que han passat
        self.tini = 122596
        ## self.t=122596
        self._crea_imatge()
        
    def update(self):
        self._crea_imatge()

    def _crea_imatge(self):
        t =  self.tini - pygame.time.get_ticks()
        self.t=t
        dt = datetime.timedelta(milliseconds=t)
        txt = str(dt)[3:-7] # text que volem escriure
        self.image = self.font.render(txt, True, conf.color_text_crono,
                                      conf.color_fons_crono)
        self.rect = self.image.get_rect()
        self.rect.center = self.center

    def reset(self):
        self.tini= 120500+pygame.time.get_ticks()
        self.seconds = 0
