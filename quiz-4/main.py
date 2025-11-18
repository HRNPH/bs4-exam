# Quiz 4: Advanced Techniques and Real-World Scenarios
# TODO: Complete this file to extract and process complex data

import re

import requests
from bs4 import BeautifulSoup


def extract_numeric_value(text):
    """
    Extract numeric value from text using regex.

    Args:
        text (str): Text containing numeric value

    Returns:
        float: Extracted numeric value
    """
    # TODO: Use regex to extract numbers from text
    # Handle different formats like "20 mins", "320 cal", "4.7/5.0"
    pass


def fetch_html():
    """
    Fetch HTML content from the live URL.

    Returns:
        str: HTML content from the URL, or None if fetch fails
    """
    url = "https://hrnph.dev/bs4-exam/exam-4"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML from {url}: {e}")
        return None


def extract_recipe_data(html_content):
    """
    Extract and process recipe data from HTML content.

    Args:
        html_content (str): HTML content to parse

    Returns:
        dict: Dictionary containing extracted recipes and statistics
    """
    # TODO: Create BeautifulSoup object from html_content

    recipes = []

    # TODO: Extract all recipe cards
    # TODO: For each recipe, extract:
    # - Name (h3)
    # - Difficulty (data-difficulty attribute or difficulty class)
    # - Prep time (convert to numeric minutes)
    # - Servings (extract numeric value)
    # - Calories (extract numeric value)
    # - Rating (extract from data-rating attribute)

    # TODO: Calculate statistics:
    # - Average prep time
    # - Highest/lowest calorie recipes
    # - Average rating
    # - Count by difficulty level

    return {"recipes": recipes, "statistics": {}, "validation": {}}


def validate_data(recipes):
    """
    Validate extracted recipe data.

    Args:
        recipes (list): List of recipe dictionaries

    Returns:
        dict: Validation results
    """
    # TODO: Check for missing fields
    # TODO: Validate numeric ranges
    # TODO: Check data consistency
    # TODO: Return validation results

    return {
        "has_required_fields": False,
        "numeric_data_valid": False,
        "ratings_valid": False,
        "no_missing_data": False,
    }


def print_results(data):
    """
    Print the extracted data and statistics in the required format.

    Args:
        data (dict): Dictionary containing extracted information
    """
    # TODO: Print all results in the format shown in INSTRUCTION.md
    pass


def main():
    """Main function to execute the advanced data extraction."""
    # TODO: Fetch HTML content
    html_content = fetch_html()

    if html_content is None:
        print("Failed to fetch HTML content. Exiting.")
        return

    # TODO: Call extract_recipe_data() and print_results()
    data = extract_recipe_data(html_content)
    print_results(data)


if __name__ == "__main__":
    main()
