import pygame
import conf
class Animacio(pygame.sprite.Sprite):

    # Inicialitza els estats. Són nombres enters.
    DPANTALLA1, ATACD, AMUNTD, QUIETD, Ddefensa, Dhurt, DRETA, IPANTALLA1, ATACI, AMUNTI, QUIETI, Edefensa, Ehurt, ESQUERRA= range(14)
    # Inicialitza les transicions
    VES_AVALL, VES_ESQUERRA, VES_DRETA, VES_AMUNT, DEFENSA, FTILT, UTILT, DTILT, FATILT, HURT, ATAC = range(11) #atac==UPS
    def __init__(self, matriu_imatges, pos,barravida,damage,shield,life):
        super().__init__()
        # Defineix l'estat inicial
        self.estat = self.QUIETD
        self.llista_im = matriu_imatges
        self.count = 0
        self.nframes = len(self.llista_im[0])
        self.image = self.llista_im[self.estat][0]
        self.mask = pygame.mask.from_surface(self.image) 
        self.vH= 0
        self.vV= 0
        self.air=False
        self.salts=2
        self.mask = pygame.mask.from_surface(self.image)
        self.direccio = 'nul' # direcció
        self.contador=life
        self.rect = self.image.get_rect().move(pos)
        self.mirant=1
        self.defensa=shield
        self.shield=shield
        self.damage=damage
        self.CENTRO =[self.rect.center[0],self.rect.center[1]]
        self.delaybetweenmoves=0
        self.barravida=barravida
        self.hpmax=life
        self.inmune=False
        self.inmunity=0
        self.hitted=0
        

    def update(self):
        if self.rect.center[1]==300:
            self.air=True
        if self.air:
            self.vV=self.vV-0.3
            if self.direccio == 'nul':
                if self.vH<-0.3:
                    self.vH=self.vH+0.3
                if self.vH>0.3:
                    self.vH=self.vH-0.3
        if self.vV<0 and self.rect.bottom>440 and self.rect.bottom<460:
                self.CENTRO = [self.rect.center[0],self.rect.center[1]]
                self.air=False
                self.canvia_estat(self.VES_AVALL)
        if self.rect.left<-270:
            if self.vH<0:
                self.vH=0
        if self.rect.right>950:
            if self.vH>0:
                self.vH=0
            

        self.count = self.count + 1
        if self.count == self.nframes * 8:
            if self.estat==self.Dhurt:
                self.estat==self.QUIETD
            if self.estat==self.Ehurt:
                self.estat==self.QUIETI                
            self.count = 0
        fila = self.estat
        columna = self.count // 8
        self.image = self.llista_im[fila][columna]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(self.rect.center[0],self.rect.center[1])
        self.rect.center = (self.CENTRO[0],self.CENTRO[1])
        self.rect.center = (self.rect.center[0]+self.vH,self.rect.center[1]-self.vV)
        self.CENTRO = [self.rect.center[0],self.rect.center[1]]

        if self.delaybetweenmoves != 0:
                self.delaybetweenmoves=self.delaybetweenmoves-1
        if self.inmunity != 0:
                self.inmunity=self.inmunity-1
        elif self.estat==self.Dhurt or self.estat==self.Ehurt:
            if self.mirant==1:
                self.estat=self.QUIETD
            else:
                self.estat=self.QUIETI
            self.inmune=False
        elif self.inmunity==0:
            self.inmune=False

    def canvia_estat(self, transicio=None):
        """Actualitza l'estat en funció de l'estat actual i de la transició

        """
        # En aquest cas, l'estat final és independent de l'estat
        # inicial: només depèn de la transició
        estat_anterior = self.estat
        if transicio == self.DEFENSA:
            pygame.mixer.init()
            sodefensa= pygame.mixer.Sound(conf.sodefensa)
            sodefensa.set_volume(0.1)
            sodefensa.play()
            if self.mirant==1:
                self.estat = self.Ddefensa
                self.nframes = len(self.llista_im[self.Ddefensa])
            if self.mirant==0:
                self.estat = self.Edefensa
                self.nframes = len(self.llista_im[self.Edefensa])
        elif transicio == self.HURT:
            if self.estat == self.Ddefensa or self.estat == self.Edefensa:
                if self.defensa>0:
                    pygame.mixer.init()
                    sodefensa= pygame.mixer.Sound(conf.sodefensa)
                    sodefensa.set_volume(0.1)
                    sodefensa.play()
                    self.defensa=self.defensa-self.damage
                elif self.mirant==1:
                    self.estat=self.QUIETD
                    self.delaybetweenmoves=100
                    self.defensa=self.shield
                elif self.mirant==0:
                    self.estat=self.QUIETI
                    self.delaybetweenmoves=100
                    self.defensa=self.shield
            else:
                if self.inmune==False and self.inmunity==0:
                    self.contador=self.contador-self.damage+1
                    self.barravida.percent=max(0,self.barravida.percent-100*(self.damage/self.hpmax)+1)
                    self.inmune=True
                    self.inmunity=40
                    self.hitted=1
                    pygame.mixer.init()
                    sodamage= pygame.mixer.Sound(conf.sodamage)
                    sodamage.set_volume(0.25)
                    sodamage.play()
                    if self.mirant==1:
                        self.estat=self.Dhurt
                        self.nframes = len(self.llista_im[self.Dhurt])
                        
                    else:
                        self.estat=self.Ehurt
                        self.nframes = len(self.llista_im[self.Ehurt])

        elif transicio == self.VES_AMUNT and self.mirant==0 :
            pygame.mixer.init()
            sosalt= pygame.mixer.Sound(conf.sosalt)
            sosalt.set_volume(0.2)
            sosalt.play()
            self.estat = self.QUIETI
            self.nframes = len(self.llista_im[self.QUIETI])
            self.inmune=True
            self.inmunity=40
            if self.air :
                self.vV=5
                self.salts= self.salts-1
                self.estat = self.AMUNTI
                self.nframes = len(self.llista_im[self.AMUNTI])
            elif not self.air:
                self.vV=10
                self.salts=2
                self.air=True
                
        elif transicio == self.VES_AMUNT and self.mirant==1 :
            pygame.mixer.init()
            sosalt= pygame.mixer.Sound(conf.sosalt)
            sosalt.set_volume(0.2)
            sosalt.play()
            self.estat = self.QUIETD
            self.nframes = len(self.llista_im[self.QUIETD])
            self.inmune=True
            self.inmunity=40
            if self.air :
                self.vV=5
                self.salts= self.salts-1
                self.estat = self.AMUNTD
                self.nframes = len(self.llista_im[self.AMUNTD])
            elif not self.air:
                self.vV=10
                self.salts=2
                self.air=True
        
        elif transicio == self.VES_AVALL and self.mirant==1:
            self.estat = self.QUIETD
            self.vH=0
            self.vV=0
            self.nframes = len(self.llista_im[self.QUIETD])

        elif transicio == self.VES_AVALL and self.mirant==0:
            self.estat = self.QUIETI
            self.vH=0
            self.vV=0
            self.nframes = len(self.llista_im[self.QUIETI])
        elif transicio == self.ATAC and self.mirant==0:
            self.estat=self. ATACI
            self.vH=0
            self.nframes= len(self.llista_im[self.ATACI])

        elif transicio == self.ATAC and self.mirant==1:
            self.estat=self. ATACD
            self.vH=0
            self.nframes= len(self.llista_im[self.ATACD])    
            
        elif transicio == self.VES_DRETA:
            self.estat = self.DRETA
            self.mirant= 1
            self.vH=7
            self.vV=0
            self.nframes = len(self.llista_im[2])
            
        elif transicio == self.VES_ESQUERRA:
            self.estat = self.ESQUERRA
            self.mirant= 0
            self.vH=-7
            self.vV=0
            self.nframes = len(self.llista_im[1])
            
        else:
            raise ValueError('Transició {} desconeguda'.format(transicio))
        if self.estat != estat_anterior:
            self.count = 0
