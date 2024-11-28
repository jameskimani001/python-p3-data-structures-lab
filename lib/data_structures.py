#!/usr/bin/env python3

def get_names(spicy_foods):
    """Returns the names of all spicy foods."""
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Returns the list of spicy foods with a heat level over 5."""
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    """Prints the list of all spicy foods, with each one formatted with 🌶 emojis based on the heat level."""
    for food in spicy_foods:
        heat_level = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns the spicy food from the list that matches the given cuisine."""
    for food in spicy_foods:
        if food['cuisine'].lower() == cuisine.lower():
            return food
    return None

def print_spiciest_foods(spicy_foods):
    """Prints the spiciest foods with heat levels over 5, formatted with 🌶 emojis."""
    for food in get_spiciest_foods(spicy_foods):
        heat_level = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def average_heat_level(spicy_foods):
    """Returns the average heat level of the spicy foods."""
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, new_food):
    """Adds a new spicy food to the list and returns the updated list."""
    spicy_foods.append(new_food)
    return spicy_foods
