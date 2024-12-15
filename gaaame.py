import pygame
import random
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Убегай от врагов")

player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]
SPEED = 10

clock = pygame.time.Clock()

def game_over():
    font = pygame.font.SysFont("monospace", 35)
    text = font.render("GAME OVER", True, RED)
    screen.blit(text, [WIDTH // 3, HEIGHT // 3])
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    quit()

def drop_enemies(enemy_list):
    if len(enemy_list) < 10: 
        enemy_x_pos = random.randint(0, WIDTH - enemy_size)
        enemy_list.append([enemy_x_pos, 0])
    for enemy_pos in enemy_list:
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.remove(enemy_pos)

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if (player_pos[0] < enemy_pos[0] < player_pos[0] + player_size or
                player_pos[0] < enemy_pos[0] + enemy_size < player_pos[0] + player_size) and (player_pos[1] < enemy_pos[1] < player_pos[1] + player_size or
                 player_pos[1] < enemy_pos[1] + enemy_size < player_pos[1] + player_size):
            return True
    return False

def main():
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= 10
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
            player_pos[0] += 10

        screen.fill(WHITE)
        
        drop_enemies(enemy_list)
        draw_enemies(enemy_list)

        if collision_check(enemy_list, player_pos):
            game_over()

        pygame.draw.rect(screen, BLACK, (player_pos[0], player_pos[1], player_size, player_size))

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
