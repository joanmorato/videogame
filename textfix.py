import pygame
import conf

class TextFix(pygame.sprite.Sprite):

    def __init__(self, txt, pos):
        super().__init__()
        font =  pygame.font.Font(pygame.font.get_default_font(),
                                 conf.font_info_size)
        self.image = font.render(txt, True, conf.color_text_info)
        self.rect = self.image.get_rect()
        self.rect.center = pos
