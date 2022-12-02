
import pygame
from pygame.locals import *
from pgu import engine
import conf
import fighter1
import sprite_sheets
from pbar import ProgressBar
import stage
import sp_mask
from crono import Cronòmetre
from textfix import TextFix


class Joc(engine.Game):
    
    def __init__(self):
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode(conf.mides_pantalla, SWSURFACE) 
        self.crono = pygame.time.Clock()
        self._init_state_machine()
        self.character1=1
        self.character2=2

    def _init_state_machine(self):
        self.jugant = Jugant(self)
        self.menu = Menu(self)
        self.options = Options(self)
        self.choose_fighter1 = Choose_Fighter1(self)
        self.choose_fighter2 = Choose_Fighter2(self)
        self.quit_state = engine.Quit(self)
        self.winp1=WinP1(self)
        self.winp2=WinP2(self)

    def init_game(self):
        del self.jugant
        self.jugant = Jugant(self)
        del self.menu
        self.menu = Menu(self)
        del self.opcions
        self.options = Options(self)
        del self.winp1
        self.winp1 = WinP1(self)
        del self.winp2
        self.winp2 = WinP2(self)
    def run(self): 
        super().run(self.menu, self.screen)

    def tick(self):
        self.crono.tick(conf.fps)


    def change_state(self, transition=None):
        #OBRIM EL MENU:
        #   -OPTIONS
        #   -CHOOSE YOUR FIGHTER SCREEN
        #   -EXIT
        #   -GAME
        if self.state is self.menu:
            if transition == 'OPTIONS':
                new_state = self.options
            elif transition == 'CHOOSE_FIGHTER':
                new_state = self.choose_fighter1
            elif transition == 'EXIT':
                new_state = self.quit_state
                
        elif self.state is self.options:
            if transition == 'MENU':
                new_state = self.menu
                
        elif self.state is self.choose_fighter1:
            if transition == 'MENU':
                new_state = self.menu
            elif transition == 'CHOOSE_FIGHTER_2':
                new_state = self.choose_fighter2
                new_state.init()

        elif self.state is self.choose_fighter2:
            if transition == 'CHOOSE_FIGHTER':
                new_state = self.choose_fighter1
                new_state.init()
            elif transition == 'GAME':
                pygame.mixer.music.set_volume(0.25)
                new_state = self.jugant
                new_state.init()
        elif self.state is self.jugant:
            if transition == 'WinP1':
                new_state = self.winp1
            elif transition =='WinP2':
                new_state = self.winp2
        elif self.state is self.winp1:
            if transition == 'MENU':
                new_state = self.menu
                new_state.init()
            elif transition == 'GAME':
                new_state = self.jugant
                new_state.init()
        elif self.state is self.winp2:
            if transition == 'MENU':
                new_state = self.menu
                new_state.init()
            elif transition == 'GAME':
                new_state = self.jugant
                new_state.init()
                   
        return new_state


class Jugant(engine.State):
    # The init method should load data, etc.  The __init__ method
    # should do nothing but record the parameters.  If the init method
    # returns a value, it becomes the new state.
    def init(self):
        pygame.mixer.init()
        self.cronoset=0
        self.grup = pygame.sprite.Group() # grup de Sprites
        self.grup2 = pygame.sprite.Group() # grup de Sprites
        self.grup3 = pygame.sprite.Group()
        self.grupb1 = pygame.sprite.Group()
        self.grupb2 = pygame.sprite.Group()
        self.gcrono = pygame.sprite.Group()
        self.gimage= pygame.sprite.Group()
        self.gm1=pygame.sprite.Group()
        self.gm2=pygame.sprite.Group()
        pb1 = ProgressBar((150,50),150, 30,(255, 0, 0), (200, 200, 200))#
        pb2= ProgressBar((530, 50),150, 30,(255, 0, 0), (200, 200, 200))#
        self.pbc1=pb1
        self.pbc2=pb2
        if self.game.character1 == 1:
            im = pygame.image.load(conf.sprite_sheet_personatge1)
            im_mask=pygame.image.load(conf.sprite_sheet_personatge1)
        elif self.game.character1 == 2:
            im = pygame.image.load(conf.sprite_sheet_personatge2)
            im_mask=pygame.image.load(conf.sprite_sheet_personatge2)
