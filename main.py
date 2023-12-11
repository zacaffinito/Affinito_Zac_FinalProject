# Created by: Zac Affinito

# Create a dictionary to store the daily calorie intake
import pygame
import sys

calorie_tracker = {}

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