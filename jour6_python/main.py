import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit Slicer 🍉")

font = pygame.font.Font(None, 100)
clock = pygame.time.Clock()

fruits = ["a", "s", "d", "f", "g"]
current_fruit = random.choice(fruits)
score = 0
strikes = 0
running = True

while running:
    screen.fill((30, 30, 30))  # fond noir

    text = font.render(current_fruit, True, (255, 255, 255))
    screen.blit(text, (380, 250))

    score_text = pygame.font.Font(None, 50).render(f"Score : {score}", True, (0, 255, 0))
    screen.blit(score_text, (10, 10))

    strike_text = pygame.font.Font(None, 50).render(f"Strikes : {strikes}", True, (255, 0, 0))
    screen.blit(strike_text, (10, 60))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode == current_fruit:
                score += 1
                current_fruit = random.choice(fruits)
            else:
                strikes += 1
                if strikes >= 3:
                    running = False

    clock.tick(30)

pygame.quit()
print(f"Score final : {score}")
