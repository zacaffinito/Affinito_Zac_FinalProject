# Code Created By: Zac Affinito
# Citations: 
# https://www.youtube.com/watch?v=jO6qQDNa2UY&ab_channel=TechWithTim
# https://www.youtube.com/watch?v=e0Pys7H-sjM&t=242s&ab_channel=Amulya%27sAcademy
# https://www.youtube.com/watch?v=msDgb2qU-EI&ab_channel=SundeepSaradhiKanthety
# https://www.youtube.com/watch?v=eirjjyP2qcQ&ab_channel=CoreySchafer

import pygame
import calendar
from datetime import datetime, timedelta

calorie_tracker = {}  
# dictionary to store calorie info

def display_calories_window(date):
    # initialize pygame and set up window
    pygame.init()
    info_window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Calorie Info')
    font = pygame.font.Font(None, 36)
    text = display_calories(date)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                # Handle window closure event
                running = False  
                # Set running to False to exit the loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        info_window.fill((220, 220, 220))
        text_surface = font.render(text, True, (0, 0, 0))
        info_window.blit(text_surface, (50, 50))

        # display instructions to the user
        instructions = [
            "Press 'Esc' to return to the main page.",
        ]
        for i, line in enumerate(instructions):
            draw_text(info_window, font, line, 50, 450 + i * 50, (50, 50, 50))

        pygame.display.update()

    pygame.quit()

# add functionality for adding and displaying calorie info
def add_calories(date, calories):
    if date in calorie_tracker:
        calorie_tracker[date]['calories'] += calories
    else:
        calorie_tracker[date] = {'calories': calories}

def display_calories(date):
    if date in calorie_tracker:
        return f"Calories consumed on {date}: {calorie_tracker[date]['calories']} (press 'V' to return)"
    else:
        return "No data available for this date - press 'V' to return"

# show calorie info in calendar view across 7 days surrounding a selected date
def display_calories_window_with_calendar(date):
    pygame.init()
    calendar_window = pygame.display.set_mode((1200, 300))
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

# cells in calendar view - render with info and at a certain size per cell
        cell_width = 150
        cell_height = 150
        start_x = 50
        start_y = 120

        previous_week_dates = get_previous_week_dates(date)
        for i, day in enumerate(previous_week_dates):
            calorie_text = ''
            if day in calorie_tracker:
                calorie_text = str(calorie_tracker[day]['calories'])

            # Calculate positions considering window boundaries
            row = i // 7
            col = i % 7

            x = start_x + col * cell_width
            y = start_y + row * cell_height

            # Wrap around if box is out of window bounds
            if x >= calendar_window.get_width():
                x -= 7 * cell_width
                y += cell_height

            # Box color (based on date)
            color = (200, 200, 255) if day == datetime.today().strftime("%m-%d-%y") else (255, 255, 255)

            pygame.draw.rect(calendar_window, color, (x, y, cell_width, cell_height), 2)

            # render calories consumed and day
            text_surface_day = font.render(day, True, (0, 0, 0))
            calendar_window.blit(text_surface_day, (x + 10, y + 10))

            # calories consumed
            text_surface_calories = font.render(calorie_text, True, (0, 0, 0))
            calendar_window.blit(text_surface_calories, (x + 10, y + 60))

        pygame.display.update()

    pygame.quit()

# function to get previous dates in the week
def get_previous_week_dates(date):
    date_format = "%m-%d-%y"
    date_obj = datetime.strptime(date, date_format)
    prev_week_dates = []

    start_of_week = date_obj - timedelta(days=date_obj.weekday())

    for i in range(7):
        prev_week_dates.append((start_of_week + timedelta(days=i)).strftime(date_format))

    return prev_week_dates

# draw text and calendar view
def draw_calendar(window, font, calorie_info, today):
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
                # Highlight today's date with a different color
            else:
                color = (200, 200, 255)
        else:
            continue

        pygame.draw.rect(window, color, (x, y, cell_width, cell_height), 2)  # Add border to cells
        text_surface = font.render(day, True, (0, 0, 0))
        window.blit(text_surface, (x + 10, y + 40))
        # define fonts and window

def draw_text(window, font, text, x, y, color=(0, 0, 0)):
    # draw text on the window
    text_surface = font.render(text, True, color)
    window.blit(text_surface, (x, y))

def main():
    pygame.init()
# main functionality - main loop controlling the program flow
# displays intructions, handles user's input, and manages the state of the program.
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
                        # fill window with white background
                        draw_text(window, font, "Enter date (MM-DD-YY):", 50, 50)
                        draw_text(window, font, input_text, 50, 100)
                        pygame.display.update()

                    date = input_text
                    calorie_entry_mode = True

                elif event.key == pygame.K_RETURN and calorie_entry_mode:
                    # prompt the user to enter calories for the date
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
                    # enter date to view calendar with calories history
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
        # display user instructions
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

        # update the display
    pygame.quit()
    # quit pygame after the main loop comes to an end
if __name__ == "__main__":
    main()
