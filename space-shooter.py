import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Load spaceship image
player_image = pygame.image.load('spaceship.png')
player_image = pygame.transform.scale(player_image, (50, 50))

# Player settings
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 60
player_speed = 7

# Bullet settings
bullets = []
bullet_speed = 10
bullet_width = 5
bullet_height = 10

# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_speed = 2
enemies = []

# Spawn enemies
def spawn_enemy():
    x = random.randint(0, SCREEN_WIDTH - enemy_width)
    y = random.randint(-150, -50)
    enemies.append(pygame.Rect(x, y, enemy_width, enemy_height))

# Main game loop
running = True
clock = pygame.time.Clock()
spawn_timer = 0  # Timer for spawning enemies

while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - 50:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:  # Limit number of bullets on screen
            bullets.append(pygame.Rect(player_x + 22, player_y, bullet_width, bullet_height))

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Spawn enemies at intervals
    spawn_timer += 1
    if spawn_timer > 30:
        spawn_enemy()
        spawn_timer = 0

    # Move enemies
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > SCREEN_HEIGHT:
            enemies.remove(enemy)

    # Check for collisions
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    # Draw player
    screen.blit(player_image, (player_x, player_y))

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, BLUE, bullet)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
