import pygame

class Animacio_mask(pygame.sprite.Sprite):

    

    def __init__(self, matriu_imatges_de_mask, pos):
        super().__init__()
        # Defineix l'estat inicial
        
        
        
        self.llista_im = matriu_imatges_de_mask
        
        
       
        self.image = self.llista_im[0][0]
        self.image_mask = self.llista_im[0][0]
        self.rect = self.image.get_rect().move(pos)
        
        self.mask = pygame.mask.from_surface(self.image_mask)
        
	

    def update(self):
        
        a=3 
        #self.rect.center = (self.rect.center[0]+self.vH,self.rect.center[1]-self.vV)
        #fila = self.estat
        #columna = self.count//5  #  columna = self.count // 10
        #self.image = self.llista_im[fila][columna]
	
	    


    
