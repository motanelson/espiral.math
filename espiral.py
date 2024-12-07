import pygame
import math

# Inicializar o Pygame
pygame.init()

# Configuração da janela
screen_size = 600  # Janela quadrada de 600x600 pixels
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Espiral do Centro")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Desenhar a espiral
def draw_spiral(screen):
    center_x, center_y = screen_size // 2, screen_size // 2
    radius = 1  # Raio inicial
    angle = 0  # Ângulo inicial

    # Incrementos
    radius_increment = 1  # Incremento do raio
    angle_increment = math.radians(5)  # Incremento do ângulo (5 graus em radianos)

    # Desenhar pontos da espiral
    while radius < screen_size:
        backx = int(center_x + radius * math.cos(angle))
        backy = int(center_y + radius * math.sin(angle))

        radius += radius_increment
        angle += angle_increment
        x = int(center_x + radius * math.cos(angle))
        y = int(center_y + radius * math.sin(angle))
        pygame.draw.line(screen, WHITE, (x, y),(backx,backy), 1)  # Desenhar um ponto
        

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preencher o fundo com preto
    screen.fill(BLACK)

    # Desenhar a espiral
    draw_spiral(screen)

    # Atualizar a tela
    pygame.display.flip()

# Sair do Pygame
pygame.quit()

