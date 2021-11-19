import pygame

from time import sleep

direction_rocket = [
    'images/rocket_000.png',
    'images/rocket_045.png',
    'images/rocket_090.png',
    'images/rocket_135.png',
    'images/rocket_180.png',
    'images/rocket_225.png',
    'images/rocket_270.png',
    'images/rocket_315.png'
]


class MyRocket():
    def __init__(self, mr_settings, screen):
        """[Inicializa a imagem do foguete]
        """
        self.screen = screen
        self.mr_settings = mr_settings
        self.direction = 0

        # Carrega a imagem do foguete e obtém seu rect
        self.image = pygame.image.load(
            direction_rocket[self.direction])     # Carrega a imagem do foguete
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia a imagem na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro do foguete
        self.centerX = float(self.rect.centerx)
        self.centerY = float(self.rect.bottom)

        # Flags de movimento
        self.change_right = False
        self.change_left = False
        self.moving_forward = False

    def update(self):
        """[Atualiza a direção e a posição do foguete de acordo com as Flags
        de movimento]"""
        if self.change_right:
            if self.direction == 7:
                self.direction = 0
            else:
                self.direction += 1
            self.image = pygame.image.load(
                direction_rocket[self.direction])
            # Um temporizador para diminuir a velocidade da direção    
            sleep(0.1)  

        if self.change_left:
            if self.direction == 0:
                self.direction = 7
            else:
                self.direction -= 1
            self.image = pygame.image.load(
                direction_rocket[self.direction])
            # Um temporizador para diminuir a velocidade da direção    
            sleep(0.1)

        if self.moving_forward:
            if self.direction == 0:     # 000
                self.rect.bottom -= 1

            elif self.direction == 1:   # 045
                self.rect.centerx += 1
                self.rect.bottom -= 1

            elif self.direction == 2:   # 090
                self.rect.centerx += 1

            elif self.direction == 3:   # 135
                self.rect.centerx += 1
                self.rect.bottom += 1

            elif self.direction == 4:   # 180
                self.rect.bottom += 1

            elif self.direction == 5:   # 225
                self.rect.centerx -= 1
                self.rect.bottom += 1

            elif self.direction == 6:   # 270
                self.rect.centerx -= 1

            elif self.direction == 7:   # 315
                self.rect.centerx -= 1
                self.rect.bottom -= 1

    def blitme(self):
        """[Desenha a imagem em sua posição atual]
        """
        self.screen.blit(self.image, self.rect)