## en cas de afegir més personatges
##        elif self.game.character1 == 3:
##            im = pygame.image.load(conf.sprite_sheet_personatge3)
##            im_mask=pygame.image.load(conf.sprite_sheet_personatge3)
##        elif self.game.character1 == 4:
##            im = pygame.image.load(conf.sprite_sheet_personatge4)
##            im_mask=pygame.image.load(conf.sprite_sheet_personatge4)
        
        if self.game.character2 == 1:
            if self.game.character1 == self.game.character2:
                im2 = pygame.image.load(conf.sprite_sheet_personatge5)
                im_mask2=pygame.image.load(conf.sprite_sheet_personatge5)
                d1=50
                s1=250
                hp1=200
                d2=d1
                s2=d2
                hp2=hp1
            else:
                im2 = pygame.image.load(conf.sprite_sheet_personatge1)
                im_mask2=pygame.image.load(conf.sprite_sheet_personatge1)
                d1=50
                s1=250
                hp1=200
                d2=20
                s2=1000
                hp2=100
        elif self.game.character2 == 2:
            if self.game.character1 == self.game.character2:
                im2 = pygame.image.load(conf.sprite_sheet_personatge6)
                im_mask2=pygame.image.load(conf.sprite_sheet_personatge6)
                d1=20
                s1=1000
                hp1=100
                d2=d1
                s2=d2
                hp2=hp1
            else:
                im2 = pygame.image.load(conf.sprite_sheet_personatge2)
                im_mask2=pygame.image.load(conf.sprite_sheet_personatge2)
                d1=20
                s1=1000
                hp1=100
                d2=50
                s2=250
                hp2=200

## en cas de afegir més personatges
##        elif self.game.character2 == 3:
##            if self.game.character1 == self.game.character2:
##                im2 = pygame.image.load(conf.sprite_sheet_personatge7)
##                im_mask2=pygame.image.load(conf.sprite_sheet_personatge7)
##            else:
##                im2 = pygame.image.load(conf.sprite_sheet_personatge3)
##                im_mask2=pygame.image.load(conf.sprite_sheet_personatge3)
##        elif self.game.character2 == 4:
##            if self.game.character1 == self.game.character2:
##                im2 = pygame.image.load(conf.sprite_sheet_personatge8)
##                im_mask2=pygame.image.load(conf.sprite_sheet_personatge8)
##            else:
##                im2 = pygame.image.load(conf.sprite_sheet_personatge4)
##                im_mask2=pygame.image.load(conf.sprite_sheet_personatge4)
        mat_im = sprite_sheets.crea_matriu_imatges(im, *conf.mides_sprite_sheet_personatge)
        mat_mask=sprite_sheets.crea_matriu_imatges(im_mask, *conf.mides_sprite_sheet_personatge)
        imgg=pygame.image.load(conf.staged)
        self.fons=stage.Stage(conf.Pstage,imgg)
        platf=pygame.image.load(conf.platf)
        self.platf=stage.Stage(conf.plat,platf)
        self.grup2.add(self.fons)
        self.grup2.add(self.platf)
        self.heroi = fighter1.Animacio( mat_im, conf.posicio_personatge,pb1,d1,s1,hp1)
        self.grup.add(self.heroi)
        mat_im2 = sprite_sheets.crea_matriu_imatges(im2, *conf.mides_sprite_sheet_personatge2)
        mat_mask2=sprite_sheets.crea_matriu_imatges(im_mask2, *conf.mides_sprite_sheet_personatge)
        self.heroi2 = fighter1.Animacio( mat_im2,conf.posicio_personatge2,pb2,d2,s2,hp2)
        self.heroi2.mirant=0
        self.h1_mask = sp_mask.Animacio_mask(mat_mask, conf.posicio_personatge)
        self.h2_mask = sp_mask.Animacio_mask(mat_mask2, conf.posicio_personatge)
        self.grup3.add(self.heroi2)
        self.grupb1.add(pb1)
        self.grupb2.add(pb2)
        self.gm1.add(self.h1_mask)
        self.gm2.add(self.h2_mask)
        
        self.keys=pygame.key.get_pressed()
        
