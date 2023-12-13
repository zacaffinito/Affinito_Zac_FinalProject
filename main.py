# Created by: Zac Affinito

# Create a dictionary to store the daily calorie intake
import pygame
import sys
import calendar

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

def main():
    running = True
    while running:
        window.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    input_date = True
                    input_text = ""
                    while input_date:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    input_date = False
                                elif event.key == pygame.K_BACKSPACE:
                                    input_text = input_text[:-1]
                                else:
                                    input_text += event.unicode

                        window.fill(white)
                        draw_text("Enter date (MM-DD-YY):", 50, 50)
                        draw_text(input_text, 50, 100)
                        pygame.display.update()

                    date = input_text
                    input_text = ""
                    input_calories = True
                    while input_calories:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    input_calories = False
                                elif event.key == pygame.K_BACKSPACE:
                                    input_text = input_text[:-1]
                                else:
                                    input_text += event.unicode

                        window.fill(white)
                        draw_text("Enter calories:", 50, 50)
                        draw_text(input_text, 50, 100)
                        pygame.display.update()

                    calories = int(input_text)
                    add_calories(date, calories)

                elif event.key == pygame.K_d:  # Press 'D' to view past dates' calorie info
                    input_date = True
                    input_text = ""
                    while input_date:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    input_date = False
                                elif event.key == pygame.K_BACKSPACE:
                                    input_text = input_text[:-1]
                                else:
                                    input_text += event.unicode

                        window.fill(white)
                        draw_text("Enter date (MM-DD-YY):", 50, 50)
                        draw_text(input_text, 50, 100)
                        pygame.display.update()

                    date = input_text

                    # Display calories for the entered date
                    text = display_calories(date)
                    draw_text(text, 50, 150)



        instructions = [
            "Welcome to the Calorie Tracker!",
            "Press 'A' to add calories.",
            "Press 'D' to view past calorie entries", 
            "Follow the prompts on the screen to enter date and calories.",
        ]
        for i, line in enumerate(instructions):
            draw_text(line, 50, 50 + i * 30, black)

        text = display_calories("2023-01-01")  # Replace "2023-01-01" with the date you want to display
        draw_text(text, 50, 200, black)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
