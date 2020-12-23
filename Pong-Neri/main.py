
from pygame.locals import *
from data.classes import *
from colorama import Fore
from time import sleep
import pygame

pygame.init() 

frame = pygame.display.set_mode((500, 600)) # Se crea el frame

game_over = False

# Jugadores
jugador = Jugador(220, 580)
jugador2 = Jugador(220, 20)

# Fuentes
fuente = pygame.font.Font(None, 19)
fuente2 = pygame.font.Font(None, 33)

# posicion de la pelota
bola_pos_x = 350
bola_pos_y = 200

# Velocidad de bola
bola_vX = 0.35
bola_vY = 0.35


while not game_over:

    frame.fill((0, 0, 0)) # Dibuja el fondo

    # Se crea la bola
    bola = pygame.Rect(bola_pos_x, bola_pos_y, 7, 7)

    # Indicador de vida (jugador1)
    vida_jugador1 = fuente2.render(str(jugador.vidas), 0, (220, 220, 220))

    # Indicador de vida (jugador1)
    vida_jugador2 = fuente2.render(str(jugador2.vidas), 0, (220, 220, 220))

    # Points counter (jugador2)
    puntos_jugador = fuente.render("Puntos: "+str(jugador.puntos), 0, (255, 255, 255))

    # Points counter (jugador2)
    puntos_jugador2 = fuente.render("Puntos: "+str(jugador2.puntos), 0, (255, 255, 255))

    # zona de eliminacion de vidas
    limite_jugador2 = pygame.Rect(0, -10, 500, 5)
    limite_jugador1 = pygame.Rect(0, 690, 500, 5)

    # Separador del juego ( banda )
    banda = fuente.render("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -", 0, (200, 200, 200))

##################################[ LOGIC ]#########################################    

    # Deteccion de controles
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(Fore.YELLOW+"[!] Haz salido!"+Fore.RESET)
            exit()
        elif event.type == KEYDOWN:
            # Jugador --------->
            if event.key == K_RIGHT:jugador.MoverseDerecha()
            if event.key == K_LEFT:jugador.MoverseIzquierda()


            # Jugador2 -------->
            if event.key == K_d: jugador2.MoverseDerecha()
            if event.key == K_a:jugador2.MoverseIzquierda()
    

    # Detector de colisiones CON LOS BORDES ( BOLA - FRAME )
    if (bola_pos_x > 500 or bola_pos_x < 0):
        bola_vX *= -1 # vX se va multiplicando por -1

    # Colision de la bola con el jugador1
    elif bola.colliderect(jugador.hitbox):
        bola_vX *= 1.08;bola_vY *= -1.08
        jugador.puntos += 1

    # Colision de la bola con el jugador2
    elif bola.colliderect(jugador2.hitbox):
        bola_vX *= 1.08;bola_vY *= -1.08
        jugador2.puntos += 1
    
    # Colisiones con el limite de los jugadores ( Resta de Vidas )
    if bola.colliderect(limite_jugador2): # Jugador1
        bola_pos_x = 250;bola_pos_y = 290
        bola_vX = 0.30;bola_vY = 0.30
        jugador2.vidas -= 1
        sleep(2)
    
    if bola.colliderect(limite_jugador1): # jugador2
        bola_pos_x = 250;bola_pos_y = 290
        bola_vX = 0.25;bola_vY = 0.25
        jugador.vidas -= 1
        sleep(2)
    

    # Wanting to assign a movement limiter (so that it does not leave the "map"),
    # it is not executed, the only thing I notice is that the position of the players
    # does not change, it remains static, the number remains in its default location. ..
    
    """
    # Jugador1 limiter
    if jugador.pos_x > 400:
        jugador.pos_x = 400
    if jugador.pos_x < 20:
        jugador.pos_x = 20
    
    # Jugador2 limiter
    if jugador2.pos_x > 400:
        jugador2.pos_x = 400
    if jugador2.pos_x < 20:
        jugador2.pos_x = 20
    """


    # La bola se mueve hacia los lados
    bola_pos_x += bola_vX
    # La bola se mueve hacia arriba
    bola_pos_y += bola_vY



##################[ Objects draw ]####################
    if (jugador.vidas and jugador2.vidas != 0):

        # Metodos de dibujo
        pygame.draw.rect(frame, (255, 255, 255), bola) # dibuja la bola
        jugador.Draw(frame) # dibuja al jugador
        jugador2.Draw(frame) # Se dibuja al jugador2
        #pygame.draw.rect(frame, (255, 255, 255), banda_linea) # dibuja la linea divisoria
        frame.blit(banda, (0, 295))

        # Indicadores de puntaje
        frame.blit(puntos_jugador, (15, 305)) # dibuja el indicador de puntos del jugador1
        frame.blit(puntos_jugador2, (400, 285)) # dibuja el indicador de puntos del jugador2
    
        # Indicadores de Vida
        frame.blit(vida_jugador1, (250, 530)) # jugador1
        frame.blit(vida_jugador2, (250, 50)) # jugador2

        # Limites de los jugadores ( Disminusores de vida )
        pygame.draw.rect(frame, (255, 255, 255), limite_jugador1)
        pygame.draw.rect(frame, (255, 255, 255), limite_jugador2)

        pygame.display.update()
    else:
        break
        
