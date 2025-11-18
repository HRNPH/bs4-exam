# Quiz 2 Grader
import os
import subprocess
import sys

from bs4 import BeautifulSoup


def load_expected_output():
    """Load the expected correct output by parsing index.html directly."""

    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()

    soup = BeautifulSoup(content, "html.parser")

    # Build expected output
    expected = []

    # Product titles
    expected.append("Product Titles:")
    titles = [title.get_text(strip=True) for title in soup.select(".product-title")]
    expected.extend(titles)

    # Current prices
    expected.append("")
    expected.append("Current Prices:")
    prices = [price.get_text(strip=True) for price in soup.select(".price-current")]
    expected.extend(prices)

    # High rated products (4.5+)
    expected.append("")
    expected.append("High Rated Products (4.5+):")
    high_rated = []
    products = soup.select(".product-card")
    for product in products:
        rating_elem = product.select_one(".product-rating")
        if rating_elem and rating_elem.get("data-rating"):
            try:
                rating = float(rating_elem.get("data-rating"))
                if rating >= 4.5:
                    title = product.select_one(".product-title")
                    if title:
                        high_rated.append(title.get_text(strip=True))
            except ValueError:
                continue
    expected.extend(high_rated)

    # Product data
    expected.append("")
    expected.append("Product Data:")
    for product in products:
        title = product.select_one(".product-title")
        category = product.get("data-category", "")
        price = product.get("data-price", "")
        if title:
            expected.append(
                f"{title.get_text(strip=True)} - Category: {category}, Price: {price}"
            )

    # Multiple class elements
    expected.append("")
    expected.append("Elements with Multiple Classes:")
    buttons = [btn.get_text(strip=True) for btn in soup.select(".btn.btn-primary")]
    expected.append(f"Button texts: {', '.join(buttons)}")

    featured_products = [
        fp.get_text(strip=True)
        for fp in soup.select(".product-card.featured .product-title")
    ]
    if featured_products:
        expected.append(f"Featured product: {featured_products[0]}")

    return "\n".join(expected)


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


def check_requirements(student_output):
    """Check if specific requirements are met in the output."""
    checks = {
        "product_titles_section": "Product Titles:" in student_output,
        "current_prices_section": "Current Prices:" in student_output,
        "high_rated_section": "High Rated Products" in student_output,
        "product_data_section": "Product Data:" in student_output,
        "multiple_class_section": "Elements with Multiple Classes:" in student_output,
        "has_gaming_laptop": "Gaming Laptop Pro" in student_output,
        "has_smartphone": "SmartPhone X" in student_output,
        "has_tablet": "Tablet Pro 12" in student_output,
        "has_ultrabook": "UltraBook Elite" in student_output,
        "has_price_format": "$" in student_output,
        "has_category_laptops": "Category: laptops" in student_output,
        "has_category_phones": "Category: phones" in student_output,
        "has_category_tablets": "Category: tablets" in student_output,
        "has_button_text": "Add to Cart" in student_output,
        "has_featured_section": "Featured product:" in student_output,
    }
    return checks


def grade_solution(student_output, expected_output):
    """Grade the student's solution against expected output."""
    score = 0
    max_score = 20

    feedback = []

    # Check requirements
    requirements = check_requirements(student_output)
    passed_requirements = sum(requirements.values())
    total_requirements = len(requirements)

    # Section-based scoring (4 sections * 4 points each)
    sections = [
        (
            "Product Titles:",
            "Product titles extraction",
            requirements["product_titles_section"],
        ),
        (
            "Current Prices:",
            "Current prices extraction",
            requirements["current_prices_section"],
        ),
        (
            "High Rated Products",
            "High-rated products identification",
            requirements["high_rated_section"],
        ),
        (
            "Product Data:",
            "Product data with attributes",
            requirements["product_data_section"],
        ),
    ]

    for section_header, section_name, has_section in sections:
        if has_section:
            score += 4
            feedback.append(f"✓ {section_name} section found (+4 points)")
        else:
            feedback.append(f"✗ {section_name} section missing")

    # Additional points for advanced features (4 points)
    if requirements["multiple_class_section"]:
        score += 2
        feedback.append("✓ Multiple class elements section found (+2 points)")

    if requirements["has_button_text"] and requirements["has_featured_section"]:
        score += 2
        feedback.append("✓ Advanced selector techniques used (+2 points)")

    # Content validation
    if passed_requirements >= total_requirements * 0.8:
        feedback.append("✓ Most required content is present")
    elif passed_requirements >= total_requirements * 0.6:
        feedback.append("⚠ Some content is missing or incomplete")
    else:
        feedback.append("✗ Significant content is missing")

    return score, max_score, feedback


def main():
    """Main grading function."""
    print("=" * 50)
    print("Beautiful Soup Quiz 2 - Grader")
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
        expected_output = load_expected_output()
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
    score, max_score, feedback = grade_solution(student_output, expected_output)

    print(f"\nGRADE: {score}/{max_score}")
    print("\nFeedback:")
    for item in feedback:
        print(f"  {item}")

    # Final assessment
    if score == max_score:
        print("\n🎉 EXCELLENT! You mastered CSS selectors!")
    elif score >= max_score * 0.8:
        print("\n👍 GREAT WORK! You understand CSS selectors well!")
    elif score >= max_score * 0.6:
        print("\n📚 GOOD EFFORT! Keep practicing CSS selectors!")
    else:
        print("\n💡 REVIEW NEEDED! Focus on CSS selector syntax and techniques.")


if __name__ == "__main__":
    main()
