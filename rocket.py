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

    def check_edge(self):
        # Checa se o foguete atingiu a borda superior da tela
        if self.rect.top == self.screen_rect.top:
            if self.direction == 0:
                self.moving_forward = False
            elif self.direction == 1:
                self.direction = 2
            elif self.direction == 7:
                self.direction = 6

        # Checa se o foguete atingiu a borda inferior da tela
        if self.rect.bottom == self.screen_rect.bottom:
            if self.direction == 4:
                self.moving_forward = False
            elif self.direction == 5:
                self.direction = 6
            elif self.direction == 3:
                self.direction = 2

        # Checa se o foguete atingiu a borda direita da tela
        if self.rect.right == self.screen_rect.right:
            if self.direction == 2:
                self.moving_forward = False
            elif self.direction == 3:
                self.direction = 4
            elif self.direction == 1:
                self.direction = 0

        # Checa se o foguete atingiu a borda esquerda da tela
        if self.rect.left == self.screen_rect.left:
            if self.direction == 6:
                self.moving_forward = False
            elif self.direction == 7:
                self.direction = 0
            elif self.direction == 5:
                self.direction = 4

        # Atualiza a imagem do foguete com a nova direção
        self.image = pygame.image.load(
            direction_rocket[self.direction])

    def update(self):
        """[Atualiza a direção e a posição do foguete de acordo com as Flags
        de movimento]"""

        # Armazena a velocidade do foguete na variável speed_factor
        speed_factor = self.mr_settings.rocket_speed_factor

        # Checa se o foguete atingiu a borda
        self.check_edge()

        # Direção do foguete para a direita
        if self.change_right:
            sleep(0.1)
            if self.direction == 7:
                self.direction = 0
            else:
                self.direction += 1
            self.image = pygame.image.load(
                direction_rocket[self.direction])
            # Um temporizador para diminuir a velocidade da direção

        # Direção do foguete para a esquerda
        if self.change_left:
            sleep(0.1)
            if self.direction == 0:
                self.direction = 7
            else:
                self.direction -= 1
            self.image = pygame.image.load(
                direction_rocket[self.direction])
            # Um temporizador para diminuir a velocidade da direção

        # Movimento do Foguete de acordo com o ângulo da direção
        if self.moving_forward:
            if self.direction == 0:     # 000
                self.centerY -= speed_factor

            elif self.direction == 1:   # 045
                self.centerX += speed_factor
                self.centerY -= speed_factor

            elif self.direction == 2:   # 090
                self.centerX += speed_factor

            elif self.direction == 3:   # 135
                self.centerX += speed_factor
                self.centerY += speed_factor

            elif self.direction == 4:   # 180
                self.centerY += speed_factor

            elif self.direction == 5:   # 225
                self.centerX -= speed_factor
                self.centerY += speed_factor

            elif self.direction == 6:   # 270
                self.centerX -= speed_factor

            elif self.direction == 7:   # 315
                self.centerX -= speed_factor
                self.centerY -= speed_factor

            self.rect.centerx = self.centerX
            self.rect.bottom = self.centerY

    def blitme(self):
        """[Desenha a imagem em sua posição atual]
        """
        self.screen.blit(self.image, self.rect)
