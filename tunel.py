import pygame

# Inicializar o Pygame
pygame.init()

# Configuração da janela
screen_size = 600  # Janela quadrada de 600x600 pixels
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Espiral Quadrada do Centro")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Desenhar a espiral quadrada
def draw_square_spiral(screen):
    center_x, center_y = screen_size // 2, screen_size // 2
    step = 20  # Tamanho de cada segmento da espiral
    x, y = 10,10  # Iniciar no centro da tela

    direction = 0  # Direção inicial (0: direita, 1: baixo, 2: esquerda, 3: cima)
    length = step  # Comprimento do segmento atual

    while x >= 0 and x <= screen_size and y >= 0 and y <= screen_size:
        
        if 0 == 0:  
            pygame.draw.rect(screen, WHITE, pygame.Rect(center_x-x/2, center_y-y/2,x,y),1)
            
            
            x=x+step
            y=y+step
            

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preencher o fundo com preto
    screen.fill(BLACK)

    # Desenhar a espiral quadrada
    draw_square_spiral(screen)

    # Atualizar a tela
    pygame.display.flip()

# Sair do Pygame
pygame.quit()

