#!/usr/bin/env python3

from data_structures import get_names, get_spiciest_foods, print_spicy_foods, \
    create_spicy_food, get_spicy_food_by_cuisine, print_spiciest_foods, average_heat_level

import io
import sys

class TestDataStructures:
    '''Module data_structures.py'''

    SPICY_FOODS = [
        {
            "name": "Green Curry",
            "cuisine": "Thai",
            "heat_level": 9,
        },
        {
            "name": "Buffalo Wings",
            "cuisine": "American",
            "heat_level": 3,
        },
        {
            "name": "Mapo Tofu",
            "cuisine": "Sichuan",
            "heat_level": 6,
        }
    ]

    def test_get_names(self):
        '''contains function get_names() that retrieves names from list of foods.'''
        assert get_names(TestDataStructures.SPICY_FOODS) == ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']

    def test_get_spiciest_foods(self):
        '''contains function get_spiciest_foods() that returns foods with a heat_level over 5.'''
        spicy_foods = get_spiciest_foods(TestDataStructures.SPICY_FOODS)
        for food in spicy_foods:
            assert food["heat_level"] > 5  # Assert that the heat_level is greater than 5

    def test_print_spicy_foods(self):
        '''contains function print_spicy_foods that returns all foods formatted with 🌶  emojis.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_spicy_foods(TestDataStructures.SPICY_FOODS)
        sys.stdout = sys.__stdout__
        # Check that the printed output matches the expected format
        assert captured_out.getvalue() == "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\n" + \
                                           "Buffalo Wings (American) | Heat Level: 🌶🌶🌶\n" + \
                                           "Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶\n"

    def test_get_spicy_food_by_cuisine(self):
        '''contains function get_spicy_food_by_cuisine that returns the food that matches a cuisine.'''
        result = get_spicy_food_by_cuisine(TestDataStructures.SPICY_FOODS, "American")
        assert result == {
            "name": "Buffalo Wings",
            "cuisine": "American",
            "heat_level": 3,
        }

    def test_print_spiciest_foods(self):
        '''contains function print_spiciest_foods that returns foods with heat_level over 5 formatted with 🌶  emojis.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_spiciest_foods(TestDataStructures.SPICY_FOODS)
        sys.stdout = sys.__stdout__
        # Check that the printed output matches the expected format for spiciest foods
        assert captured_out.getvalue() == "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\n" + \
                                           "Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶\n"

    def test_average_heat_level(self):
        '''contains function average_heat_level that returns the average of heat_levels in spicy_foods.'''
        result = average_heat_level(TestDataStructures.SPICY_FOODS)
        assert result == 6  # The average heat level should be 6

    def test_create_spicy_food(self):
        '''contains function create_spicy_food that returns the original list of spicy_foods with new spicy_food added.'''
        new_spicy_foods = create_spicy_food(
            TestDataStructures.SPICY_FOODS,
            {
                'name': 'Griot',
                'cuisine': 'Haitian',
                'heat_level': 10,
            }
        )

        assert new_spicy_foods == [
            {
                "name": "Green Curry",
                "cuisine": "Thai",
                "heat_level": 9,
            },
            {
                "name": "Buffalo Wings",
                "cuisine": "American",
                "heat_level": 3,
            },
            {
                "name": "Mapo Tofu",
                "cuisine": "Sichuan",
                "heat_level": 6,
            },
            {
                "name": "Griot",
                "cuisine": "Haitian",
                "heat_level": 10,
            },
        ]
