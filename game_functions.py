import sys

import pygame


def check_events(rocket):
    """[Responde a eventos de pressionamento de teclas e mouse]
    """
    # Observa eventos de teclado e de mouse

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:  # Verifica se uma tecla poi pressionada
            if event.key == pygame.K_RIGHT:
                rocket.position_right()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rocket.position_left()


def update_screen(mr_settings, screen, rocket):
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(mr_settings.bg_color)

    # Exibe a espaçonave
    rocket.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()
