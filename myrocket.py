import pygame

from settings import Settings
from rocket import MyRocket
from sky import Star
import game_functions as gf


def run_game():
    # Inicializa e cria um objeto para a tela
    pygame.init()
    mr_settings = Settings()
    screen = pygame.display.set_mode(
        (mr_settings.screen_width, mr_settings.screen_height))
    background = pygame.image.load('images/City Night.png')
    pygame.display.set_caption('<< MY ROCKET >>')

    # Cria um foguete
    rocket = MyRocket(mr_settings, screen)

    # Cria uma estrela
    star = Star(mr_settings, screen) 

    # Inicia o laço principal da aplicação
    while True:

        # Observa eventos de teclado e mouse
        gf.check_events(rocket)

        # Checa se alguma tecla está sendo pressionada
        rocket.update()

        # Chama a função que atualiza a tela
        gf.update_screen(mr_settings, screen, rocket, star, background)


run_game()
