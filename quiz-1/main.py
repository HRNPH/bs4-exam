# Quiz 1: Basic HTML Parsing with Web Fetching
# TODO: Complete this file to fetch and parse HTML from the live website

import requests
from bs4 import BeautifulSoup


def fetch_html():
    """
    Fetch HTML content from the remote URL.

    Returns:
        str: HTML content or None if fetch fails
    """
    # TODO: Use requests to fetch from https://hrnph.dev/bs4-exam/exam-1
    # TODO: Handle HTTP errors (404, timeout, connection errors)
    # TODO: Return the HTML content or None if there's an error
    pass


def parse_html(html_content):
    """
    Parse HTML and extract post information.

    Args:
        html_content (str): HTML content to parse

    Returns:
        dict: Dictionary containing titles, authors, dates, and total posts
    """
    # TODO: Create BeautifulSoup object from fetched HTML
    # TODO: Extract all post titles (h2 tags within articles)
    # TODO: Extract author names (p with class="author")
    # TODO: Extract post dates (p with class="date")
    # TODO: Count total posts (article with class="post")

    # Return a dictionary with the extracted information
    return {"titles": [], "authors": [], "dates": [], "total_posts": 0}


def print_results(data):
    """
    Print the extracted data in the required format.

    Args:
        data (dict): Dictionary containing extracted information
    """
    # TODO: Print the results in the format shown in INSTRUCTION.md
    pass


def main():
    """Main function to execute the HTML fetching and parsing."""
    try:
        # TODO: Fetch HTML from the remote URL
        # TODO: Parse the HTML if fetch was successful
        # TODO: Print the results
        # TODO: Handle fetch failures gracefully
        pass
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
