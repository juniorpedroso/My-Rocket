import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """[Uma classe para representar uma estrela]"""

    def __init__(self, mr_settings, screen):
        """ Inicializa a estrela e define sua posição inicial """    
        super().__init__()
        self.screen = screen
        self.mr_settings = mr_settings

        # Carrega a imagem da estrela e define seu atributo rect
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # Inicia a estrela na parte superior da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata da estrela
        self.x = float(self.rect.x)

    def blitme(self):
        """[desenha a estrela em sua posição atual] """
        self.screen.blit(self.image, self.rect)
        