#
        # Sprite amb el cronòmetre
        self.cronosprite = Cronòmetre((conf.amplePant/2, (conf.altPant-148)/7))

        # Imatges fixes amb un text        
        # Grup de sprites
        
        self.gcrono.add(self.cronosprite)
        

#

        ##controles antes de pelea:
        
        image = pygame.image.load(conf.controls)
        self.tuto=stage.Stage(conf.Pstage,image)
        self.gimage.add(self.tuto)
        
        
    # The paint method is called once.  If you call repaint(), it
    # will be called again.
    def paint(self,screen):
        self.update(screen)
        
            
 

    # Every time an event occurs, event is called.  If the event
    # method returns a value, it will become the new state.
    def event(self,event): 
        if event.type == KEYDOWN:
            if self.cronoset ==0:
                self.cronoset=1
                self.cronosprite.reset()
            if event.key == pygame.K_KP0:
                self.heroi2.canvia_estat(self.heroi2.ATAC)
            elif event.key ==  pygame.K_UP:
                if self.heroi2.salts>0:
                    self.heroi2.canvia_estat(self.heroi2.VES_AMUNT)
                elif self.heroi2.air==False:
                    self.heroi2.salts=2
            elif event.key == pygame.K_DOWN:
                self.heroi2.canvia_estat(self.heroi2.DEFENSA)
                self.heroi2.vH=0
            elif event.key == pygame.K_RIGHT:
                self.heroi2.canvia_estat(self.heroi2.VES_DRETA)
                self.heroi2.vH=4
            elif event.key == pygame.K_LEFT:
                self.heroi2.canvia_estat(self.heroi2.VES_ESQUERRA)
                self.heroi2.vH=-4

            if event.key == pygame.K_SPACE:
                self.heroi.canvia_estat(self.heroi.ATAC)
            elif event.key ==  pygame.K_w:
                if self.heroi.salts>0:
                    self.heroi.canvia_estat(self.heroi.VES_AMUNT)
                elif self.heroi.air==False:
                    self.heroi.salts=2
            elif event.key == pygame.K_s:
                self.heroi.canvia_estat(self.heroi.DEFENSA)
            elif event.key == pygame.K_d:
                self.heroi.canvia_estat(self.heroi.VES_DRETA)
                self.heroi.vH=4
            elif event.key == pygame.K_a:
                self.heroi.canvia_estat(self.heroi.VES_ESQUERRA)
                self.heroi.vH=-4
        if event.type == KEYUP:
            if event.key == pygame.K_SPACE or event.key == pygame.K_a or event.key == pygame.K_d:
                self.heroi.canvia_estat(self.heroi.VES_AVALL)
                self.heroi.vH=0
            if event.key == pygame.K_KP0 or event.key == pygame.K_RIGHT or event.key==pygame.K_LEFT:
                self.heroi2.canvia_estat(self.heroi2.VES_AVALL)


        

            
    # Loop is called once a frame.  It should contain all the logic.
    # If the loop method returns a value it will become the new state.
    def loop(self):          
        self.h2_mask.rect.top =self.heroi2.rect.top
        self.h2_mask.rect.left = self.heroi2.rect.left
        self.gm1.update()
        self.gm2.update()
        self.grup2.update()
        self.grup.update()
        self.grup3.update()
        self.grupb1.update()
        self.grupb2.update()
        self.gcrono.update()            
        if self.heroi.contador<=0:

            return self.game.change_state('WinP2')
        elif self.heroi2.contador<=0:

            return self.game.change_state('WinP1')
        elif self.cronosprite.t<=0 and self.cronoset==1:
            if self.heroi2.contador>self.heroi.contador:
                return self.game.change_state('WinP2')
            else:
                return self.game.change_state('WinP1') 
        
        hitPJ1 = pygame.sprite.collide_mask(self.heroi, self.heroi2)
        hitPJ2 = pygame.sprite.collide_mask(self.heroi2, self.heroi)

        if hitPJ2 and self.heroi.estat==self.heroi.ATACD:
            
            #if self.heroi2.estat!=self.heroi2.Dhurt and self.heroi2.estat!=self.heroi2.Ehurt:
            
            self.heroi2.canvia_estat(self.heroi2.HURT)
            
        elif hitPJ2 and self.heroi.estat==self.heroi.ATACD:
            
            #if self.heroi2.estat!=self.heroi2.Dhurt and self.heroi2.estat!=self.heroi2.Ehurt:
            
            self.heroi2.canvia_estat(self.heroi2.HURT)
        
                
        elif hitPJ1 and self.heroi2.estat==self.heroi2.ATACD:
            
            #if self.heroi.estat!=self.heroi.Dhurt and self.heroi.estat!=self.heroi.Ehurt:
            
            self.heroi.canvia_estat(self.heroi.HURT)

        elif hitPJ1 and self.heroi2.estat==self.heroi2.ATACI:
            
            #if self.heroi.estat!=self.heroi.Dhurt and self.heroi.estat!=self.heroi.Ehurt:
            
            self.heroi.canvia_estat(self.heroi.HURT)

    # Update is called once a frame.  It should update the display.
    def update(self,screen):
        b=0
        b1=b+1
        zero=0
        noche=500
        if b1<=189 and zero==0:
            b=b+1
        elif zero==1 and b==0:
            zero=0
            noche=500
            b1=0
        elif noche!=0:
            b=b
        else:
            b=b-1
        screen.fill((0,b,244))    
        
            
        self.grup2.draw(screen)
        self.grup.draw(screen)
        self.grup3.draw(screen)
        self.grupb1.draw(screen)
        self.grupb2.draw(screen)
        self.gcrono.draw(screen)
        if self.cronoset==0:
            self.gimage.draw(screen)
        pygame.display.flip()


