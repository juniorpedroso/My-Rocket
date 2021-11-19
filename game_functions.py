import sys

import pygame


def check_keydown_events(event, rocket):
    """[Responde a pressionamentos de teclas]
    """
    # Pressionando a tecla o movimento inicia
    if event.key == pygame.K_RIGHT:
        rocket.change_right = True
    elif event.key == pygame.K_LEFT:
        rocket.change_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_forward = True


def check_keyup_events(event, rocket):
    """[Responde a soltura de teclas]
    """
    if event.key == pygame.K_RIGHT:
        rocket.change_right = False
    elif event.key == pygame.K_LEFT:
        rocket.change_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_forward = False


def check_events(rocket):
    """[Responde a eventos de pressionamento de teclas e mouse]
    """
    # Observa eventos de teclado e de mouse

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def update_screen(mr_settings, screen, rocket):
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(mr_settings.bg_color)

    # Exibe a espaçonave
    rocket.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()
