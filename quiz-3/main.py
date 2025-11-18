# Quiz 3: Navigation and Sibling Traversal
# TODO: Complete this file to extract information using navigation methods

import requests
from bs4 import BeautifulSoup


def fetch_html():
    """
    Fetch HTML content from the live URL.

    Returns:
        str: HTML content from the URL, or None if fetch fails
    """
    url = "https://hrnph.dev/bs4-exam/exam-3"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML from {url}: {e}")
        return None


def navigate_dom_tree(html_content):
    """
    Extract information from HTML content using DOM navigation methods.

    Args:
        html_content (str): HTML content to parse

    Returns:
        dict: Dictionary containing all extracted information using navigation
    """
    # TODO: Create BeautifulSoup object from html_content

    # TODO: Find navigation menu siblings
    # TODO: Use find_next_sibling() or similar methods

    # TODO: Extract parent-child relationships
    # TODO: Use parent, find_parent(), children methods

    # TODO: Use find_next() and find_previous() navigation
    # TODO: Start from specific elements and navigate

    # TODO: Extract nested structure information
    # TODO: Navigate complex parent-child relationships

    return {
        "navigation_siblings": [],
        "article_authors": [],
        "navigation_results": {},
        "trending_context": [],
    }


def print_results(data):
    """
    Print the extracted data in the required format.

    Args:
        data (dict): Dictionary containing extracted information
    """
    # TODO: Print all results in the format shown in INSTRUCTION.md
    pass


def main():
    """Main function to execute the DOM navigation extraction."""
    # TODO: Fetch HTML content
    html_content = fetch_html()

    if html_content is None:
        print("Failed to fetch HTML content. Exiting.")
        return

    # TODO: Call navigate_dom_tree() and print_results()
    data = navigate_dom_tree(html_content)
    print_results(data)


if __name__ == "__main__":
    main()
