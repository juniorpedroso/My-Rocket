import pygame

position_rocket = [
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
        self.position = 0

        # Carrega a imagem do foguete e obtém seu rect
        self.image = pygame.image.load(
            position_rocket[self.position])
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia a imagem na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def position_right(self):
        if self.position == 7:
            self.position = 0
        else:
            self.position += 1
        self.image = pygame.image.load(
            position_rocket[self.position])

    
    def position_left(self):
        if self.position == 0:
            self.position = 7
        else:
            self.position -= 1
        self.image = pygame.image.load(
            position_rocket[self.position])
        
        

    def blitme(self):
        """[Desenha a imagem em sua posição atual]
        """
        self.screen.blit(self.image, self.rect)