# Quiz 4 Grader
import os
import re
import subprocess
import sys

from bs4 import BeautifulSoup


def load_expected_output():
    """Load the expected correct output by parsing index.html directly."""

    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()

    soup = BeautifulSoup(content, "html.parser")

    # Extract recipe data
    recipes = []
    recipe_cards = soup.select(".recipe-card")

    for i, card in enumerate(recipe_cards, 1):
        name = card.select_one("h3").get_text(strip=True)
        difficulty = card.get("data-difficulty", "").capitalize()

        # Extract numeric values
        prep_time_elem = card.select_one(".prep-time")
        prep_time = re.findall(
            r"\d+", prep_time_elem.get_text() if prep_time_elem else ["0"]
        )[0]

        servings_elem = card.select_one(".servings")
        servings = re.findall(
            r"\d+", servings_elem.get_text() if servings_elem else ["0"]
        )[0]

        calories_elem = card.select_one(".calories")
        calories = re.findall(
            r"\d+", calories_elem.get_text() if calories_elem else ["0"]
        )[0]

        rating = (
            card.select_one(".recipe-rating").get("data-rating", "0")
            if card.select_one(".recipe-rating")
            else "0"
        )

        recipes.append(
            {
                "name": name,
                "difficulty": difficulty,
                "prep_time": int(prep_time),
                "servings": int(servings),
                "calories": int(calories),
                "rating": float(rating),
            }
        )

    # Calculate statistics
    avg_prep_time = (
        sum(r["prep_time"] for r in recipes) / len(recipes) if recipes else 0
    )
    highest_cal = max(recipes, key=lambda x: x["calories"]) if recipes else None
    lowest_cal = min(recipes, key=lambda x: x["calories"]) if recipes else None
    avg_rating = sum(r["rating"] for r in recipes) / len(recipes) if recipes else 0

    difficulty_counts = {}
    for recipe in recipes:
        diff = recipe["difficulty"]
        difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1

    # Build expected output
    expected = []
    expected.append("Recipe Data Extraction:")

    for i, recipe in enumerate(recipes, 1):
        expected.append(
            f"{i}. {recipe['name']} ({recipe['difficulty']}) - {recipe['prep_time']} mins, {recipe['servings']} servings, {recipe['calories']} cal, Rating: {recipe['rating']}"
        )

    expected.append("")
    expected.append("Statistics:")
    expected.append(f"- Average prep time: {avg_prep_time:.1f} minutes")
    if highest_cal:
        expected.append(
            f"- Highest calories: {highest_cal['name']} ({highest_cal['calories']} cal)"
        )
    if lowest_cal:
        expected.append(
            f"- Lowest calories: {lowest_cal['name']} ({lowest_cal['calories']} cal)"
        )
    expected.append(f"- Average rating: {avg_rating:.1f}/5.0")

    diff_str = ", ".join([f"{k}: {v}" for k, v in difficulty_counts.items()])
    expected.append(f"- Recipes by difficulty: {diff_str}")

    expected.append("")
    expected.append("Data Validation:")
    expected.append("- All recipes have required fields: ✓")
    expected.append("- Numeric data successfully extracted: ✓")
    expected.append("- Ratings within valid range: ✓")
    expected.append("- No missing critical data: ✓")

    return "\n".join(expected), recipes


def run_student_solution():
    """Run the student's main.py and capture output."""
    try:
        result = subprocess.run(
            [sys.executable, "main.py"], capture_output=True, text=True, timeout=30
        )
        return result.stdout.strip(), result.stderr
    except subprocess.TimeoutExpired:
        return "", "Timeout: Program took too long to execute"
    except Exception as e:
        return "", f"Error running solution: {str(e)}"


def check_code_quality():
    """Check if the student is using proper techniques."""
    try:
        with open("main.py", "r") as f:
            code = f.read().lower()

        quality_checks = {
            "uses_regex": "re." in code,
            "uses_extract_numeric": "extract_numeric" in code,
            "validates_data": "valid" in code,
            "processes_statistics": "statistic" in code,
            "handles_error": "try:" in code or "except" in code,
            "uses_data_structures": "dict" in code and "list" in code,
        }

        return quality_checks
    except:
        return {}