''' [][][][][][][][][][][]  MAIN  MENU  [][][][][][][][][][][] '''
class Menu(engine.State):
#       ESC - to show options
#       B - to exit game
#       V - to show the choose your fighter screen
    def init(self):
        #CARREGUEM LA IMATGE DEL MENU
        self.image = pygame.image.load("main_menu.png")
        pygame.mixer.init()
        pygame.mixer.music.load(conf.musicamenu)
        pygame.mixer.music.play()
        
    def paint(self, s):
        s.fill(conf.color_fons) 
        rect = self.image.get_rect()
        rect.center = s.get_rect().center
        s.blit(self.image, rect)
        pygame.display.flip()

    def event(self,e): 
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                return self.game.change_state('OPTIONS')
            elif e.key == K_v:
                return self.game.change_state('CHOOSE_FIGHTER')
            elif e.key == K_b:
                return self.game.change_state('EXIT')
''' [][][][][][][][][][][][][][][][][][][][][][][][][][][][][] '''



''' [][][][][][][][][][]   OPTIONS MENU   [][][][][][][][][][] '''
class Options(engine.State):
#       ESCAPE - to go back to the main menu
    
    def init(self):
        self.image = pygame.image.load("options_menu.png") 
    
    def paint(self, s):
        s.fill(conf.color_fons) 
        rect = self.image.get_rect()
        rect.center = s.get_rect().center
        s.blit(self.image, rect)
        pygame.display.flip()

    def event(self,e): 
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                return self.game.change_state('MENU')
''' [][][][][][][][][][][][][][][][][][][][][][][][][][][][][] '''
class WinP1(engine.State):
    def init(self):
        self.image=pygame.image.load("winp1.png")
    def paint(self,s):
        s.fill(conf.color_fons)
        rect=self.image.get_rect()
        s.blit(self.image,rect)
        pygame.display.flip()

    def event(self,e): 
        if e.type == KEYDOWN:
            if e.key == K_BACKSPACE:
                return self.game.change_state('MENU')
            elif e.key == K_RETURN:
                return self.game.change_state('GAME')
    
