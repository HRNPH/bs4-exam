# Quiz 1 Grader
import os
import re
import subprocess
import sys

import requests
from bs4 import BeautifulSoup


def load_expected_output():
    """Load the expected correct output by fetching from the live URL or falling back to local index.html."""

    # Try to fetch from the live URL first
    live_url = "https://hrnph.dev/bs4-exam/exam-1"

    try:
        response = requests.get(live_url, timeout=10)
        response.raise_for_status()
        content = response.text
        print(f"✓ Successfully fetched content from live URL: {live_url}")
    except (requests.RequestException, requests.Timeout) as e:
        print(f"⚠ Could not fetch from live URL {live_url}: {e}")
        print("Falling back to local index.html file...")

        # Fallback to local file
        if not os.path.exists("index.html"):
            raise FileNotFoundError(
                "Neither live URL nor local index.html is available"
            )

        with open("index.html", "r", encoding="utf-8") as file:
            content = file.read()
        print("✓ Using local index.html file")

    soup = BeautifulSoup(content, "html.parser")

    # Extract expected data
    titles = [h2.get_text(strip=True) for h2 in soup.select("article.post h2")]
    authors = [
        p.get_text(strip=True).replace("By ", "") for p in soup.select("p.author")
    ]
    dates = [p.get_text(strip=True) for p in soup.select("p.date")]
    total_posts = len(soup.select("article.post"))

    # Build expected output
    expected = []
    expected.append("Post Titles:")
    expected.extend(titles)
    expected.append("")
    expected.append("Authors:")
    expected.extend(authors)
    expected.append("")
    expected.append("Dates:")
    expected.extend(dates)
    expected.append("")
    expected.append(f"Total Posts: {total_posts}")

    return "\n".join(expected)


def check_web_fetching_usage():
    """Check if student code uses requests library for web fetching."""
    try:
        with open("main.py", "r", encoding="utf-8") as file:
            student_code = file.read()

        # Check for requests import and usage
        has_requests_import = bool(
            re.search(r"import\s+requests|from\s+requests", student_code)
        )
        has_requests_get = bool(re.search(r"requests\.get\(", student_code))
        has_url_usage = bool(re.search(r"https?://", student_code))

        return {
            "has_requests_import": has_requests_import,
            "has_requests_get": has_requests_get,
            "has_url_usage": has_url_usage,
            "using_web_fetching": has_requests_import
            and has_requests_get
            and has_url_usage,
        }
    except FileNotFoundError:
        return {
            "has_requests_import": False,
            "has_requests_get": False,
            "has_url_usage": False,
            "using_web_fetching": False,
        }


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


def grade_solution(student_output, expected_output):
    """Grade the student's solution against expected output."""
    score = 0
    max_score = 20

    feedback = []

    # Split outputs into lines for comparison
    student_lines = [
        line.strip() for line in student_output.split("\n") if line.strip()
    ]
    expected_lines = [
        line.strip() for line in expected_output.split("\n") if line.strip()
    ]

    # Check if outputs match exactly
    if student_lines == expected_lines:
        score = max_score
        feedback.append("✓ Perfect! Output matches exactly.")
    else:
        # Partial scoring
        missing_sections = []

        # Check for Post Titles section
        if "Post Titles:" in student_output:
            score += 5
            feedback.append("✓ Post Titles section found (+5 points)")
        else:
            missing_sections.append("Post Titles section")

        # Check for Authors section
        if "Authors:" in student_output:
            score += 5
            feedback.append("✓ Authors section found (+5 points)")
        else:
            missing_sections.append("Authors section")

        # Check for Dates section
        if "Dates:" in student_output:
            score += 5
            feedback.append("✓ Dates section found (+5 points)")
        else:
            missing_sections.append("Dates section")

        # Check for Total Posts
        if "Total Posts:" in student_output:
            score += 5
            feedback.append("✓ Total Posts found (+5 points)")
        else:
            missing_sections.append("Total Posts")

        if missing_sections:
            feedback.append(f"✗ Missing sections: {', '.join(missing_sections)}")

        # Check if the number of lines is approximately correct
        if len(student_lines) >= len(expected_lines) * 0.8:
            feedback.append("✓ Output length is reasonable")
        else:
            feedback.append("✗ Output seems incomplete")

    return score, max_score, feedback


def main():
    """Main grading function."""
    print("=" * 50)
    print("Beautiful Soup Quiz 1 - Grader")
    print("=" * 50)

    # Check if main.py exists
    if not os.path.exists("main.py"):
        print("ERROR: main.py not found!")
        return

    # Check web fetching usage first
    print("Checking web fetching implementation...")
    web_check = check_web_fetching_usage()

    if not web_check["using_web_fetching"]:
        print("\n⚠ WARNING: Web fetching issues detected:")
        if not web_check["has_requests_import"]:
            print("  - No 'import requests' found in your code")
        if not web_check["has_requests_get"]:
            print("  - No 'requests.get()' usage found in your code")
        if not web_check["has_url_usage"]:
            print("  - No URL (http/https) found in your code")
        print(
            "\n💡 TIP: This quiz expects you to fetch content from the web using requests library!"
        )
        print("   Example: requests.get('https://hrnph.dev/bs4-exam/exam-1')")
    else:
        print("✓ Web fetching implementation detected!")

    # Check if index.html exists (for fallback)
    if not os.path.exists("index.html"):
        print(
            "⚠ WARNING: index.html not found! Will rely on live URL for expected output."
        )
    else:
        print("✓ Local index.html available as fallback")

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
        print("\n🎉 EXCELLENT! You got a perfect score!")
    elif score >= max_score * 0.8:
        print("\n👍 GOOD JOB! You did well!")
    elif score >= max_score * 0.6:
        print("\n📚 KEEP PRACTICING! You're getting there!")
    else:
        print("\n💡 NEEDS WORK! Review the requirements and try again.")


if __name__ == "__main__":
    main()
