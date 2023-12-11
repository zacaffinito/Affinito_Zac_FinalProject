# Created by: Zac Affinito

# Create a dictionary to store the daily calorie intake
import pygame
import sys

calorie_tracker = {}

def display_calories_window(date):
    pygame.init()
    info_window = pygame.display.set_mode((300, 100))
    pygame.display.set_caption('Calorie Info')
    font = pygame.font.Font(None, 28)
    text = display_calories(date)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        info_window.fill((220, 220, 220))
        text_surface = font.render(text, True, (0, 0, 0))
        info_window.blit(text_surface, (20, 20))
        pygame.display.update()

    pygame.quit()


def add_calories(date, calories):
    if date in calorie_tracker:
        calorie_tracker[date] += calories
    else:
        calorie_tracker[date] = calories

def display_calories(date):
    if date in calorie_tracker:
        return f"Calories consumed on {date}: {calorie_tracker[date]}"
    else:
        return "No data available for this date."

pygame.init()

window_width, window_height = 800, 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Calorie Tracker')

white = (255, 255, 255)
black = (0, 0, 0)
grey = (200, 200, 200)

font = pygame.font.Font(None, 28)

def draw_text(text, x, y, color=black):
    text_surface = font.render(text, True, color)
    window.blit(text_surface, (x, y))