class WinP2(engine.State):
    def init(self):
        self.image=pygame.image.load("winp2.png")
    def paint(self,s):
        s.fill(conf.color_fons)
        rect=self.image.get_rect()
        s.blit(self.image,rect)
        pygame.display.flip()

    def event(self,e): 
        if e.type == KEYDOWN:
            if e.key == K_BACKSPACE:
                return self.game.change_state('MENU')
            elif e.key == K_RETURN:
                return self.game.change_state('GAME')
    


''' [][][][][][][] CHOOSE YOUR FIGHETER 1 SCREEN [][][][][][][] '''
class Choose_Fighter1(engine.State):
#       BACKSPACE - to go back to the main menu
    
    def init(self):
        self.image = pygame.image.load("choose_player_1.png") 
    
    def paint(self, s):
        s.fill(conf.color_fons) 
        rect = self.image.get_rect()
        rect.center = s.get_rect().center
        s.blit(self.image, rect)
        pygame.display.flip()

    def event(self,e): 
        if e.type == KEYDOWN:
            if e.key == K_BACKSPACE:
                return self.game.change_state('MENU')
            elif e.key == K_1 or e.key == K_KP1:
                self.game.character1 = 1
                return self.game.change_state('CHOOSE_FIGHTER_2')
            elif e.key == K_2 or e.key == K_KP2:
                self.game.character1 = 2
                return self.game.change_state('CHOOSE_FIGHTER_2')
##            elif e.key == K_3:
##                self.game.character1 = 3
##                return self.game.change_state('CHOOSE_FIGHTER_2')
##            elif e.key == K_4:
##                self.game.character1 = 4
##                return self.game.change_state('CHOOSE_FIGHTER_2')
''' [][][][][][][][][][][][][][][][][][][][][][][][][][][][][] '''


''' [][][][][][][] CHOOSE YOUR FIGHETER 2 SCREEN [][][][][][][] '''
class Choose_Fighter2(engine.State):
#       BACKSPACE - to go back to the main menu
    
    def init(self):
        self.image = pygame.image.load("choose_player_2.png") 
    
    def paint(self, s):
        s.fill(conf.color_fons) 
        rect = self.image.get_rect()
        rect.center = s.get_rect().center
        s.blit(self.image, rect)
        pygame.display.flip()

    def event(self,e): 
        if e.type == KEYDOWN:
            if e.key == K_BACKSPACE:
                return self.game.change_state('CHOOSE_FIGHTER')
            elif e.key == K_1 or e.key == K_KP1:
                self.game.character2 = 1
                return self.game.change_state('GAME')
            elif e.key == K_2 or e.key == K_KP2:
                self.game.character2 = 2
                return self.game.change_state('GAME')
##            elif e.key == K_3:
##                self.game.character2 = 3
##                return self.game.change_state('GAME')
##            elif e.key == K_4:
##                self.game.character2 = 4
##                return self.game.change_state('GAME')
''' [][][][][][][][][][][][][][][][][][][][][][][][][][][][][] '''



# Programa principal
def main():
    global game
    game = Joc()
    game.run()


# Crida el programa principal només si s'executa el mòdul:
#
#   python3 joc.py
#
# o bé
#
#   python3 -m joc
#
# Importa les funcions i les classes, però no executa el programa
# principal si s'importa el mòdul:
#
#   import joc
if __name__ == "__main__":
    main()







