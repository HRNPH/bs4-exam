# Quiz 3 Grader
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

    # Navigation menu siblings
    expected.append("Navigation Menu Siblings:")
    nav_links = soup.select(".nav-list a")
    for i, link in enumerate(nav_links, 1):
        expected.append(f"{link.get_text(strip=True)} (Position: {i})")

    # Article items with authors
    expected.append("")
    expected.append("Article Items with Authors:")
    article_items = soup.select(".article-item")
    for item in article_items:
        title_elem = item.select_one("h4 a")
        author_elem = item.select_one(".article-summary .author")
        if title_elem and author_elem:
            title = title_elem.get_text(strip=True)
            author = author_elem.get_text(strip=True)
            expected.append(f"{title} - Author: {author}")

    # Navigation results
    expected.append("")
    expected.append("Navigation Results:")
    featured_title = soup.select_one(".featured-article h2")
    if featured_title:
        meta_elem = featured_title.find_next(class_="article-meta")
        if meta_elem:
            meta_text = meta_elem.get_text(" ", strip=True)
            expected.append(f"From featured article title to meta: {meta_text}")

    weather_widget = soup.select_one(".weather-widget")
    if weather_widget:
        prev_heading = weather_widget.find_previous("h3")
        if prev_heading:
            expected.append(
                f"From weather widget to previous heading: {prev_heading.get_text(strip=True)}"
            )

    # Trending items with context
    expected.append("")
    expected.append("Trending Items with Context:")
    trending_items = soup.select(".trending-item")
    trending_section = soup.select_one(".sidebar-section h3")
    section_title = (
        trending_section.get_text(strip=True) if trending_section else "Trending Topics"
    )

    for item in trending_items:
        number = item.select_one(".trending-number").get_text(strip=True)
        link = item.select_one("a").get_text(strip=True)
        time = item.select_one(".trending-time").get_text(strip=True)
        expected.append(f"{number}. {link} - {time} (Section: {section_title})")

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


def check_navigation_usage(student_code):
    """Check if the student is using proper navigation methods."""
    with open("main.py", "r") as f:
        code = f.read().lower()

    navigation_methods = [
        "find_next",
        "find_previous",
        "find_next_sibling",
        "find_previous_sibling",
        "parent",
        "find_parent",
        "children",
        "find_parents",
    ]

    used_methods = [method for method in navigation_methods if method in code]
    return used_methods


def check_requirements(student_output):
    """Check if specific requirements are met in the output."""
    checks = {
        "navigation_siblings_section": "Navigation Menu Siblings:" in student_output,
        "article_authors_section": "Article Items with Authors:" in student_output,
        "navigation_results_section": "Navigation Results:" in student_output,
        "trending_context_section": "Trending Items with Context:" in student_output,
        "has_nav_links": any(
            link in student_output for link in ["Home", "Politics", "Sports"]
        ),
        "has_positions": "Position:" in student_output,
        "has_authors": "Author:" in student_output,
        "has_navigation_results": "From featured article title to meta:"
        in student_output,
        "has_weather_navigation": "From weather widget to previous heading:"
        in student_output,
        "has_trending_numbers": any(f"{i}." in student_output for i in range(1, 10)),
        "has_trending_context": "Section:" in student_output,
        "has_sports_content": "Sports:" in student_output,
        "has_politics_content": "Politics:" in student_output,
        "has_business_content": "Business:" in student_output,
    }
    return checks


def grade_solution(student_output, expected_output):
    """Grade the student's solution against expected output."""
    score = 0
    max_score = 20

    feedback = []

    # Check if navigation methods are being used in code
    try:
        navigation_methods = check_navigation_usage("main.py")
        if navigation_methods:
            feedback.append(
                f"✓ Navigation methods detected: {', '.join(navigation_methods)}"
            )
        else:
            feedback.append(
                "⚠ Consider using more navigation methods (find_next, parent, etc.)"
            )
    except:
        feedback.append("⚠ Could not analyze code for navigation methods")

    # Check requirements
    requirements = check_requirements(student_output)
    passed_requirements = sum(requirements.values())
    total_requirements = len(requirements)

    # Section-based scoring (4 sections * 5 points each)
    sections = [
        (
            "Navigation Menu Siblings:",
            "Navigation siblings",
            requirements["navigation_siblings_section"],
        ),
        (
            "Article Items with Authors:",
            "Article parent-child relationships",
            requirements["article_authors_section"],
        ),
        (
            "Navigation Results:",
            "Navigation methods usage",
            requirements["navigation_results_section"],
        ),
        (
            "Trending Items with Context:",
            "Nested structure navigation",
            requirements["trending_context_section"],
        ),
    ]

    for section_header, section_name, has_section in sections:
        if has_section:
            score += 5
            feedback.append(f"✓ {section_name} section found (+5 points)")
        else:
            feedback.append(f"✗ {section_name} section missing")

    # Additional checks for quality
    if requirements["has_positions"]:
        feedback.append("✓ Position information included")

    if requirements["has_authors"]:
        feedback.append("✓ Author information extracted")

    if requirements["has_trending_context"]:
        feedback.append("✓ Trending items with context extracted")

    # Content completeness check
    if passed_requirements >= total_requirements * 0.8:
        feedback.append("✓ Most required content is present and well-structured")
    elif passed_requirements >= total_requirements * 0.6:
        feedback.append("⚠ Some content is missing or needs refinement")
    else:
        feedback.append("✗ Significant content is missing")

    return score, max_score, feedback


def main():
    """Main grading function."""
    print("=" * 50)
    print("Beautiful Soup Quiz 3 - Grader")
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
        print("\n🎉 EXCELLENT! You mastered DOM navigation!")
    elif score >= max_score * 0.8:
        print("\n👍 GREAT WORK! You navigate the DOM well!")
    elif score >= max_score * 0.6:
        print("\n📚 GOOD PROGRESS! Keep practicing navigation!")
    else:
        print("\n💡 NEEDS PRACTICE! Review DOM navigation methods.")


if __name__ == "__main__":
    main()
