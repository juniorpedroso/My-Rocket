import pygame

from settings import Settings
from rocket import MyRocket
import game_functions as gf



def run_game():
    # Inicializa e cria um objeto para a tela
    pygame.init()
    mr_settings = Settings()
    screen = pygame.display.set_mode(
        (mr_settings.screen_width, mr_settings.screen_height))
    pygame.display.set_caption('<< MY ROCKET >>')

    # Cria um foguete
    rocket = MyRocket(mr_settings, screen)


    # Inicia o laço principal da aplicação
    while True:

        # Observa eventos de teclado e mouse
        gf.check_events(rocket)
        
        # Redesenha a tela a cada passagem pelo laço
        screen.fill(mr_settings.bg_color)
        rocket.blitme()

        # Deixa a tela mais recente visível
        pygame.display.flip()


run_game()
