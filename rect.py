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
    step = 10  # Tamanho de cada segmento da espiral
    x, y = center_x, center_y  # Iniciar no centro da tela

    direction = 0  # Direção inicial (0: direita, 1: baixo, 2: esquerda, 3: cima)
    length = step  # Comprimento do segmento atual

    while x >= 0 and x <= screen_size and y >= 0 and y <= screen_size:
        # Calcular próximo ponto com base na direção
        if direction == 0:  # Direita
            pygame.draw.line(screen, WHITE, (x, y), (x + length, y))
            x += length
        elif direction == 1:  # Baixo
            pygame.draw.line(screen, WHITE, (x, y), (x, y + length))
            y += length
        elif direction == 2:  # Esquerda
            pygame.draw.line(screen, WHITE, (x, y), (x - length, y))
            x -= length
        elif direction == 3:  # Cima
            pygame.draw.line(screen, WHITE, (x, y), (x, y - length))
            y -= length

        # Alternar a direção
        direction = (direction + 1) % 4

        # Incrementar o comprimento do segmento a cada duas direções (completar uma volta)
        if direction == 0 or direction == 2:
            length += step

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

