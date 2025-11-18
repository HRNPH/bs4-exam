# Quiz 1 Grader
import os
import subprocess
import sys

from bs4 import BeautifulSoup


def load_expected_output():
    """Load the expected correct output by parsing index.html directly."""

    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()

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
        print("\n🎉 EXCELLENT! You got a perfect score!")
    elif score >= max_score * 0.8:
        print("\n👍 GOOD JOB! You did well!")
    elif score >= max_score * 0.6:
        print("\n📚 KEEP PRACTICING! You're getting there!")
    else:
        print("\n💡 NEEDS WORK! Review the requirements and try again.")


if __name__ == "__main__":
    main()
