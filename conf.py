import pygame

''' Variables globals amb valors per configurar el joc ''' 


# Amplada i alçada de la pantalla
mides_pantalla = 680, 510
amplePant = 680
altPant = 510

# Nombre màxim d'imatges per segon (fps)
fps = 60

# Color de fons de la pantalla
color_fons = 255, 255, 255


musicamenu ='musicamenu.ogg'
sodefensa = 'sodefensa.ogg'
sosalt = 'sosalt.ogg'
sodamage = 'mixkit-man-in-pain-2197.wav'


controls='controls.png'
# Nom i mides del fitxer amb l'sprite sheet
sprite_sheet_personatge2 = "luffy1.png"
mides_sprite_sheet_personatge = 14,8
staged='fondo1.png'
Pstage=0,0
# Posició del personatge
posicio_personatge = -150,264
platf='plataforma.png'
plat=0,430
sprite_sheet_personatge1 = "saitama1.png"
sprite_sheet_personatge3 = " " #tercer personaje
sprite_sheet_personatge4 = " " #cuarto personaje
#descargar imagen con 3.0x
sprite_sheet_personatge6 = "luffy2.png"
sprite_sheet_personatge5 = "saitama2.png"
sprite_sheet_personatge7 = " " #tercer personaje 2
sprite_sheet_personatge8 = " " #cuatro personaje 2

mides_sprite_sheet_personatge2 = 14,8
posicio_personatge2 = 250,264


'''CRONO'''
# Colors del cronòmetre
color_text_crono = pygame.color.Color('darkorange')
color_fons_crono = pygame.color.Color('black')
color_text_info = pygame.color.Color('white')

# Font de lletres i mides
font_crono_filename = "DSEG14Classic-Bold.ttf"
font_crono_size = 40
font_info_size = 20





counter, text = 120, '120'.rjust(3)
