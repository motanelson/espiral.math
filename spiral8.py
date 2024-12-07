
import pygame
import math

# Inicializar o Pygame
pygame.init()

# Configuração da janela
screen_size = 600  # Janela quadrada de 600x600 pixels
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("spiral 6")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Desenhar a espiral triangular
def draw_8_spiral(screen):
    center_x, center_y = screen_size // 2, screen_size // 2
    x, y = center_x, center_y  # Começa no centro da tela
    step = 20  # Comprimento de cada segmento da espiral
    angle = 0  # Ângulo inicial

    while x >= 0 and x <= screen_size and y >= 0 and y <= screen_size:
        # Calcular o próximo ponto baseado no ângulo
        next_x = x + step * math.cos(math.radians(angle))
        next_y = y + step * math.sin(math.radians(angle))
        pygame.draw.line(screen, WHITE, (x, y), (next_x, next_y))  # Desenhar segmento
        x, y = next_x, next_y  # Atualizar posição atual

        # Alternar o ângulo (0°, 120°, 240°, voltando a 0°)
        angle = (angle + 45) % 360

        # Aumentar o comprimento do passo gradualmente para expandir a espiral
        step += 5

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preencher o fundo com preto
    screen.fill(BLACK)

    # Desenhar a espiral triangular
    draw_8_spiral(screen)

    # Atualizar a tela
    pygame.display.flip()

# Sair do Pygame
pygame.quit()