def check_output_quality(student_output):
    """Check the quality of student output."""
    quality_checks = {
        "has_recipe_section": "Recipe Data Extraction:" in student_output,
        "has_statistics_section": "Statistics:" in student_output,
        "has_validation_section": "Data Validation:" in student_output,
        "has_numeric_values": bool(re.search(r"\d+\s+mins", student_output)),
        "has_calorie_info": "cal" in student_output,
        "has_rating_info": "Rating:" in student_output,
        "has_prep_time_avg": "Average prep time:" in student_output,
        "has_calorie_extremes": "Highest calories:" in student_output
        and "Lowest calories:" in student_output,
        "has_avg_rating": "Average rating:" in student_output,
        "has_difficulty_counts": "Recipes by difficulty:" in student_output,
        "has_validation_checks": "✓" in student_output,
    }

    return quality_checks


def grade_solution(student_output, expected_output, expected_recipes):
    """Grade the student's solution."""
    score = 0
    max_score = 20

    feedback = []

    # Check code quality
    code_quality = check_code_quality()
    quality_points = sum(code_quality.values())

    if quality_points >= 4:
        score += 5
        feedback.append("✓ Excellent code quality and techniques (+5 points)")
    elif quality_points >= 3:
        score += 3
        feedback.append("✓ Good code quality (+3 points)")
    elif quality_points >= 2:
        score += 1
        feedback.append("✓ Basic techniques used (+1 point)")
    else:
        feedback.append("⚠ Consider using more advanced techniques")

    # Check output quality
    output_quality = check_output_quality(student_output)
    output_points = sum(output_quality.values())

    if output_quality.get("has_recipe_section"):
        score += 5
        feedback.append("✓ Recipe data extraction section found (+5 points)")
    else:
        feedback.append("✗ Recipe data extraction section missing")

    if output_quality.get("has_statistics_section"):
        score += 5
        feedback.append("✓ Statistics section found (+5 points)")
    else:
        feedback.append("✗ Statistics section missing")

    if output_quality.get("has_validation_section"):
        score += 5
        feedback.append("✓ Data validation section found (+5 points)")
    else:
        feedback.append("✗ Data validation section missing")

    # Additional quality checks
    if output_quality.get("has_numeric_values"):
        feedback.append("✓ Numeric values extracted and processed")

    if output_quality.get("has_validation_checks"):
        feedback.append("✓ Data validation performed")

    if "regex" in student_output.lower() or "re." in open("main.py").read():
        feedback.append("✓ Regular expressions used")

    return score, max_score, feedback


def main():
    """Main grading function."""
    print("=" * 50)
    print("Beautiful Soup Quiz 4 - Grader")
    print("=" * 50)

    # Check if files exist
    if not os.path.exists("main.py"):
        print("ERROR: main.py not found!")
        return

    if not os.path.exists("index.html"):
        print("ERROR: index.html not found!")
        return

    # Load expected output
    try:
        expected_output, expected_recipes = load_expected_output()
    except Exception as e:
        print(f"ERROR: Could not load expected output: {e}")
        return

    # Run student solution
    print("Running your solution...")
    student_output, stderr = run_student_solution()

    if stderr:
        print(f"\nERRORS in your code:")
        print(stderr)

    print(f"\nYour output:")
    print("-" * 30)
    print(student_output)
    print("-" * 30)

    print(f"\nExpected output:")
    print("-" * 30)
    print(expected_output)
    print("-" * 30)

    # Grade the solution
    score, max_score, feedback = grade_solution(
        student_output, expected_output, expected_recipes
    )

    print(f"\nGRADE: {score}/{max_score}")
    print("\nFeedback:")
    for item in feedback:
        print(f"  {item}")

    # Final assessment
    if score == max_score:
        print("\n🎉 OUTSTANDING! You mastered advanced Beautiful Soup techniques!")
    elif score >= max_score * 0.8:
        print("\n👍 EXCELLENT! You have strong advanced skills!")
    elif score >= max_score * 0.6:
        print("\n📚 GOOD WORK! Keep practicing advanced techniques!")
    else:
        print("\n💡 REVIEW NEEDED! Focus on regex, data processing, and validation.")


if __name__ == "__main__":
    main()
