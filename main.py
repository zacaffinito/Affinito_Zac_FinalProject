# Code Created By: Zac Affinito
import pygame
import calendar
from datetime import datetime, timedelta

calorie_tracker = {}

def display_calories_window(date):
    pygame.init()
    info_window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Calorie Info')
    font = pygame.font.Font(None, 36)
    text = display_calories(date)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        info_window.fill((220, 220, 220))
        text_surface = font.render(text, True, (0, 0, 0))
        info_window.blit(text_surface, (50, 50))

        instructions = [
            "Press 'Esc' to return to the main page.",
        ]
        for i, line in enumerate(instructions):
            draw_text(info_window, font, line, 50, 450 + i * 50, (50, 50, 50))

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

def display_calories_window_with_calendar(date):
    pygame.init()
    calendar_window = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Calorie Info & Calendar')
    font = pygame.font.Font(None, 36)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:
                    return

        calendar_window.fill((220, 220, 220))

        text_date = display_calories(date)
        text_surface_date = font.render(text_date, True, (0, 0, 0))
        calendar_window.blit(text_surface_date, (50, 50))

        previous_week_dates = get_previous_week_dates(date)
        calorie_info = ""
        for day in previous_week_dates:
            calorie_info += display_calories(day) + "\n"

        draw_calendar(calendar_window, font, calorie_info)

        instructions = [
            "Press 'V' to return to the main page.",
        ]
        for i, line in enumerate(instructions):
            draw_text(calendar_window, font, line, 50, 650 + i * 50, (50, 50, 50))

        pygame.display.update()

    pygame.quit()

def get_previous_week_dates(date):
    date_format = "%m-%d-%y"
    date_obj = datetime.strptime(date, date_format)
    prev_week_dates = []

    start_of_week = date_obj - timedelta(days=date_obj.weekday())

    for i in range(7):
        prev_week_dates.append((start_of_week + timedelta(days=i)).strftime(date_format))

    return prev_week_dates

def draw_calendar(window, font, calorie_info):
    date_format = "%m-%d-%y"
    today = datetime.today().strftime(date_format)

    cell_width = 120
    cell_height = 90
    start_x = 50
    start_y = 120

    for i, day in enumerate(calendar.day_abbr):
        pygame.draw.rect(window, (200, 200, 200), (start_x + (i * cell_width), start_y, cell_width, cell_height))
        text_surface = font.render(day, True, (0, 0, 0))
        window.blit(text_surface, (start_x + (i * cell_width) + 20, start_y + 20))

    for i, day in enumerate(calorie_info.split('\n')):
        x = start_x + (i % 7) * cell_width
        y = start_y + (i // 7) * cell_height

        if day.startswith("No data"):
            color = (255, 150, 150)
        elif day.startswith("Calories"):
            if day.split(": ")[1] == today:
                color = (150, 255, 150)
            else:
                color = (200, 200, 255)
        else:
            continue

        pygame.draw.rect(window, color, (x, y, cell_width, cell_height))
        text_surface = font.render(day, True, (0, 0, 0))
        window.blit(text_surface, (x + 10, y + 40))

def draw_text(window, font, text, x, y, color=(0, 0, 0)):
    text_surface = font.render(text, True, color)
    window.blit(text_surface, (x, y))

def main():
    pygame.init()

    window_width, window_height = 1000, 800
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Calorie Tracker')

    white = (255, 255, 255)
    black = (0, 0, 0)

    font = pygame.font.Font(None, 36)

    running = True
    calorie_entry_mode = False

    while running:
        window.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and not calorie_entry_mode:
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
                        draw_text(window, font, "Enter date (MM-DD-YY):", 50, 50)
                        draw_text(window, font, input_text, 50, 100)
                        pygame.display.update()

                    date = input_text
                    calorie_entry_mode = True

                elif event.key == pygame.K_RETURN and calorie_entry_mode:
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
                        draw_text(window, font, "Enter calories:", 50, 50)
                        draw_text(window, font, input_text, 50, 100)
                        pygame.display.update()

                    calories = int(input_text)
                    add_calories(date, calories)
                    calorie_entry_mode = False

                elif event.key == pygame.K_d and not calorie_entry_mode:
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
                        draw_text(window, font, "Enter date (MM-DD-YY):", 50, 50)
                        draw_text(window, font, input_text, 50, 100)
                        pygame.display.update()

                    date = input_text
                    display_calories_window_with_calendar(date)

        instructions = [
            "Welcome to the Calorie Tracker!",
            "Press 'A' to add calories.",
            "Press 'D' to view past calorie entries",
            "Follow the prompts on the screen to enter date and calories.",
        ]
        for i, line in enumerate(instructions):
            draw_text(window, font, line, 50, 50 + i * 50, black)

        text = display_calories("2023-01-01")
        draw_text(window, font, text, 50, 400, black)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
