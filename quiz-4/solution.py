# Quiz 4: Advanced Techniques and Real-World Scenarios - SOLUTION
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
    # Use regex to extract numbers from text
    # Handle different formats like "20 mins", "320 cal", "4.7/5.0"
    if not text:
        return 0.0

    # Extract the first number found (handles both integers and decimals)
    match = re.search(r"(\d+\.?\d*)", text.strip())
    if match:
        return float(match.group(1))
    return 0.0


def fetch_html():
    """
    Fetch HTML content from the live URL.

    Returns:
        str: HTML content from the URL
    """
    url = "https://hrnph.dev/bs4-exam/exam-4"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching HTML: {e}")
        return None


def extract_recipe_data(html_content):
    """
    Extract and process recipe data from HTML content.

    Args:
        html_content (str): HTML content to parse

    Returns:
        dict: Dictionary containing extracted recipes and statistics
    """
    # Use the provided HTML content
    content = html_content

    # Create BeautifulSoup object
    soup = BeautifulSoup(content, "html.parser")

    recipes = []

    # Extract all recipe cards
    recipe_cards = soup.select(".recipe-card")

    for card in recipe_cards:
        # Extract name (h3)
        name = card.select_one("h3").get_text(strip=True)

        # Extract difficulty (data-difficulty attribute or difficulty class)
        difficulty = card.get("data-difficulty", "unknown").capitalize()

        # Extract prep time (convert to numeric minutes)
        prep_time_elem = card.select_one(".prep-time")
        prep_time_text = prep_time_elem.get_text() if prep_time_elem else "0"
        prep_time = extract_numeric_value(prep_time_text)

        # Extract servings (extract numeric value)
        servings_elem = card.select_one(".servings")
        servings_text = servings_elem.get_text() if servings_elem else "0"
        servings = extract_numeric_value(servings_text)

        # Extract calories (extract numeric value)
        calories_elem = card.select_one(".calories")
        calories_text = calories_elem.get_text() if calories_elem else "0"
        calories = extract_numeric_value(calories_text)

        # Extract rating (extract from data-rating attribute)
        rating_elem = card.select_one(".recipe-rating")
        rating = 0.0
        if rating_elem and rating_elem.get("data-rating"):
            try:
                rating = float(rating_elem.get("data-rating"))
            except ValueError:
                rating = 0.0

        recipes.append(
            {
                "name": name,
                "difficulty": difficulty,
                "prep_time": prep_time,
                "servings": servings,
                "calories": calories,
                "rating": rating,
            }
        )

    # Calculate statistics
    statistics = {}

    # Average prep time
    if recipes:
        avg_prep_time = sum(r["prep_time"] for r in recipes) / len(recipes)
        statistics["average_prep_time"] = avg_prep_time

        # Highest and lowest calorie recipes
        highest_cal = max(recipes, key=lambda x: x["calories"])
        lowest_cal = min(recipes, key=lambda x: x["calories"])
        statistics["highest_calories"] = highest_cal
        statistics["lowest_calories"] = lowest_cal

        # Average rating
        avg_rating = sum(r["rating"] for r in recipes) / len(recipes)
        statistics["average_rating"] = avg_rating

        # Count by difficulty level
        difficulty_counts = {}
        for recipe in recipes:
            diff = recipe["difficulty"]
            difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1
        statistics["difficulty_counts"] = difficulty_counts

    # Validate data
    validation = validate_data(recipes)

    return {"recipes": recipes, "statistics": statistics, "validation": validation}


def validate_data(recipes):
    """
    Validate extracted recipe data.

    Args:
        recipes (list): List of recipe dictionaries

    Returns:
        dict: Validation results
    """
    validation = {
        "has_required_fields": True,
        "numeric_data_valid": True,
        "ratings_valid": True,
        "no_missing_data": True,
    }

    # Check for missing fields
    required_fields = [
        "name",
        "difficulty",
        "prep_time",
        "servings",
        "calories",
        "rating",
    ]
    for recipe in recipes:
        for field in required_fields:
            if field not in recipe or recipe[field] is None:
                validation["has_required_fields"] = False
                validation["no_missing_data"] = False
                break

    # Validate numeric ranges
    for recipe in recipes:
        if recipe["prep_time"] < 0 or recipe["servings"] <= 0 or recipe["calories"] < 0:
            validation["numeric_data_valid"] = False

    # Check ratings within valid range
    for recipe in recipes:
        if recipe["rating"] < 0 or recipe["rating"] > 5:
            validation["ratings_valid"] = False

    return validation


def print_results(data):
    """
    Print the extracted data and statistics in the required format.

    Args:
        data (dict): Dictionary containing extracted information
    """
    print("Recipe Data Extraction:")
    for i, recipe in enumerate(data["recipes"], 1):
        print(
            f"{i}. {recipe['name']} ({recipe['difficulty']}) - {int(recipe['prep_time'])} mins, {int(recipe['servings'])} servings, {int(recipe['calories'])} cal, Rating: {recipe['rating']}"
        )

    print("\nStatistics:")
    stats = data["statistics"]
    if "average_prep_time" in stats:
        print(f"- Average prep time: {stats['average_prep_time']:.1f} minutes")
    if "highest_calories" in stats:
        high = stats["highest_calories"]
        print(f"- Highest calories: {high['name']} ({int(high['calories'])} cal)")
    if "lowest_calories" in stats:
        low = stats["lowest_calories"]
        print(f"- Lowest calories: {low['name']} ({int(low['calories'])} cal)")
    if "average_rating" in stats:
        print(f"- Average rating: {stats['average_rating']:.1f}/5.0")
    if "difficulty_counts" in stats:
        diff_counts = stats["difficulty_counts"]
        diff_str = ", ".join([f"{k}: {v}" for k, v in diff_counts.items()])
        print(f"- Recipes by difficulty: {diff_str}")

    print("\nData Validation:")
    validation = data["validation"]
    status = "✓" if validation["has_required_fields"] else "✗"
    print(f"- All recipes have required fields: {status}")
    status = "✓" if validation["numeric_data_valid"] else "✗"
    print(f"- Numeric data successfully extracted: {status}")
    status = "✓" if validation["ratings_valid"] else "✗"
    print(f"- Ratings within valid range: {status}")
    status = "✓" if validation["no_missing_data"] else "✗"
    print(f"- No missing critical data: {status}")


def main():
    """Main function to execute the advanced data extraction."""
    # Fetch HTML content first
    html_content = fetch_html()
    if html_content is None:
        print("Failed to fetch HTML content. Exiting.")
        return

    # Call extract_recipe_data() with the fetched HTML content and print_results()
    data = extract_recipe_data(html_content)
    print_results(data)


if __name__ == "__main__":
    main()
