vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
cinza = (230, 230, 230)
cinzaescuro = (128, 128, 128)


class Settings():
    """[Uma classe para armazenar todas as configurações de 
    My Rocket.]
    """

    def __init__(self):
        """[Inicializa as configurações do jogo]
        """
        # Configuração da tela
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = cinzaescuro

        # Configurações do foguete
        self.rocket_speed_factor = 0.5
