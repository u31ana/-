import pygame
import random
pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Убегай от врагов")
#настройки персонажа
player_size = 80
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size] #выше нижнего края, по центру
player_image = pygame.image.load("png_кик борд.png")
player_image = pygame.transform.scale(player_image,(player_size, player_size))

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]
SPEED = 10

#контроль скорости обновления экрана
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
   #если врагов меньше 10, то добавляем нового с рандомной позицией. все враги перемещаются вниз по экрану. как только заходит за нижнюю границу - удаляется
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

#проверяем столкновения
def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if (player_pos[0] < enemy_pos[0] < player_pos[0] + player_size or
                player_pos[0] < enemy_pos[0] + enemy_size < player_pos[0] + player_size) and (player_pos[1] < enemy_pos[1] < player_pos[1] + player_size or
                 player_pos[1] < enemy_pos[1] + enemy_size < player_pos[1] + player_size):
            return True
    return False

#главный цикл игры
def main():
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
#провряем, нажата ли нужная клавиша. если нажата стрелка влево и игрок не находится у левого края, то он смещается на 10 пикслелей влево. то же самое с правой стрелкой
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= 10
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
            player_pos[0] += 10

        screen.fill(WHITE)
        
        drop_enemies(enemy_list)
        draw_enemies(enemy_list)

#если есть столкновение, игра заканчивается
        if collision_check(enemy_list, player_pos):
            game_over()

        screen.blit(player_image,(player_pos[0], player_pos[1]))

        pygame.display.update()
        clock.tick(30) #кадров в секунду 
    pygame.quit()

if __name__ == "__main__":
    main()
