#!/usr/bin/python3
import requests

def get_hero_data():
    """
    Send a GET request to the Flask API and return normalized hero data.

    Returns:
        str: Normalized hero data as a string.
    """
    url = 'http://localhost:5000/herodata'  # Replace with the URL of your Flask API
    response = requests.get(url)

    if response.status_code == 200:
        hero_data = response.json()
        normalized_heroes = normalize_hero_data(hero_data)
        return normalized_heroes
    else:
        print(f"Error: Unable to fetch hero data. Status code: {response.status_code}")
        return None

def normalize_hero_data(heroes):
    """
    Normalize the hero data for user-friendly display.

    Args:
        heroes (list): List of hero dictionaries.

    Returns:
        str: Normalized hero data as a string.
    """
    normalized_heroes = []
    for hero in heroes:
        name = hero['name']
        real_name = hero['realName']
        since = hero['since']
        powers = ", ".join(hero['powers'])

        normalized_hero = f"Hero: {name}\n" \
                          f"Real Name: {real_name}\n" \
                          f"First Appearance: {since}\n" \
                          f"Powers: {powers}\n"

        normalized_heroes.append(normalized_hero)

    return "\n\n".join(normalized_heroes)

if __name__ == '__main__':
    normalized_data = get_hero_data()
    if normalized_data:
        print(normalized_data)

